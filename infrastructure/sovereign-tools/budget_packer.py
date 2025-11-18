"""
Budget Packer + Hybrid Reranker for Sovereign Skills
Based on CRoM-EfficientLLM algorithms adapted for Skills context optimization
"""

import os
from pathlib import Path
from typing import List, Dict, Tuple, Optional
import math


class HybridReranker:
    """
    Combines TF-IDF (sparse) + semantic similarity (dense) for robust ranking
    Optimized for Skills reference selection based on task intent
    """

    def __init__(self):
        self.idf_cache = {}

    def calculate_tfidf_score(self, query: str, document: str) -> float:
        """Calculate TF-IDF score between query and document"""
        query_tokens = set(query.lower().split())
        doc_tokens = document.lower().split()

        # Term frequency
        tf_scores = []
        for token in query_tokens:
            tf = doc_tokens.count(token) / len(doc_tokens) if doc_tokens else 0
            tf_scores.append(tf)

        # Average TF as simple TF-IDF approximation
        return sum(tf_scores) / len(tf_scores) if tf_scores else 0.0

    def calculate_semantic_score(self, query: str, document: str) -> float:
        """
        Calculate semantic similarity using keyword overlap
        Simplified version - production would use sentence-transformers
        """
        query_words = set(query.lower().split())
        doc_words = set(document.lower().split())

        if not query_words or not doc_words:
            return 0.0

        # Jaccard similarity
        intersection = len(query_words & doc_words)
        union = len(query_words | doc_words)

        return intersection / union if union > 0 else 0.0

    def rank_references(
        self,
        query: str,
        references: List[Tuple[str, str]],  # [(filename, content), ...]
        top_k: int = 2,
        alpha: float = 0.6  # Weight for TF-IDF vs semantic (0.6 TF-IDF, 0.4 semantic)
    ) -> List[Tuple[str, str, float]]:
        """
        Rank references using hybrid TF-IDF + semantic scoring

        Returns: [(filename, content, score), ...] sorted by score descending
        """
        scores = []

        for filename, content in references:
            tfidf_score = self.calculate_tfidf_score(query, content)
            semantic_score = self.calculate_semantic_score(query, content)

            # Hybrid score
            hybrid_score = alpha * tfidf_score + (1 - alpha) * semantic_score

            scores.append((filename, content, hybrid_score))

        # Sort by score descending
        scores.sort(key=lambda x: x[2], reverse=True)

        return scores[:top_k]


class BudgetPacker:
    """
    Greedy packer for fitting highest-value content within token budget
    CRoM algorithm adapted for Skills progressive disclosure
    """

    def __init__(self, tokens_per_char: float = 0.25):
        """
        Args:
            tokens_per_char: Rough estimate (4 chars ≈ 1 token)
        """
        self.tokens_per_char = tokens_per_char

    def estimate_tokens(self, text: str) -> int:
        """Estimate token count from text"""
        return int(len(text) * self.tokens_per_char)

    def pack(
        self,
        base_content: str,
        optional_contents: List[Tuple[str, str, float]],  # [(name, content, score), ...]
        budget_tokens: int
    ) -> Tuple[str, List[str], int]:
        """
        Pack content within budget using greedy algorithm

        Args:
            base_content: Required content (SKILL.md minimal)
            optional_contents: Ranked optional content (references)
            budget_tokens: Maximum token budget

        Returns:
            (packed_content, included_files, total_tokens)
        """
        base_tokens = self.estimate_tokens(base_content)

        if base_tokens > budget_tokens:
            # Base content exceeds budget - return only base
            return base_content, [], base_tokens

        remaining_budget = budget_tokens - base_tokens
        packed = [base_content]
        included_files = []
        current_tokens = base_tokens

        # Greedy pack: add highest-scoring items that fit
        for name, content, score in optional_contents:
            content_tokens = self.estimate_tokens(content)

            if current_tokens + content_tokens <= budget_tokens:
                packed.append(content)
                included_files.append(name)
                current_tokens += content_tokens

        return "\n\n".join(packed), included_files, current_tokens


