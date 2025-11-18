#!/usr/bin/env python3
"""
Sovereign Core - Evolution Engine v1.0.0

Universal evolution tracking and learning system.
Extends DFI-META pattern to all domains.
"""

import json
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple


@dataclass
class EvolutionCycle:
    """Single evolution cycle record"""
    cycle: int
    timestamp: float
    quality_scores: Dict[str, float]
    grade: str
    grade_score: float
    recommendations: List[str]
    learning: Optional[str] = None
    metrics: Dict[str, Any] = None

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        if self.metrics is None:
            data["metrics"] = {}
        return data


class EvolutionEngine:
    """
    Universal Evolution & Learning Engine

    Tracks quality evolution across cycles and generates
    meta-cognitive insights and recommendations.

    DFI-META Pattern:
    1. Collect metrics from each execution
    2. Analyze trends over time
    3. Generate optimization recommendations
    4. Predict convergence to S-grade
    5. Auto-learn patterns for future tasks
    """

    def __init__(self, meta_dir: Path, domain: str):
        """
        Args:
            meta_dir: Directory for evolution data (.sovereign-meta/)
            domain: Domain name (code, debug, refactor, etc.)
        """
        self.meta_dir = Path(meta_dir)
        self.domain = domain
        self.history_file = self.meta_dir / f"{domain}_evolution_history.json"

        # Ensure directory exists
        self.meta_dir.mkdir(parents=True, exist_ok=True)

        # Load existing history
        self.history = self._load_history()

    def _load_history(self) -> List[EvolutionCycle]:
        """Load evolution history from disk"""
        if not self.history_file.exists():
            return []

        try:
            with open(self.history_file, 'r') as f:
                data = json.load(f)

            return [EvolutionCycle(**cycle) for cycle in data.get("cycles", [])]
        except Exception:
            return []

    def _save_history(self):
        """Save evolution history to disk"""
        data = {
            "domain": self.domain,
            "version": "1.0.0",
            "total_cycles": len(self.history),
            "cycles": [cycle.to_dict() for cycle in self.history]
        }

        with open(self.history_file, 'w') as f:
            json.dump(data, f, indent=2)

    def add_cycle(self, quality_scores: Dict[str, float],
                  grade: str, grade_score: float,
                  recommendations: List[str],
                  metrics: Dict[str, Any] = None) -> EvolutionCycle:
        """
        Add new evolution cycle.

        Args:
            quality_scores: Quality dimension scores
            grade: Overall grade (S/A/B/C/D/F)
            grade_score: Numeric grade score (0-1)
            recommendations: Improvement recommendations
            metrics: Additional metrics to track

        Returns:
            Created EvolutionCycle
        """
        cycle_num = len(self.history) + 1
        learning = None

        # Detect learning from previous cycle
        if len(self.history) > 0:
            prev_cycle = self.history[-1]
            learning = self._analyze_learning(prev_cycle, grade_score)

        cycle = EvolutionCycle(
            cycle=cycle_num,
            timestamp=time.time(),
            quality_scores=quality_scores,
            grade=grade,
            grade_score=grade_score,
            recommendations=recommendations,
            learning=learning,
            metrics=metrics or {}
        )

        self.history.append(cycle)
        self._save_history()

        return cycle

    def _analyze_learning(self, prev_cycle: EvolutionCycle,
                         current_score: float) -> Optional[str]:
        """Generate learning insight by comparing cycles"""
        prev_score = prev_cycle.grade_score

        if current_score > prev_score:
            improvement = ((current_score - prev_score) / prev_score) * 100
            return f"Quality improved by {improvement:.1f}% ({prev_cycle.grade} → grade)"
        elif current_score < prev_score:
            degradation = ((prev_score - current_score) / prev_score) * 100
            return f"Quality degraded by {degradation:.1f}% - review recent changes"
        else:
            return "Quality stable - consider new optimization strategies"

    def get_trend(self, window: int = 5) -> str:
        """
        Analyze quality trend over recent cycles.

        Args:
            window: Number of recent cycles to analyze

        Returns:
            "improving", "degrading", "stable", or "insufficient_data"
        """
        if len(self.history) < 2:
            return "insufficient_data"

        recent = self.history[-window:]
        if len(recent) < 2:
            return "insufficient_data"

        # Calculate linear trend
        scores = [c.grade_score for c in recent]
        n = len(scores)

        # Simple linear regression slope
        x_mean = (n - 1) / 2
        y_mean = sum(scores) / n

        numerator = sum((i - x_mean) * (scores[i] - y_mean) for i in range(n))
        denominator = sum((i - x_mean) ** 2 for i in range(n))

        if denominator == 0:
            return "stable"

        slope = numerator / denominator

        if slope > 0.01:
            return "improving"
        elif slope < -0.01:
            return "degrading"
        else:
            return "stable"

    def predict_convergence(self, target_score: float = 0.95) -> Tuple[Optional[int], float]:
        """
        Predict how many cycles until target score reached.

        Args:
            target_score: Target quality score (default: S-grade 0.95)

        Returns:
            (estimated_cycles, confidence)
            Returns (None, 0.0) if prediction not possible
        """
        if len(self.history) < 3:
            return None, 0.0

        # Use recent cycles for prediction
        recent = self.history[-5:]
        scores = [c.grade_score for c in recent]

        # Calculate improvement rate
        n = len(scores)
        x_mean = (n - 1) / 2
        y_mean = sum(scores) / n

        numerator = sum((i - x_mean) * (scores[i] - y_mean) for i in range(n))
        denominator = sum((i - x_mean) ** 2 for i in range(n))

        if denominator == 0 or numerator <= 0:
            return None, 0.0

        improvement_rate = numerator / denominator

        # Current score
        current_score = scores[-1]

        # Already at or above target
        if current_score >= target_score:
            return 0, 1.0

        # Predict cycles needed
        gap = target_score - current_score
        cycles_needed = int(gap / improvement_rate)

        # Confidence based on data points and trend consistency
        confidence = min(len(self.history) / 10, 1.0)  # More data = higher confidence

        # Reduce confidence if trend is inconsistent
        variance = sum((scores[i] - (scores[0] + i * improvement_rate)) ** 2
                      for i in range(n)) / n
        if variance > 0.01:
            confidence *= 0.7

        return cycles_needed, confidence

    def generate_recommendations(self, current_scores: Dict[str, float],
                                weights: Dict[str, float]) -> List[str]:
        """
        Generate optimization recommendations based on history.

        Args:
            current_scores: Current quality scores
            weights: Dimension weights

        Returns:
            List of recommendations
        """
        recommendations = []

        # Find weakest high-weight dimensions
        weak_dims = []
        for dim, score in current_scores.items():
            if score < 0.90 and weights.get(dim, 0) > 0.15:
                gap = 0.90 - score
                priority = gap * weights[dim]
                weak_dims.append((dim, score, priority))

        weak_dims.sort(key=lambda x: x[2], reverse=True)

        # Recommendations for weak dimensions
        for dim, score, _ in weak_dims[:3]:  # Top 3
            target = 0.95 if score >= 0.90 else 0.90
            recommendations.append(
                f"Improve {dim} from {score:.2f} to {target:.2f}"
            )

        # Historical pattern recommendations
        if len(self.history) >= 3:
            trend = self.get_trend()

            if trend == "degrading":
                recommendations.append(
                    "Quality degrading - review recent changes and revert if needed"
                )
            elif trend == "stable" and self.history[-1].grade in ["B", "C"]:
                recommendations.append(
                    "Quality plateau detected - try new optimization strategies"
                )

        # Convergence prediction
        cycles_to_s, confidence = self.predict_convergence()
        if cycles_to_s is not None and confidence > 0.5:
            if cycles_to_s == 0:
                recommendations.append("S-grade achieved! Focus on maintaining excellence")
            elif cycles_to_s <= 3:
                recommendations.append(
                    f"S-grade achievable in {cycles_to_s} cycles (confidence: {confidence:.0%})"
                )
            else:
                recommendations.append(
                    f"Estimated {cycles_to_s} cycles to S-grade - stay consistent"
                )

        return recommendations

    def get_summary(self) -> Dict[str, Any]:
        """Get evolution summary statistics"""
        if not self.history:
            return {
                "total_cycles": 0,
                "current_grade": None,
                "trend": "insufficient_data"
            }

        current = self.history[-1]
        trend = self.get_trend()
        cycles_to_s, confidence = self.predict_convergence()

        return {
            "total_cycles": len(self.history),
            "current_grade": current.grade,
            "current_score": current.grade_score,
            "trend": trend,
            "convergence_prediction": {
                "cycles_to_s_grade": cycles_to_s,
                "confidence": confidence
            } if cycles_to_s is not None else None,
            "best_cycle": max(self.history, key=lambda c: c.grade_score).cycle,
            "best_score": max(c.grade_score for c in self.history)
        }
