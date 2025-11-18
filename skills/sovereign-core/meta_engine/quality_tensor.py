#!/usr/bin/env python3
"""
Sovereign Core - Quality Tensor v1.0.0

N-dimensional quality measurement framework.
Extends Meta-Pytest 5D tensor to arbitrary dimensions.
"""

from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class QualityDimension:
    """Single quality dimension definition"""
    name: str
    weight: float         # 0-1, must sum to 1.0 across all dimensions
    description: str
    target_s_grade: float = 0.95
    target_a_grade: float = 0.90
    target_b_grade: float = 0.80


class QualityTensor:
    """
    N-Dimensional Quality Measurement

    Generalizes Meta-Pytest's 5D tensor (κ, μ, π, α, ω)
    to support arbitrary quality dimensions for any domain.

    Grade Calculation:
    Q = Σ(dimension_score * weight)

    Grading Scale:
    - S-Grade (≥0.95): Exceptional - Production excellence
    - A-Grade (≥0.90): Excellent - Production ready
    - B-Grade (≥0.80): Good - Minor improvements needed
    - C-Grade (≥0.70): Acceptable - Improvements required
    - D-Grade (≥0.60): Poor - Major improvements required
    - F-Grade (<0.60): Failing - Critical improvements required
    """

    def __init__(self, dimensions: Dict[str, float], weights: Dict[str, float]):
        """
        Args:
            dimensions: {dimension_name: score (0-1)}
            weights: {dimension_name: weight (0-1), must sum to 1.0}
        """
        self.dimensions = dimensions
        self.weights = weights

        # Validate
        self._validate()

    def _validate(self):
        """Validate tensor integrity"""
        # Check all dimensions have weights
        for dim in self.dimensions:
            if dim not in self.weights:
                raise ValueError(f"Dimension '{dim}' missing weight")

        # Check weights sum to 1.0 (with tolerance)
        total_weight = sum(self.weights.values())
        if abs(total_weight - 1.0) > 0.01:
            raise ValueError(f"Weights must sum to 1.0, got {total_weight}")

        # Check scores in valid range
        for dim, score in self.dimensions.items():
            if score < 0 or score > 1:
                raise ValueError(f"Score for '{dim}' out of range: {score}")

    def calculate_grade(self) -> Tuple[str, float]:
        """
        Calculate overall quality grade.

        Returns:
            (grade_letter, grade_score)
            Example: ("A", 0.92)
        """
        Q = sum(self.dimensions[dim] * self.weights[dim]
                for dim in self.dimensions)

        if Q >= 0.95:
            return "S", Q
        elif Q >= 0.90:
            return "A", Q
        elif Q >= 0.80:
            return "B", Q
        elif Q >= 0.70:
            return "C", Q
        elif Q >= 0.60:
            return "D", Q
        else:
            return "F", Q

    def get_weakest_dimensions(self, threshold: float = 0.90) -> List[Tuple[str, float]]:
        """
        Get dimensions below threshold, sorted by (weight * gap).

        Returns list of (dimension_name, score) tuples.
        """
        weak_dims = []

        for dim, score in self.dimensions.items():
            if score < threshold:
                weight = self.weights[dim]
                gap = threshold - score
                priority = weight * gap
                weak_dims.append((dim, score, priority))

        # Sort by priority (highest first)
        weak_dims.sort(key=lambda x: x[2], reverse=True)

        return [(dim, score) for dim, score, _ in weak_dims]

    def get_contribution_breakdown(self) -> Dict[str, float]:
        """
        Get how much each dimension contributes to final score.

        Returns:
            {dimension_name: contribution (0-1)}
        """
        return {
            dim: self.dimensions[dim] * self.weights[dim]
            for dim in self.dimensions
        }

    def predict_grade_with_improvement(self, improvements: Dict[str, float]) -> Tuple[str, float]:
        """
        Predict new grade if specified improvements are made.

        Args:
            improvements: {dimension_name: new_score}

        Returns:
            (predicted_grade, predicted_score)
        """
        # Create hypothetical dimensions
        new_dimensions = self.dimensions.copy()
        for dim, new_score in improvements.items():
            if dim in new_dimensions:
                new_dimensions[dim] = min(1.0, new_score)

        # Calculate hypothetical grade
        new_tensor = QualityTensor(new_dimensions, self.weights)
        return new_tensor.calculate_grade()

    def to_dict(self) -> Dict[str, any]:
        """Export tensor as dictionary"""
        grade, score = self.calculate_grade()

        return {
            "dimensions": self.dimensions,
            "weights": self.weights,
            "grade": grade,
            "score": score,
            "contributions": self.get_contribution_breakdown(),
            "weak_dimensions": self.get_weakest_dimensions()
        }

    def __repr__(self) -> str:
        grade, score = self.calculate_grade()
        dims_str = ", ".join(f"{k}={v:.2f}" for k, v in self.dimensions.items())
        return f"QualityTensor(grade={grade}, score={score:.2f}, {dims_str})"