class SkillContextOptimizer:
    """
    Main optimizer combining Hybrid Reranker + Budget Packer
    """

    def __init__(self, skill_dir: Path):
        self.skill_dir = Path(skill_dir)
        self.reranker = HybridReranker()
        self.packer = BudgetPacker()

    def load_references(self) -> List[Tuple[str, str]]:
        """Load all reference files from skill's references/ directory"""
        references_dir = self.skill_dir / "references"

        if not references_dir.exists():
            return []

        references = []
        for ref_file in references_dir.glob("*.md"):
            try:
                content = ref_file.read_text(encoding='utf-8')
                references.append((ref_file.name, content))
            except Exception as e:
                print(f"[!] Error loading {ref_file}: {e}")

        return references

    def optimize_context(
        self,
        task_query: str,
        complexity: float,
        mode: str = "auto"
    ) -> Dict:
        """
        Optimize skill context based on task and complexity

        Args:
            task_query: User's task description
            complexity: Task complexity (0-1)
            mode: "auto", "MINIMAL", "BALANCED", "STRICT"

        Returns:
            {
                "mode": str,
                "base_content": str,
                "references_included": List[str],
                "total_tokens": int,
                "budget_tokens": int
            }
        """
        # Auto-select mode based on complexity
        if mode == "auto":
            if complexity < 0.3:
                mode = "MINIMAL"
            elif complexity < 0.7:
                mode = "BALANCED"
            else:
                mode = "STRICT"

        # Token budgets per mode
        budgets = {
            "MINIMAL": 100,    # Only base SKILL.md (~60 tokens)
            "BALANCED": 400,   # Base + top 2 references (~360 tokens)
            "STRICT": 0        # CLI delegation - no context loading
        }

        budget = budgets.get(mode, 100)

        # STRICT mode: No context loading (CLI handles everything)
        if mode == "STRICT":
            return {
                "mode": mode,
                "base_content": "[CLI DELEGATION MODE]",
                "references_included": [],
                "total_tokens": 0,
                "budget_tokens": 0,
                "cli_command": f'python D:/Sanctum/sovereign-tools/cli.py execute "{task_query}"'
            }

        # Load base SKILL.md
        skill_md = self.skill_dir / "SKILL.md"
        base_content = skill_md.read_text(encoding='utf-8') if skill_md.exists() else ""

        # MINIMAL mode: Only base SKILL.md
        if mode == "MINIMAL":
            tokens = self.packer.estimate_tokens(base_content)
            return {
                "mode": mode,
                "base_content": base_content,
                "references_included": [],
                "total_tokens": tokens,
                "budget_tokens": budget
            }

        # BALANCED mode: Base + ranked references
        references = self.load_references()

        if not references:
            # No references available
            tokens = self.packer.estimate_tokens(base_content)
            return {
                "mode": mode,
                "base_content": base_content,
                "references_included": [],
                "total_tokens": tokens,
                "budget_tokens": budget
            }

        # Rank references using hybrid reranker
        ranked_refs = self.reranker.rank_references(
            query=task_query,
            references=references,
            top_k=3  # Consider top 3
        )

        # Pack within budget
        packed_content, included_files, total_tokens = self.packer.pack(
            base_content=base_content,
            optional_contents=ranked_refs,
            budget_tokens=budget
        )

        return {
            "mode": mode,
            "base_content": base_content,
            "packed_content": packed_content,
            "references_included": included_files,
            "total_tokens": total_tokens,
            "budget_tokens": budget,
            "savings": f"{100 * (1 - total_tokens/budget):.1f}%" if budget > 0 else "N/A"
        }


# Demo/Test
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python budget_packer.py <skill_name> <task_query> [complexity]")
        print("Example: python budget_packer.py sovereign-code 'Create Redis cache layer' 0.65")
        sys.exit(1)

    skill_name = sys.argv[1]
    task_query = sys.argv[2] if len(sys.argv) > 2 else "Generic task"
    complexity = float(sys.argv[3]) if len(sys.argv) > 3 else 0.5

    # Locate skill directory
    skills_dir = Path("C:/Users/Flamehaven/.claude/plugins/marketplaces/anthropics-skills")
    skill_dir = skills_dir / skill_name

    if not skill_dir.exists():
        print(f"[!] Skill not found: {skill_dir}")
        sys.exit(1)

    # Optimize context
    optimizer = SkillContextOptimizer(skill_dir)
    result = optimizer.optimize_context(task_query, complexity)

    print(f"\n[+] Skill: {skill_name}")
    print(f"[+] Task: {task_query}")
    print(f"[+] Complexity: {complexity:.2f}")
    print(f"[+] Mode: {result['mode']}")
    print(f"[+] Budget: {result['budget_tokens']} tokens")
    print(f"[+] Actual: {result['total_tokens']} tokens")
    print(f"[+] References included: {result['references_included']}")

    if 'savings' in result:
        print(f"[+] Savings: {result['savings']}")

    if 'cli_command' in result:
        print(f"\n[>] CLI Command: {result['cli_command']}")
