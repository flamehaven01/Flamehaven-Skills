#!/usr/bin/env python3
"""
Sovereign Core - Meta-Cognitive Base Engine v1.0.0

Universal framework implementing CGE pattern:
Intent → Validation → Policy → Plan → Execute → Quality → Evolve → Explain
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Any, List, Optional, Callable
import time
import hashlib


class RuntimeMode(Enum):
    """Adaptive runtime modes based on complexity"""
    MINIMAL = "MINIMAL"      # <0.3: Fast, simple
    BALANCED = "BALANCED"    # 0.3-0.7: Optimal balance
    STRICT = "STRICT"        # >0.7: Complete validation


@dataclass
class Intent:
    """Universal intent representation"""
    task: str                               # What to do
    domain: str                             # Which domain (code, debug, etc.)
    user_context: Dict[str, Any] = field(default_factory=dict)
    complexity: float = 0.0                 # 0-1 scale
    priority: int = 5                       # 1-10
    quality_target: str = "A-grade"        # Target quality


@dataclass
class Policy:
    """Execution policy based on intent analysis"""
    mode: RuntimeMode
    complexity: float
    checks: List[str]
    resource_allocation: Dict[str, Any]
    quality_weights: Dict[str, float]
    estimated_duration: float

    def to_dict(self) -> Dict[str, Any]:
        return {
            "mode": self.mode.value,
            "complexity": self.complexity,
            "checks": self.checks,
            "resource_allocation": self.resource_allocation,
            "quality_weights": self.quality_weights,
            "estimated_duration": self.estimated_duration
        }


@dataclass
class ExecutionPlan:
    """Detailed execution plan"""
    steps: List[Dict[str, Any]]
    estimated_duration: float
    resource_requirements: Dict[str, Any]
    validation_points: List[str]
    rollback_strategy: List[str]


class MetaCognitiveEngine(ABC):
    """
    Universal Meta-Cognitive Engine

    All domain-specific engines (code, debug, refactor, etc.)
    inherit from this base class and implement domain-specific methods.

    Core Pattern (CGE v2.3):
    1. Intent Analysis - understand what user wants
    2. Validation - verify context and constraints
    3. Policy Resolution - decide how to approach
    4. Plan Generation - create execution plan
    5. Execution - perform the task
    6. Quality Measurement - evaluate result
    7. Evolution Tracking - learn from outcome
    8. Explanation - communicate to user
    """

    def __init__(self, domain: str):
        self.domain = domain
        self.evolution_history = []
        self.current_cycle = 0

    # ========== Abstract Methods (Domain-Specific) ==========

    @abstractmethod
    def analyze_intent(self, user_input: str, context: Dict[str, Any]) -> Intent:
        """
        Analyze user intent and extract task details.
        Domain-specific implementation required.
        """
        pass

    @abstractmethod
    def calculate_complexity(self, intent: Intent) -> float:
        """
        Calculate task complexity (0-1 scale).
        Domain-specific factors.
        """
        pass

    @abstractmethod
    def get_quality_dimensions(self) -> List[str]:
        """
        Return list of quality dimensions for this domain.
        Example: ["correctness", "readability", "performance"]
        """
        pass

    @abstractmethod
    def get_quality_weights(self) -> Dict[str, float]:
        """
        Return weights for quality dimensions.
        Must sum to 1.0.
        """
        pass

    @abstractmethod
    def measure_quality(self, result: Any, intent: Intent) -> Dict[str, float]:
        """
        Measure quality across domain-specific dimensions.
        Return dict of dimension -> score (0-1).
        """
        pass

    @abstractmethod
    def execute_task(self, plan: ExecutionPlan, intent: Intent) -> Any:
        """
        Execute the actual task.
        Domain-specific implementation.
        """
        pass

    # ========== Universal Methods (Shared Logic) ==========

    def validate_context(self, intent: Intent) -> Dict[str, Any]:
        """
        Validate intent and context.
        Can be overridden for domain-specific validation.
        """
        validation = {
            "valid": True,
            "confidence": 0.95,
            "warnings": [],
            "errors": []
        }

        # Basic validation
        if not intent.task:
            validation["valid"] = False
            validation["errors"].append("Empty task")
            validation["confidence"] = 0.0

        if intent.complexity < 0 or intent.complexity > 1:
            validation["warnings"].append(f"Complexity out of range: {intent.complexity}")

        return validation

    def resolve_policy(self, intent: Intent, validation: Dict[str, Any]) -> Policy:
        """
        Resolve execution policy based on complexity and intent.
        Universal logic with domain customization.
        """
        complexity = intent.complexity

        # Select runtime mode
        if complexity < 0.3:
            mode = RuntimeMode.MINIMAL
            checks = ["basic_validation"]
            estimated_duration = 5.0
        elif complexity > 0.7:
            mode = RuntimeMode.STRICT
            checks = ["validation", "security", "performance", "testing"]
            estimated_duration = 60.0
        else:
            mode = RuntimeMode.BALANCED
            checks = ["validation", "basic_testing"]
            estimated_duration = 20.0

        # Resource allocation
        if mode == RuntimeMode.MINIMAL:
            resource_allocation = {"use_cli": False, "parallel": False}
        elif mode == RuntimeMode.STRICT:
            resource_allocation = {"use_cli": True, "parallel": True}
        else:
            resource_allocation = {"use_cli": False, "parallel": False}

        return Policy(
            mode=mode,
            complexity=complexity,
            checks=checks,
            resource_allocation=resource_allocation,
            quality_weights=self.get_quality_weights(),
            estimated_duration=estimated_duration
        )

    def generate_plan(self, policy: Policy, intent: Intent) -> ExecutionPlan:
        """
        Generate execution plan based on policy.
        Can be overridden for domain-specific planning.
        """
        steps = []

        # Standard steps
        steps.append({
            "step": 1,
            "action": "validate_input",
            "timeout": 1.0
        })

        steps.append({
            "step": 2,
            "action": "prepare_resources",
            "timeout": 2.0
        })

        steps.append({
            "step": 3,
            "action": "execute_primary",
            "timeout": policy.estimated_duration * 0.8
        })

        steps.append({
            "step": 4,
            "action": "validate_output",
            "timeout": 2.0
        })

        if "testing" in policy.checks:
            steps.append({
                "step": 5,
                "action": "run_tests",
                "timeout": 10.0
            })

        return ExecutionPlan(
            steps=steps,
            estimated_duration=policy.estimated_duration,
            resource_requirements=policy.resource_allocation,
            validation_points=["input_validated", "output_validated"],
            rollback_strategy=["restore_state", "cleanup_resources"]
        )

    def track_evolution(self, quality_scores: Dict[str, float],
                       grade: str, grade_score: float,
                       recommendations: List[str]) -> None:
        """
        Track evolution cycle.
        Universal implementation.
        """
        from .evolution_engine import EvolutionCycle

        self.current_cycle += 1

        cycle = EvolutionCycle(
            cycle=self.current_cycle,
            timestamp=time.time(),
            quality_scores=quality_scores,
            grade=grade,
            grade_score=grade_score,
            recommendations=recommendations,
            learning=None
        )

        # Detect learning
        if len(self.evolution_history) > 0:
            prev_score = self.evolution_history[-1].grade_score
            if grade_score > prev_score:
                improvement = ((grade_score - prev_score) / prev_score) * 100
                cycle.learning = f"Quality improved by {improvement:.1f}%"
            elif grade_score < prev_score:
                cycle.learning = "Quality degraded - review recent changes"

        self.evolution_history.append(cycle)

    def generate_recommendations(self, quality_scores: Dict[str, float],
                                grade: str) -> List[str]:
        """
        Generate improvement recommendations.
        Can be overridden for domain-specific recommendations.
        """
        recommendations = []
        weights = self.get_quality_weights()

        # Find weakest dimensions
        for dim, score in quality_scores.items():
            if score < 0.90:
                weight = weights.get(dim, 0.0)
                if weight > 0.15:  # Significant dimension
                    recommendations.append(
                        f"Improve {dim} from {score:.2f} to 0.90+ "
                        f"(weight: {weight:.0%})"
                    )

        # Grade-specific recommendations
        if grade == "F":
            recommendations.append("Major improvements needed across all dimensions")
        elif grade in ["C", "D"]:
            recommendations.append("Focus on highest-weight dimensions first")
        elif grade == "B":
            recommendations.append("Close to A-grade - refine weak dimensions")
        elif grade == "A":
            recommendations.append("Optimize for S-grade - aim for 0.95+ on all dimensions")

        return recommendations

    def explain(self, result: Any, quality_scores: Dict[str, float],
               grade: str, grade_score: float,
               recommendations: List[str]) -> Dict[str, Any]:
        """
        Generate user-friendly explanation.
        Universal structure with domain customization.
        """
        return {
            "result": result,
            "quality": {
                "grade": grade,
                "score": grade_score,
                "dimensions": quality_scores
            },
            "recommendations": recommendations,
            "evolution": {
                "cycle": self.current_cycle,
                "history_available": len(self.evolution_history) > 0
            },
            "metadata": {
                "domain": self.domain,
                "timestamp": time.time()
            }
        }

    # ========== Main Execution Pipeline ==========

    def execute(self, user_input: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Universal execution pipeline (CGE pattern).

        This is the main entry point that orchestrates all steps.
        """
        if context is None:
            context = {}

        start_time = time.perf_counter()

        try:
            # 1. INTENT ANALYSIS
            intent = self.analyze_intent(user_input, context)
            intent.complexity = self.calculate_complexity(intent)

            # 2. VALIDATION
            validation = self.validate_context(intent)
            if not validation["valid"]:
                return {
                    "success": False,
                    "error": "Validation failed",
                    "details": validation["errors"]
                }

            # 3. POLICY RESOLUTION
            policy = self.resolve_policy(intent, validation)

            # 4. PLAN GENERATION
            plan = self.generate_plan(policy, intent)

            # 5. EXECUTION
            result = self.execute_task(plan, intent)

            # 6. QUALITY MEASUREMENT
            quality_scores = self.measure_quality(result, intent)

            # Calculate overall grade
            from .quality_tensor import QualityTensor
            tensor = QualityTensor(
                dimensions=quality_scores,
                weights=self.get_quality_weights()
            )
            grade, grade_score = tensor.calculate_grade()

            # 7. EVOLUTION TRACKING
            recommendations = self.generate_recommendations(quality_scores, grade)
            self.track_evolution(quality_scores, grade, grade_score, recommendations)

            # 8. EXPLANATION
            explanation = self.explain(
                result, quality_scores, grade, grade_score, recommendations
            )

            total_duration = (time.perf_counter() - start_time) * 1000
            explanation["performance"] = {
                "total_duration_ms": total_duration,
                "estimated_duration_ms": policy.estimated_duration * 1000,
                "efficiency": min(1.0, (policy.estimated_duration * 1000) / total_duration)
            }

            explanation["success"] = True
            return explanation

        except Exception as e:
            error_duration = (time.perf_counter() - start_time) * 1000
            return {
                "success": False,
                "error": str(e),
                "performance": {"total_duration_ms": error_duration},
                "metadata": {"domain": self.domain}
            }
