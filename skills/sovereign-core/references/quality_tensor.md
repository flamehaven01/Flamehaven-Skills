# N-Dimensional Quality Tensor

## Overview

Generalizes Meta-Pytest's 5D tensor to arbitrary dimensions.

**Formula**: Q = Σ(dimension_score × weight)

## Grading Scale

- **S-Grade (≥0.95)**: Exceptional
- **A-Grade (≥0.90)**: Production ready
- **B-Grade (≥0.80)**: Good
- **C-Grade (≥0.70)**: Acceptable
- **D-Grade (≥0.60)**: Poor
- **F-Grade (<0.60)**: Failing

## Example Dimensions by Domain

### Code Generation
- Correctness (30%)
- Readability (25%)
- Performance (20%)
- Security (15%)
- Maintainability (10%)

### Debugging
- Root Cause Accuracy (30%)
- Fix Effectiveness (25%)
- Regression Risk (20%)
- Time Efficiency (15%)
- Learning (10%)

### Refactoring
- Simplicity (30%)
- Cohesion (25%)
- Coupling (20%)
- Testability (15%)
- Performance (10%)

## Custom Dimensions

Any domain can define custom dimensions:

```python
class CustomQualityTensor(QualityTensor):
    def __init__(self):
        dimensions = {
            "dimension1": 0.85,
            "dimension2": 0.92,
            "dimension3": 0.78
        }
        weights = {
            "dimension1": 0.40,
            "dimension2": 0.35,
            "dimension3": 0.25
        }
        super().__init__(dimensions, weights)
```

## Quality Calculation

```python
Q = Σ(dimension_i × weight_i)

Example:
Q = 0.94×0.30 + 0.91×0.25 + 0.87×0.20 + 0.90×0.15 + 0.89×0.10
Q = 0.282 + 0.2275 + 0.174 + 0.135 + 0.089
Q = 0.9075 → A-Grade
```
