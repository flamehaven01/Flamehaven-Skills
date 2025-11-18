# Algorithms

```python
# Measured drift
measured_drift = current_state - baseline_identity

# IDMR recall strength
recall = 0.92 * recall_prev + 0.08 * consistency

# Drift reduction
drift_new = drift - (correction_gain * recall * measured_drift)

# Consistency update
consistency = 0.85 * consistency + 0.1 * (1 - measured_drift) + 0.05 * recall

```

```python
def conscience_check(intent, policy, state):
    # Hard rule violations → BLOCK
    if banned_topic in intent:
        return "BLOCK"

    # Drift or consistency issues → REPAIR
    if state.drift > max_drift or state.consistency < min_consistency:
        return "REPAIR"

    # Passed → ACT
    return "ACT"

```