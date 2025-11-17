---
name: drift-detection
description: Three-tier semantic preservation validation (Shallow/Deep/Attention) - ensures output maintains original intent and principles through ASDP DriftLock + AEGIS-C SAI metrics
---

# Drift-Free Execution

## Overview

Random outputs violate principles. Quick execution masks semantic drift.

**Core principle:** ALWAYS validate semantic preservation before delivery. Drift = failure.

**Violating the letter of this process is violating the spirit of execution.**

## The Iron Law

```
NO OUTPUT DELIVERY WITHOUT DRIFT VALIDATION FIRST
Drift Score D < 0.3 REQUIRED
```

If you haven't validated drift score < 0.3, you cannot deliver.

## When to Use

Use for ANY output:
- Code generation
- Document writing
- Translation
- Refactoring
- API responses
- Academic papers
- Any transformation task

**Use this ESPECIALLY when:**
- User provided explicit principles/requirements
- Output modifies existing content
- Translation or transformation involved
- Quality is critical
- Compliance required

**Don't skip when:**
- Output seems simple (simple tasks drift too)
- You're in a hurry (drift causes rework)
- No explicit principles given (infer them)

## Three-Tier Validation

You MUST pass ALL three tiers before delivery.

### Tier 1: SHALLOW (100% Coverage)

**BEFORE delivery:**

1. **Extract Principles**
   - User requirements
   - Functional specs
   - Quality criteria
   - Domain constraints

2. **Keyword Matching**
   ```python
   for principle in principles:
       if principle.lower() not in output.lower():
           DRIFT_DETECTED()
   ```

3. **Pattern Checking**
   - Required structures present?
   - Forbidden patterns absent?
   - Format compliance?

**Threshold:** ≥ 80% principle coverage required

### Tier 2: DEEP (Probabilistic LLM)

**WHEN Tier 1 passes AND random() < 10%:**

1. **Semantic Evaluation**
   ```
   Prompt LLM:
   "Does this output adhere to these principles?
   Principles: {principles}
   Output: {output}
   Score 0.0-1.0 where 1.0 = perfect adherence."
   ```

2. **Contextual Understanding**
   - LLM evaluates meaning, not keywords
   - Catches subtle semantic shifts
   - Validates intent preservation

**Threshold:** ≥ 0.9 LLM score required

### Tier 3: ATTENTION (Structural SAI)

**WHEN generation attention available:**

1. **Compute SAI Vector**
   ```
   T = Temporal Coherence (entropy focus)
   E = Entropic Intelligence (perplexity)
   C = Cooperative Cognition (head similarity)
   S = Structural Integrity (graph properties)

   SAI = [T, E, C, S] ∈ [0,1]⁴
   ```

2. **Calculate Drift Score**
   ```
   D = 1 - (0.3·T + 0.25·E + 0.25·C + 0.2·S)
   ```

3. **Action Decision**
   ```
   D < 0.3 → OBSERVE  (deliver)
   D < 0.7 → REFACTOR (regenerate)
   D ≥ 0.7 → INHIBIT  (block)
   ```

**Threshold:** D < 0.3 required for delivery

## Unified Decision Matrix

| Shallow | Deep | Attention | Action |
|---------|------|-----------|--------|
| ✓ | ✓ | D<0.3 | **DELIVER** |
| ✓ | ✓ | D<0.7 | **REFACTOR** |
| ✓ | ✓ | D≥0.7 | **INHIBIT** |
| ✓ | ✗ | * | **REFACTOR** |
| ✗ | * | * | **INHIBIT** |

## Red Flags - STOP and Validate

If you catch yourself thinking:
- "Quick delivery for now, validate later"
- "User won't notice small changes"
- "Close enough to requirements"
- "Skip validation, I'll manually check"
- "It's probably fine"
- "I don't have explicit principles"
- "Validation is overkill for this"

**ALL of these mean: STOP. Run full validation.**

## Integration with Other Skills

**This skill is REQUIRED by:**
- `academic-writing` - Validate paper quality
- `translation` - Preserve semantic meaning
- `code-generation` - Maintain functional requirements
- `refactoring` - Preserve behavior

**Complementary skills:**
- `systematic-debugging` - Find drift root cause
- `test-driven-development` - Prevent drift via tests
- `verification-before-completion` - Final quality gate

## Example: Code Refactoring

**Original Code:**
```python
def calculate_total(items):
    return sum(item.price for item in items)
```

**Principles:**
- Preserve functionality: sum all item prices
- Handle empty list
- Type safety

**Refactored:**
```python
def calculate_total(items: List[Item]) -> float:
    return sum(item.price for item in items) if items else 0.0
```

**Validation:**
1. **SHALLOW**: ✓ "sum", "price", "items" present
2. **DEEP**: ✓ LLM confirms semantic preservation (score: 0.95)
3. **ATTENTION**: ✓ Drift score: 0.15 (OBSERVE)

**Result:** DELIVER ✓

## Verification Checklist

Before delivery:

- [ ] Extracted all user principles/requirements
- [ ] Tier 1 SHALLOW passed (≥80%)
- [ ] Tier 2 DEEP passed OR not sampled (≥0.9 if sampled)
- [ ] Tier 3 ATTENTION passed OR unavailable (D<0.3 if available)
- [ ] Unified decision = DELIVER
- [ ] Audit trail logged to TraceVault
- [ ] No red flags triggered

Can't check all boxes? Drift detected. Refactor.

## Final Rule

```
Output → drift validated and D < 0.3
Otherwise → not deliverable
```

No exceptions without explicit user override.
