# Evolution Engine

## Overview

Tracks quality progression across cycles with convergence prediction.

## Evolution Example

```python
Cycle 1: Grade B (0.82)
→ Recommendations generated

Cycle 3: Grade A (0.90)
→ Learning: "Quality improved by 9.8%"

Cycle 7: Grade S (0.96)
→ Convergence achieved!
```

## Features

### 1. Trend Analysis
Analyzes quality progression trend:
- **improving**: Quality consistently increasing
- **degrading**: Quality consistently decreasing
- **stable**: Quality plateau reached

### 2. Convergence Prediction
Predicts cycles needed to reach S-grade:
```python
{
  "cycles_to_s": 2,
  "confidence": 0.87
}
```

### 3. Pattern Learning
Captures domain-specific insights:
```python
{
  "pattern": "High complexity + low coverage → extract methods",
  "success_rate": 0.94,
  "time_reduction": 0.50
}
```

### 4. Auto-Recommendations
Generates dimension-aware improvement suggestions:
```python
[
  "Improve readability: Add docstrings",
  "Improve security: Add input validation",
  "Consider rate limiting for production"
]
```

## Evolution Storage

All domain skills use `.sovereign-meta/`:

```
project/
└── .sovereign-meta/
    ├── code_evolution_history.json
    ├── debug_evolution_history.json
    └── refactor_evolution_history.json
```

## Storage Format

```json
{
  "domain": "code",
  "cycles": [
    {
      "cycle_id": 1,
      "timestamp": "2025-11-17T12:00:00",
      "quality_scores": {
        "correctness": 0.90,
        "readability": 0.75,
        "performance": 0.85,
        "security": 0.80,
        "maintainability": 0.80
      },
      "grade": "B",
      "grade_score": 0.82,
      "recommendations": [
        "Improve readability from 0.75 to 0.90"
      ]
    }
  ],
  "trend": "improving",
  "convergence_prediction": {
    "cycles_to_s": 2,
    "confidence": 0.87
  }
}
```
