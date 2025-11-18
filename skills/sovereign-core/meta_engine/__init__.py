"""
Sovereign Core Meta-Cognitive Engine v1.0.0

Universal meta-cognitive framework for all AI tasks.
Foundation for sovereign-* domain skills.
"""

from .base import MetaCognitiveEngine, Intent, Policy, ExecutionPlan
from .quality_tensor import QualityTensor, QualityDimension
from .evolution_engine import EvolutionEngine, EvolutionCycle

__version__ = "1.0.0"
__all__ = [
    "MetaCognitiveEngine",
    "Intent",
    "Policy",
    "ExecutionPlan",
    "QualityTensor",
    "QualityDimension",
    "EvolutionEngine",
    "EvolutionCycle",
]
