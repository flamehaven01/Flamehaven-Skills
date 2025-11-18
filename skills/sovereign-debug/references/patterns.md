# Sovereign Debug Pattern Learning

## Evolution & Pattern Recognition

```
Cycle 5: Race Condition Pattern Mastered
- Auto-recognize: "intermittent" keyword → race condition check
- Auto-suggest: Threading analysis tools
- Confidence: 95% on similar cases
- Time reduction: 70% (2 hours → 30 minutes)
```

## Quality Dimensions (5D)

**Formula**: Q = 0.30×Root Cause + 0.25×Fix + 0.20×Regression + 0.15×Time + 0.10×Learning

1. **Root Cause Accuracy (30%)**: Correctly identified actual cause
2. **Fix Effectiveness (25%)**: Problem fully resolved
3. **Regression Risk (20%)**: Low chance of introducing new bugs
4. **Time Efficiency (15%)**: Fast resolution
5. **Learning (10%)**: Knowledge captured for future

## Common Debug Patterns

### Pattern 1: Intermittent Failures
**Symptoms**: "간헐적으로", "sometimes", "randomly"
**Likely Causes**:
- Race conditions (75%)
- Memory leaks (15%)
- External dependencies (10%)
**Approach**: STRICT mode, threading analysis

### Pattern 2: Performance Degradation
**Symptoms**: "느려짐", "slow", "performance"
**Likely Causes**:
- N+1 queries (40%)
- Memory leaks (30%)
- Inefficient algorithms (30%)
**Approach**: BALANCED mode, profiling

### Pattern 3: Null/Undefined Errors
**Symptoms**: "NullPointerException", "undefined is not an object"
**Likely Causes**:
- Missing validation (60%)
- Async timing issues (30%)
- Type mismatches (10%)
**Approach**: MINIMAL mode, add guards

## Learning Storage

`.sovereign-meta/debug_evolution_history.json`:
```json
{
  "patterns": [
    {
      "pattern_id": "race_condition_001",
      "keywords": ["intermittent", "async", "concurrent"],
      "success_rate": 0.95,
      "avg_resolution_time": "30min",
      "recommended_approach": "threading_analysis"
    }
  ]
}
```