# ========== Domain-Specific Tensor Presets ==========

class CodeQualityTensor(QualityTensor):
    """
    Quality tensor for code generation.

    Dimensions:
    - Correctness (30%): Logic correctness, type safety
    - Readability (25%): Code clarity, naming, structure
    - Performance (20%): Time/space complexity
    - Security (15%): Vulnerability-free, OWASP compliance
    - Maintainability (10%): Modular, testable, documented
    """

    @classmethod
    def from_scores(cls, correctness: float, readability: float,
                   performance: float, security: float,
                   maintainability: float):
        dimensions = {
            "correctness": correctness,
            "readability": readability,
            "performance": performance,
            "security": security,
            "maintainability": maintainability
        }
        weights = {
            "correctness": 0.30,
            "readability": 0.25,
            "performance": 0.20,
            "security": 0.15,
            "maintainability": 0.10
        }
        return cls(dimensions, weights)


class DebugQualityTensor(QualityTensor):
    """
    Quality tensor for debugging.

    Dimensions:
    - Root Cause Accuracy (30%): Correctly identified root cause
    - Fix Effectiveness (25%): Problem fully resolved
    - Regression Risk (20%): Low chance of new bugs
    - Time Efficiency (15%): Fast resolution
    - Learning (10%): Knowledge captured for future
    """

    @classmethod
    def from_scores(cls, root_cause_accuracy: float, fix_effectiveness: float,
                   regression_risk: float, time_efficiency: float,
                   learning: float):
        dimensions = {
            "root_cause_accuracy": root_cause_accuracy,
            "fix_effectiveness": fix_effectiveness,
            "regression_risk": 1.0 - regression_risk,  # Invert (low risk = high quality)
            "time_efficiency": time_efficiency,
            "learning": learning
        }
        weights = {
            "root_cause_accuracy": 0.30,
            "fix_effectiveness": 0.25,
            "regression_risk": 0.20,
            "time_efficiency": 0.15,
            "learning": 0.10
        }
        return cls(dimensions, weights)


class RefactorQualityTensor(QualityTensor):
    """
    Quality tensor for refactoring.

    Dimensions:
    - Simplicity (30%): Reduced complexity
    - Cohesion (25%): High cohesion within modules
    - Coupling (20%): Low coupling between modules
    - Testability (15%): Easier to test
    - Performance (10%): No performance regression
    """

    @classmethod
    def from_scores(cls, simplicity: float, cohesion: float,
                   coupling: float, testability: float,
                   performance: float):
        dimensions = {
            "simplicity": simplicity,
            "cohesion": cohesion,
            "coupling": 1.0 - coupling,  # Invert (low coupling = high quality)
            "testability": testability,
            "performance": performance
        }
        weights = {
            "simplicity": 0.30,
            "cohesion": 0.25,
            "coupling": 0.20,
            "testability": 0.15,
            "performance": 0.10
        }
        return cls(dimensions, weights)
