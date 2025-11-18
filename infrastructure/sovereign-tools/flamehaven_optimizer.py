"""
Flamehaven Skill Optimizer - v1.2.0
Extends Sovereign-Tools v1.1.0 with Flamehaven Governance Integration

Integrates:
- DriftLock (D < 0.3 validation)
- Scriptoria (Ω ≥ 0.90 scoring)
- Constitutional Requirements
- IRF-Calc (Philosophical reasoning metrics)
- Progressive Disclosure + Budget Packer
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Tuple, Optional
import json

# Import from sovereign-tools
import sys
sys.path.insert(0, str(Path(__file__).parent))
from budget_packer import HybridReranker, BudgetPacker, SkillContextOptimizer


class FlamehavenGovernanceMetrics:
    """
    Flamehaven-specific quality metrics:
    - Drift Score (D < 0.3)
    - Omega Score (Ω ≥ 0.90)
    - IRF Score (≥ 0.78 for philosophical reasoning)
    - Constitutional Compliance (≥ 0.80)
    """

    def __init__(self):
        self.thresholds = {
            "drift_score": 0.3,       # D < 0.3 (lower is better)
            "omega_score": 0.90,      # Ω ≥ 0.90
            "irf_score": 0.78,        # IRF ≥ 0.78 (philosophical)
            "compliance": 0.80,       # ≥ 0.80
            "principle_coverage": 0.80  # ≥ 80%
        }

    def validate_flamehaven_compliance(self, metrics: Dict[str, float]) -> Tuple[bool, List[str]]:
        """
        Validate if metrics meet Flamehaven governance standards

        Returns: (is_compliant, violations)
        """
        violations = []

        # Drift check (inverted: lower is better)
        if metrics.get("drift_score", 1.0) >= self.thresholds["drift_score"]:
            violations.append(f"Drift Score {metrics['drift_score']:.3f} ≥ {self.thresholds['drift_score']} (VIOLATION)")

        # Omega check
        if metrics.get("omega_score", 0.0) < self.thresholds["omega_score"]:
            violations.append(f"Omega Score {metrics['omega_score']:.3f} < {self.thresholds['omega_score']} (VIOLATION)")

        # Compliance check
        if metrics.get("compliance", 0.0) < self.thresholds["compliance"]:
            violations.append(f"Compliance {metrics['compliance']:.3f} < {self.thresholds['compliance']} (VIOLATION)")

        is_compliant = len(violations) == 0

        return is_compliant, violations


class FlamehavenSkillMinimizer:
    """
    Automatically minimizes Flamehaven skills while preserving governance

    Extracts:
    - Iron Law statements
    - Quantitative thresholds
    - Core workflow (high-level only)

    Moves to references/:
    - Python pseudocode → algorithms.md
    - Detailed examples → examples.md
    - Full workflow → workflow.md
    - Governance specs → governance.md
    """

    def __init__(self):
        self.iron_law_patterns = [
            r"NO .+ WITHOUT .+",
            r".+ REQUIRED",
            r".+ ≥ \d+\.\d+",
            r".+ < \d+\.\d+",
            r".+ = \d+%"
        ]

    def extract_iron_law(self, content: str) -> str:
        """Extract Iron Law section"""
        match = re.search(r'## The Iron Law\s*```([^`]+)```', content, re.DOTALL)
        if match:
            return match.group(0)
        return ""

    def extract_thresholds(self, content: str) -> Dict[str, str]:
        """Extract all quantitative thresholds"""
        thresholds = {}

        # Pattern: "Threshold: X ≥ Y" or "Score D < 0.3"
        patterns = [
            r'([A-Z][a-z\s]+(?:Score|Threshold|Coverage)):\s*([≥<>=]+\s*\d+\.\d+)',
            r'([A-Z])\s*([≥<>=]\s*\d+\.\d+)',
            r'(\w+\s+[Ss]core)\s*([≥<>=]\s*\d+\.\d+)'
        ]

        for pattern in patterns:
            matches = re.findall(pattern, content)
            for name, value in matches:
                thresholds[name.strip()] = value.strip()

        return thresholds

    def extract_overview(self, content: str) -> str:
        """Extract Overview section (first ~200 words)"""
        match = re.search(r'## Overview\s*(.+?)(?=##)', content, re.DOTALL)
        if match:
            overview = match.group(1).strip()
            # Limit to first 200 words
            words = overview.split()
            if len(words) > 200:
                overview = ' '.join(words[:200]) + '...'
            return f"## Overview\n\n{overview}"
        return ""

    def extract_when_to_use(self, content: str) -> str:
        """Extract When to Use section (condensed)"""
        match = re.search(r'## When to Use\s*(.+?)(?=##)', content, re.DOTALL)
        if match:
            when = match.group(1).strip()
            # Extract only bullet points
            bullets = re.findall(r'^[-*]\s*(.+)$', when, re.MULTILINE)
            if bullets:
                # Keep first 5 bullets
                condensed = '\n'.join(f"- {b}" for b in bullets[:5])
                return f"## When to Use\n\n{condensed}"
        return ""

    def extract_python_code(self, content: str) -> List[str]:
        """Extract all Python code blocks"""
        return re.findall(r'```python\s*(.+?)```', content, re.DOTALL)

    def minimize_skill(self, skill_md_path: Path) -> Tuple[str, Dict[str, str]]:
        """
        Minimize SKILL.md to essentials

        Returns: (minimized_content, references_dict)
        """
        content = skill_md_path.read_text(encoding='utf-8')

        # Extract YAML frontmatter
        frontmatter_match = re.match(r'^---\s*(.+?)\s*---', content, re.DOTALL)
        if frontmatter_match:
            frontmatter = f"---\n{frontmatter_match.group(1).strip()}\n---"
            content_body = content[frontmatter_match.end():].strip()
        else:
            frontmatter = ""
            content_body = content

        # Extract title
        title_match = re.search(r'^# (.+)$', content_body, re.MULTILINE)
        title = title_match.group(0) if title_match else ""

        # Extract key sections
        iron_law = self.extract_iron_law(content_body)
        overview = self.extract_overview(content_body)
        when_to_use = self.extract_when_to_use(content_body)
        thresholds = self.extract_thresholds(content_body)

        # Build minimized version
        minimized_parts = [frontmatter, title, overview]

        if when_to_use:
            minimized_parts.append(when_to_use)

        if iron_law:
            minimized_parts.append(iron_law)

        if thresholds:
            threshold_section = "## Thresholds\n\n" + '\n'.join(
                f"- **{k}**: {v}" for k, v in thresholds.items()
            )
            minimized_parts.append(threshold_section)

        # Add references pointer
        minimized_parts.append("\n## Details\n\nSee `references/` for complete workflows, algorithms, and examples.")

        minimized = '\n\n'.join(part for part in minimized_parts if part).strip()

        # Prepare references
        references = {
            "workflow.md": self._extract_workflow(content_body),
            "algorithms.md": self._extract_algorithms(content_body),
            "examples.md": self._extract_examples(content_body),
            "governance.md": self._extract_governance(content_body, thresholds)
        }

        return minimized, references

    def _extract_workflow(self, content: str) -> str:
        """Extract complete workflow details"""
        # Extract all Phase/Component/Layer sections
        sections = re.findall(r'(###? (?:Phase|Component|Layer|Tier|Step) \d+[^\n]+.+?)(?=###? (?:Phase|Component|Layer|Tier|Step)|\Z)', content, re.DOTALL)
        return '\n\n'.join(sections) if sections else "# Workflow\n\n(To be documented)"

    def _extract_algorithms(self, content: str) -> str:
        """Extract all Python pseudocode"""
        code_blocks = self.extract_python_code(content)
        if code_blocks:
            return "# Algorithms\n\n" + '\n\n'.join(f"```python\n{block}\n```" for block in code_blocks)
        return "# Algorithms\n\n(No algorithms defined)"

    def _extract_examples(self, content: str) -> str:
        """Extract example sections"""
        examples = re.findall(r'## (?:Example|Usage|Demo)[^\n]*\s*(.+?)(?=##|\Z)', content, re.DOTALL)
        if examples:
            return "# Examples\n\n" + '\n\n'.join(examples)
        return "# Examples\n\n(To be documented)"

    def _extract_governance(self, content: str, thresholds: Dict[str, str]) -> str:
        """Extract governance and validation rules"""
        gov = "# Governance Requirements\n\n"
        gov += "## Thresholds\n\n"
        gov += '\n'.join(f"- **{k}**: {v}" for k, v in thresholds.items())
        gov += "\n\n## Validation Rules\n\n"
        gov += "(Extracted from skill content)"
        return gov


class FlamehavenOptimizer(SkillContextOptimizer):
    """
    Complete Flamehaven Skill Optimizer
    Combines Budget Packer + Governance + Minimization
    """

    def __init__(self, skills_root: Path):
        self.skills_root = Path(skills_root)
        self.reranker = HybridReranker()
        self.packer = BudgetPacker()
        self.governance = FlamehavenGovernanceMetrics()
        self.minimizer = FlamehavenSkillMinimizer()

    def optimize_all_skills(self, dry_run: bool = False) -> Dict:
        """
        Optimize all skills in Flamehaven-Skills repository

        Args:
            dry_run: If True, only report what would be done

        Returns:
            {
                "skills_processed": int,
                "total_before_bytes": int,
                "total_after_bytes": int,
                "reduction_percent": float,
                "skills": [
                    {
                        "name": str,
                        "before_bytes": int,
                        "after_bytes": int,
                        "references_created": List[str]
                    },
                    ...
                ]
            }
        """
        results = {
            "skills_processed": 0,
            "total_before_bytes": 0,
            "total_after_bytes": 0,
            "skills": []
        }

        # Find all SKILL.md files
        skill_files = list(self.skills_root.glob("**/SKILL.md"))

        print(f"[+] Found {len(skill_files)} skills to optimize")

        for skill_file in skill_files:
            skill_name = skill_file.parent.name

            # Skip already optimized sovereign-* skills
            if skill_name.startswith("sovereign-"):
                print(f"[~] Skipping {skill_name} (already optimized)")
                continue

            before_size = skill_file.stat().st_size
            results["total_before_bytes"] += before_size

            try:
                # Minimize skill
                minimized, references = self.minimizer.minimize_skill(skill_file)
                after_size = len(minimized.encode('utf-8'))

                skill_result = {
                    "name": skill_name,
                    "before_bytes": before_size,
                    "after_bytes": after_size,
                    "reduction_percent": 100 * (1 - after_size / before_size),
                    "references_created": []
                }

                if not dry_run:
                    # Backup original
                    backup_path = skill_file.parent / "SKILL.md.backup"
                    skill_file.rename(backup_path)

                    # Write minimized version
                    skill_file.write_text(minimized, encoding='utf-8')

                    # Create references directory
                    refs_dir = skill_file.parent / "references"
                    refs_dir.mkdir(exist_ok=True)

                    # Write reference files
                    for ref_name, ref_content in references.items():
                        if ref_content and len(ref_content) > 50:  # Only write if meaningful content
                            ref_path = refs_dir / ref_name
                            ref_path.write_text(ref_content, encoding='utf-8')
                            skill_result["references_created"].append(ref_name)

                    print(f"[✓] {skill_name}: {before_size} → {after_size} bytes ({skill_result['reduction_percent']:.1f}% reduction)")
                else:
                    print(f"[DRY] {skill_name}: {before_size} → {after_size} bytes ({skill_result['reduction_percent']:.1f}% reduction)")

                results["total_after_bytes"] += after_size
                results["skills_processed"] += 1
                results["skills"].append(skill_result)

            except Exception as e:
                print(f"[!] Error processing {skill_name}: {e}")

        results["reduction_percent"] = 100 * (1 - results["total_after_bytes"] / results["total_before_bytes"]) if results["total_before_bytes"] > 0 else 0

        return results


# CLI Interface
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Flamehaven Skill Optimizer v1.2.0")
    parser.add_argument("--skills-dir", default="D:/Sanctum/Flamehaven-Skills/skills", help="Skills directory path")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without making changes")
    parser.add_argument("--report", action="store_true", help="Generate optimization report")

    args = parser.parse_args()

    optimizer = FlamehavenOptimizer(Path(args.skills_dir))

    print("\n" + "="*60)
    print("Flamehaven Skill Optimizer v1.2.0")
    print("="*60 + "\n")

    results = optimizer.optimize_all_skills(dry_run=args.dry_run)

    print("\n" + "="*60)
    print("OPTIMIZATION COMPLETE")
    print("="*60)
    print(f"Skills processed: {results['skills_processed']}")
    print(f"Total before: {results['total_before_bytes']:,} bytes")
    print(f"Total after: {results['total_after_bytes']:,} bytes")
    print(f"Reduction: {results['reduction_percent']:.1f}%")
    print("="*60)

    if args.report:
        report_path = Path("flamehaven_optimization_report.json")
        report_path.write_text(json.dumps(results, indent=2))
        print(f"\n[+] Report saved to: {report_path}")
