# Sovereign Core v1.0.0

**Universal Meta-Cognitive Framework for AI Tasks**

Foundation layer for Meta-Cognitive Lead Engine ecosystem.

## Overview

Sovereign Core provides the universal meta-cognitive framework that all domain-specific skills (code, debug, refactor, etc.) inherit from. It implements:

- **CGE v2.3 Pattern**: Intent → Validation → Policy → Plan → Execute → Quality → Evolve → Explain
- **N-Dimensional Quality**: Arbitrary quality dimensions with weighted grading
- **Evolution Engine**: Continuous learning and convergence prediction
- **Token Optimization**: Adaptive resource delegation (Skills ↔ CLI)

## Quick Start

Sovereign Core is not directly used. Instead, use domain-specific skills:

```
# Code generation
"함수 만들어줘: 파일 업로드 API"
→ sovereign-code skill activates
  → Uses Sovereign Core foundation

# Debugging
"이 버그 고쳐줘"
→ sovereign-debug skill activates
  → Uses Sovereign Core foundation

# Refactoring
"이 코드 리팩토링해줘"
→ sovereign-refactor skill activates
  → Uses Sovereign Core foundation
```

## Architecture

```
┌─────────────────────────────────────────────┐
│ Sovereign Core (Foundation)                 │
│ - MetaCognitiveEngine                       │
│ - QualityTensor (N-dimensional)             │
│ - EvolutionEngine                           │
└─────────────────────────────────────────────┘
           ↑            ↑            ↑
     ┌─────┴─────┬──────┴──────┬─────┴──────┐
     │           │             │            │
sovereign-code sovereign-debug sovereign-refactor ...
```

## Core Components

### 1. MetaCognitiveEngine

Universal base class for all domain engines:

```python
class MetaCognitiveEngine(ABC):
    def execute(user_input, context):
        # 8-step CGE pattern
        intent = analyze_intent()
        policy = resolve_policy()
        plan = generate_plan()
        result = execute_task()
        quality = measure_quality()
        evolve = track_evolution()
        return explain()
```

### 2. QualityTensor

N-dimensional quality measurement:

```python
tensor = QualityTensor(
    dimensions={
        "correctness": 0.95,
        "readability": 0.91,
        "performance": 0.87,
        "security": 0.90,
        "maintainability": 0.89
    },
    weights={
        "correctness": 0.30,
        "readability": 0.25,
        "performance": 0.20,
        "security": 0.15,
        "maintainability": 0.10
    }
)

grade, score = tensor.calculate_grade()  # ("A", 0.90)
```

### 3. EvolutionEngine

Continuous learning and improvement:

```python
engine = EvolutionEngine(meta_dir=".sovereign-meta", domain="code")

# After each execution
cycle = engine.add_cycle(
    quality_scores={"correctness": 0.95, ...},
    grade="A",
    grade_score=0.90,
    recommendations=[...]
)

# Get insights
trend = engine.get_trend()  # "improving"
cycles_to_s, confidence = engine.predict_convergence()  # (3, 0.85)
```

## Domain Skills

### sovereign-code
Code generation with quality-gated output.

**Dimensions**: Correctness (30%), Readability (25%), Performance (20%), Security (15%), Maintainability (10%)

### sovereign-debug
Intelligent debugging with root cause analysis.

**Dimensions**: Root Cause Accuracy (30%), Fix Effectiveness (25%), Regression Risk (20%), Time Efficiency (15%), Learning (10%)

### sovereign-refactor
Systematic refactoring with architectural improvements.

**Dimensions**: Simplicity (30%), Cohesion (25%), Coupling (20%), Testability (15%), Performance (10%)

## Quality Evolution Example

```
Cycle 1: Grade B (0.82)
- correctness: 0.90 ✓
- readability: 0.75 ← weak
- performance: 0.85 ✓
- security: 0.80 ✓
- maintainability: 0.80 ✓

Recommendations:
→ Improve readability from 0.75 to 0.90

[User applies recommendations]

Cycle 2: Grade A (0.91)
- correctness: 0.92 ✓
- readability: 0.92 ✓ improved!
- performance: 0.87 ✓
- security: 0.85 ✓
- maintainability: 0.88 ✓

Learning: Quality improved by 10.9% (B → A)

Convergence Prediction: S-grade in 2 cycles (confidence: 87%)
```

## Token Optimization

Adaptive runtime mode selection:

| Complexity | Mode | Token Usage | Delegation |
|------------|------|-------------|------------|
| < 0.3 | MINIMAL | 500-2,000 | Skills inline |
| 0.3-0.7 | BALANCED | 1,000 | Hybrid |
| > 0.7 | STRICT | 500 | CLI subprocess |

## Version

**v1.0.0** - Production Release (2025-11-17)

Built with CGE v2.3, Meta-Pytest N-D extension, DFI-META evolution.
