# Sovereign Debug Workflow

## Meta-Cognitive Debugging Process

```
User: "이 함수가 간헐적으로 실패해"

Claude (Meta-Cognitive Debugging):

[1. INTENT ANALYSIS]
Type: Intermittent failure
Complexity: 0.85 (race condition likely)
Impact: Production critical

[2. POLICY]
Mode: STRICT
Strategy: [hypothesis, reproduce, fix, test, prevent]

[3. ROOT CAUSE ANALYSIS]
Hypothesis Ranking:
1. Race condition (prob: 0.75) ← Most likely
2. Memory leak (prob: 0.15)
3. External dependency (prob: 0.10)

[Verification: Race condition confirmed]

[4. FIX + TEST]
Applied: Threading lock + unit tests

[5. QUALITY]
- Root Cause Accuracy: 0.95 ✓
- Fix Effectiveness: 0.92 ✓
- Regression Risk: 0.12 (low) ✓
- Time Efficiency: 0.88 ✓
- Learning: 0.90 ✓

Grade: A (0.91)

[6. EVOLUTION]
Pattern learned: "intermittent" + "async" → race condition
Added to debug knowledge base

Next: Similar cases auto-suggest threading analysis
```

## When to Use

- User reports bugs or errors
- Intermittent failures
- Performance issues
- Memory leaks
- Race conditions
