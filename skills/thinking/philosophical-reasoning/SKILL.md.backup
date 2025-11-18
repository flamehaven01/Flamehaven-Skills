---
name: philosophical-reasoning
description: IRF-Calc v0.0.2 integrated philosophical reasoning - combines Methodic doubt (M), Abduction (A), Deduction (D), Induction (I), Falsification (F), and Paradigm alignment (P) with quantitative scoring and drift control
---

# Philosophical Reasoning (IRF-Calc v0.0.2)

## Overview

Surface reasoning creates shallow insights. Ad-hoc thinking misses paradigm shifts.

**Core principle:** ALWAYS engage six philosophical dimensions before conclusion. Depth = IRF score.

## The Iron Law

```
NO PHILOSOPHICAL CONCLUSION WITHOUT IRF SCORE ≥ 0.78
All six components (M,A,D,I,F,P) ≥ 0.70 REQUIRED
```

## When to Use

Use for ANY complex reasoning task:
- Strategic decision-making
- Research hypothesis formation
- Paradigm-shifting problems
- Multi-perspective analysis
- Root cause investigation
- Philosophical inquiry
- Complex system understanding

**Use this ESPECIALLY when:**
- Problem requires deep insight
- Multiple paradigms compete
- Assumptions are hidden
- Evidence is ambiguous
- Conventional wisdom fails
- Stakes are high

## Six-Component Framework (M-A-D-I-F-P)

### Component 1: M (Methodic Doubt) - Premise Purification

**BEFORE any reasoning:**

1. **Extract All Premises**
   ```python
   def extract_premises(question, context):
       premises = {
           'explicit': [],    # Stated directly
           'implicit': [],    # Hidden assumptions
           'suspect': []      # Potentially flawed
       }

       # Explicit premises from question/context
       for statement in parse_statements(question, context):
           if is_premise(statement):
               premises['explicit'].append({
                   'text': statement,
                   'source': 'explicit'
               })

       # Implicit premises (cultural, domain-specific, logical)
       implicit = detect_implicit_premises(question, context)
       premises['implicit'].extend(implicit)

       # Flag suspect premises
       for premise in premises['explicit'] + premises['implicit']:
           suspicion = assess_premise_quality(premise)
           if suspicion['is_suspect']:
               premises['suspect'].append({
                   'premise': premise,
                   'reason': suspicion['reason'],
                   'severity': suspicion['severity']
               })

       return premises
   ```

2. **Calculate M Score**
   ```python
   def calculate_M_score(premises):
       # Quality factors
       completeness = len(premises['explicit'] + premises['implicit']) / expected_count
       clarity = assess_premise_clarity(premises)
       suspect_ratio = len(premises['suspect']) / total_premises

       M = (
           0.4 * completeness +
           0.4 * clarity +
           0.2 * (1 - suspect_ratio)  # Fewer suspects = higher score
       )

       return clip(M, 0.0, 1.0)
   ```

**Threshold:** M ≥ 0.70

### Component 2: A (Abduction) - Hypothesis Generation

**WHEN premises identified:**

1. **Generate Multiple Hypotheses**
   ```python
   def generate_hypotheses(observations, premises):
       hypotheses = []

       # Use different abductive strategies
       strategies = [
           'best_explanation',      # Occam's razor
           'anomaly_driven',        # Focus on outliers
           'analogy_based',         # Cross-domain patterns
           'paradigm_shift'         # Revolutionary thinking
       ]

       for strategy in strategies:
           h = apply_abductive_strategy(
               observations=observations,
               premises=premises,
               strategy=strategy
           )

           hypotheses.append({
               'hypothesis': h,
               'strategy': strategy,
               'plausibility': assess_plausibility(h, observations),
               'novelty': assess_novelty(h),
               'explanatory_power': assess_explanatory_power(h)
           })

       return hypotheses
   ```

2. **Calculate A Score**
   ```python
   def calculate_A_score(hypotheses):
       if not hypotheses:
           return 0.0

       # Quality metrics
       avg_plausibility = mean([h['plausibility'] for h in hypotheses])
       diversity = calculate_hypothesis_diversity(hypotheses)
       explanatory_power = max([h['explanatory_power'] for h in hypotheses])

       A = (
           0.35 * avg_plausibility +
           0.30 * diversity +
           0.35 * explanatory_power
       )

       return clip(A, 0.0, 1.0)
   ```

**Threshold:** A ≥ 0.70

### Component 3: D (Deduction) - Logical Consequence Derivation

**FOR each hypothesis:**

1. **Derive Logical Consequences**
   ```python
   def derive_consequences(hypothesis, premises):
       trace = {
           'hypothesis': hypothesis,
           'steps': [],
           'conclusions': []
       }

       # Forward chaining from premises + hypothesis
       current_knowledge = premises.copy()
       current_knowledge.append(hypothesis)

       iteration = 0
       while iteration < max_iterations:
           # Apply logical rules
           new_facts = apply_logical_rules(current_knowledge)

           if not new_facts:
               break  # No more deductions

           trace['steps'].append({
               'iteration': iteration,
               'rule_applied': new_facts['rule'],
               'derived': new_facts['fact']
           })

           current_knowledge.extend(new_facts)
           iteration += 1

       trace['conclusions'] = extract_conclusions(current_knowledge)

       return trace
   ```

2. **Calculate D Score**
   ```python
   def calculate_D_score(deduction_trace):
       # Quality factors
       logical_validity = verify_logical_validity(deduction_trace)
       step_clarity = assess_step_clarity(deduction_trace['steps'])
       conclusion_strength = assess_conclusion_strength(deduction_trace)

       D = (
           0.4 * logical_validity +
           0.3 * step_clarity +
           0.3 * conclusion_strength
       )

       return clip(D, 0.0, 1.0)
   ```

**Threshold:** D ≥ 0.70

### Component 4: I (Induction) - Empirical Consistency

**WHEN deductions complete:**

1. **Check Empirical Fit**
   ```python
   def check_inductive_fit(hypothesis, deduction, observations):
       fit_metrics = {
           'coverage': 0.0,           # How many observations explained
           'accuracy': 0.0,           # Prediction accuracy
           'consistency': 0.0,        # No contradictions
           'counterexamples': []
       }

       # Coverage: observations explained by hypothesis
       explained = [obs for obs in observations
                    if hypothesis_explains(hypothesis, obs)]
       fit_metrics['coverage'] = len(explained) / len(observations)

       # Accuracy: predictions match reality
       predictions = make_predictions(hypothesis, deduction)
       matches = [p for p in predictions
                  if observation_supports(observations, p)]
       fit_metrics['accuracy'] = len(matches) / len(predictions)

       # Consistency: no contradictions
       contradictions = find_contradictions(
           hypothesis, deduction, observations
       )
       fit_metrics['consistency'] = 1.0 - (len(contradictions) / len(observations))

       # Counterexamples
       fit_metrics['counterexamples'] = find_counterexamples(
           hypothesis, observations
       )

       return fit_metrics
   ```

2. **Calculate I Score**
   ```python
   def calculate_I_score(fit_metrics):
       I = (
           0.35 * fit_metrics['coverage'] +
           0.35 * fit_metrics['accuracy'] +
           0.30 * fit_metrics['consistency']
       )

       # Penalty for counterexamples
       counterexample_penalty = min(0.2, len(fit_metrics['counterexamples']) * 0.05)
       I = max(0.0, I - counterexample_penalty)

       return clip(I, 0.0, 1.0)
   ```

**Threshold:** I ≥ 0.70

### Component 5: F (Falsification) - Killer Counterexample Search

**CRITICAL validation step:**

1. **Active Falsification Attempt**
   ```python
   def attempt_falsification(hypothesis, evidence):
       falsification_result = {
           'verdict': None,           # 'rejected', 'weakened', 'inconclusive'
           'counterexamples': [],
           'test_cases': [],
           'revised_hypothesis': None
       }

       # Generate adversarial test cases
       test_cases = generate_falsification_tests(hypothesis)

       for test in test_cases:
           result = execute_test(test, hypothesis, evidence)

           if result['falsifies']:
               falsification_result['counterexamples'].append({
                   'test': test,
                   'why_falsifies': result['reason']
               })

       # Determine verdict
       if len(falsification_result['counterexamples']) > 0:
           severity = assess_counterexample_severity(
               falsification_result['counterexamples']
           )

           if severity > 0.8:
               falsification_result['verdict'] = 'rejected'
           elif severity > 0.5:
               falsification_result['verdict'] = 'weakened'
               # Propose revision
               falsification_result['revised_hypothesis'] = revise_hypothesis(
                   hypothesis,
                   falsification_result['counterexamples']
               )
           else:
               falsification_result['verdict'] = 'inconclusive'
       else:
           falsification_result['verdict'] = 'inconclusive'

       return falsification_result
   ```

2. **Calculate F Score**
   ```python
   def calculate_F_score(falsification_result):
       # F measures rigor of falsification attempt
       test_coverage = len(falsification_result['test_cases']) / expected_tests
       counterexample_detection = 1.0 if falsification_result['counterexamples'] else 0.0

       # High F score = rigorous falsification attempt
       # NOT "hypothesis survived" (that's in verdict)
       F = (
           0.5 * test_coverage +
           0.3 * assess_test_quality(falsification_result['test_cases']) +
           0.2 * (1.0 if falsification_result['revised_hypothesis'] else 0.5)
       )

       return clip(F, 0.0, 1.0)
   ```

**Threshold:** F ≥ 0.70

### Component 6: P (Paradigm) - Paradigm Alignment

**META-level analysis:**

1. **Paradigm Consistency Check**
   ```python
   def check_paradigm_alignment(hypothesis, current_paradigm):
       alignment = {
           'paradigm': current_paradigm,
           'consistency': 0.0,
           'shift_type': None,        # 'normal', 'anomaly', 'revolution'
           'implications': []
       }

       # Measure alignment with current paradigm
       paradigm_principles = extract_paradigm_principles(current_paradigm)

       violations = []
       for principle in paradigm_principles:
           if hypothesis_violates(hypothesis, principle):
               violations.append({
                   'principle': principle,
                   'severity': assess_violation_severity(hypothesis, principle)
               })

       alignment['consistency'] = 1.0 - (len(violations) / len(paradigm_principles))

       # Determine shift type
       if len(violations) == 0:
           alignment['shift_type'] = 'normal'  # Normal science
       elif 1 <= len(violations) <= 2:
           alignment['shift_type'] = 'anomaly'  # Anomaly (Kuhn)
       else:
           alignment['shift_type'] = 'revolution'  # Paradigm shift

       # Analyze implications
       if alignment['shift_type'] in ['anomaly', 'revolution']:
           alignment['implications'] = analyze_paradigm_shift_implications(
               hypothesis, current_paradigm, violations
           )

       return alignment
   ```

2. **Calculate P Score**
   ```python
   def calculate_P_score(alignment):
       # P measures paradigm awareness quality
       consistency_awareness = alignment['consistency']
       shift_recognition = 1.0 if alignment['shift_type'] else 0.5
       implication_depth = assess_implication_depth(alignment['implications'])

       P = (
           0.4 * consistency_awareness +
           0.3 * shift_recognition +
           0.3 * implication_depth
       )

       return clip(P, 0.0, 1.0)
   ```

**Threshold:** P ≥ 0.70

## Integrated IRF Scoring

```python
def calculate_IRF_score(M, A, D, I, F, P):
    """
    Global IRF score using geometric mean with epsilon smoothing

    Formula:
    s_i = (Π_k (epsilon + q_{i,k}))^(1/6)

    where:
    - epsilon = 0.001 (prevents zero product)
    - q = [M, A, D, I, F, P]
    - k = component index
    """
    epsilon = 0.001
    components = [M, A, D, I, F, P]

    # Geometric mean
    product = 1.0
    for q in components:
        product *= (epsilon + q)

    s = product ** (1/6)

    # Integer scores (for reporting)
    R_components = {
        'M': round(10 * M),
        'A': round(10 * A),
        'D': round(10 * D),
        'I': round(10 * I),
        'F': round(10 * F),
        'P': round(10 * P)
    }
    R_global = round(100 * s)

    return {
        'continuous': {
            'M': M, 'A': A, 'D': D, 'I': I, 'F': F, 'P': P,
            'global': s
        },
        'integer': {
            'components': R_components,
            'global': R_global
        },
        'passed': s >= 0.78 and all(q >= 0.70 for q in components)
    }
```

## Drift Control (IRF-DriftLock)

```python
def check_IRF_drift(scores_t1, scores_t2):
    """
    Two-metric drift detection:
    1. JSD (Jensen-Shannon Divergence) on score distributions
    2. L2 on component mean vectors
    """

    # JSD drift (distribution-based)
    p_t1 = normalize_distribution(scores_t1)  # s_i / Σs_i
    p_t2 = normalize_distribution(scores_t2)

    jsd = jensen_shannon_divergence(p_t1, p_t2) / log(2)  # Normalized [0,1]

    # L2 drift (component vector)
    q_bar_t1 = mean([M, A, D, I, F, P], axis=0)  # At t1
    q_bar_t2 = mean([M, A, D, I, F, P], axis=0)  # At t2

    l2_drift = euclidean_distance(q_bar_t1, q_bar_t2)

    drift_result = {
        'jsd': jsd,
        'l2': l2_drift,
        'jsd_passed': jsd <= 0.06,
        'l2_passed': l2_drift <= 0.04,
        'overall_passed': jsd <= 0.06 and l2_drift <= 0.04
    }

    return drift_result
```

## DR3 Decision Protocol

After IRF scoring, apply DR3 (Deductive-Realism-Rationality) decision fusion:

```python
def DR3_decision_protocol(candidates, IRF_scores):
    """
    3-axis decision scoring with conservative selection

    Axes:
    - Realism (based on I, F)
    - Stability (based on D, M)
    - Conservative Rationality (based on A, P)
    """

    scored_candidates = []

    for candidate in candidates:
        # Axis scores
        realism = (
            0.6 * IRF_scores[candidate]['I'] +
            0.4 * IRF_scores[candidate]['F']
        )

        stability = (
            0.6 * IRF_scores[candidate]['D'] +
            0.4 * IRF_scores[candidate]['M']
        )

        conservative_rationality = (
            0.5 * IRF_scores[candidate]['A'] +
            0.5 * IRF_scores[candidate]['P']
        )

        # Weighted final score
        final_score = (
            0.4 * realism +
            0.4 * stability +
            0.2 * conservative_rationality
        )

        scored_candidates.append({
            'candidate': candidate,
            'realism': realism,
            'stability': stability,
            'conservative_rationality': conservative_rationality,
            'final_score': final_score,
            'passes_threshold': all([
                realism >= 0.6,
                stability >= 0.6,
                conservative_rationality >= 0.6
            ])
        })

    # Select best candidate that passes all thresholds
    valid_candidates = [c for c in scored_candidates if c['passes_threshold']]

    if valid_candidates:
        return max(valid_candidates, key=lambda x: x['final_score'])
    else:
        return {
            'decision': 'ABSTAIN',
            'reason': 'No candidate meets minimum axis thresholds (≥0.6)',
            'recommendation': 'REQUEST_MORE_EVIDENCE'
        }
```

## Integrated Flow

```
Problem Input
    ↓
[M: Premise Purification]
    ├─ Extract explicit premises
    ├─ Identify implicit assumptions
    └─ Flag suspect premises (M ≥ 0.70)
    ↓
[A: Hypothesis Generation]
    ├─ Generate 3-5 hypotheses (abductive strategies)
    ├─ Assess plausibility
    └─ Calculate diversity (A ≥ 0.70)
    ↓
[D: Deduction]
    ├─ Derive logical consequences
    ├─ Forward chaining
    └─ Validate step clarity (D ≥ 0.70)
    ↓
[I: Induction]
    ├─ Check empirical fit
    ├─ Calculate coverage + accuracy
    └─ Find counterexamples (I ≥ 0.70)
    ↓
[F: Falsification]
    ├─ Generate adversarial tests
    ├─ Search killer counterexamples
    └─ Verdict (rejected/weakened/inconclusive) (F ≥ 0.70)
    ↓
[P: Paradigm Alignment]
    ├─ Check paradigm consistency
    ├─ Identify shift type (normal/anomaly/revolution)
    └─ Analyze implications (P ≥ 0.70)
    ↓
[IRF Score Calculation]
    ├─ Global: s = (Π(ε + q_k))^(1/6)
    ├─ Integer: R ∈ {0..100}
    └─ Gate: s ≥ 0.78 AND all q_k ≥ 0.70
    ↓
[Drift Check]
    ├─ JSD ≤ 0.06
    └─ L2 ≤ 0.04
    ↓
[DR3 Decision Protocol]
    ├─ Realism (I, F) ≥ 0.6
    ├─ Stability (D, M) ≥ 0.6
    ├─ Conservative Rationality (A, P) ≥ 0.6
    └─ Select argmax OR ABSTAIN
    ↓
OUTPUT: Validated philosophical reasoning + IRF report + decision
```

## Red Flags

- "Skip premise analysis"
- "One hypothesis is enough"
- "Deduction is unnecessary"
- "Don't need empirical check"
- "Falsification is too harsh"
- "Paradigm doesn't matter"
- "IRF score < 0.78 is acceptable"

**ALL mean: STOP. Run full IRF-Calc.**

## Integration

**REQUIRED by:**
- `strategic-consulting` - Deep strategy analysis
- `research-design` - Hypothesis formation
- `root-cause-analysis` - Complex problem diagnosis

**Complementary:**
- `drift-detection` - Semantic preservation
- `fact-checking` - Empirical validation
- `principle-validation` - Policy compliance

## Example: Strategic Decision

**Problem:** "Should we pivot our SaaS to AI-native architecture?"

**Execution:**

1. **M (Premises):**
   ```python
   premises = {
       'explicit': [
           'Current architecture is cloud-based microservices',
           'AI workloads require GPU infrastructure',
           'Customer demand for AI features growing'
       ],
       'implicit': [
           'AI-native = competitive advantage',
           'Pivot cost is recoverable',
           'Team can execute AI transformation'
       ],
       'suspect': [
           {
               'premise': 'AI-native = competitive advantage',
               'reason': 'Assumes AI differentiation, not commodity',
               'severity': 'high'
           }
       ]
   }
   M_score = 0.75 ✓
   ```

2. **A (Hypotheses):**
   ```python
   hypotheses = [
       {
           'h': 'Full AI-native rewrite',
           'strategy': 'revolutionary',
           'plausibility': 0.6,
           'explanatory_power': 0.85
       },
       {
           'h': 'Incremental AI layer on existing',
           'strategy': 'best_explanation',
           'plausibility': 0.85,
           'explanatory_power': 0.70
       },
       {
           'h': 'Partner with AI platform vendor',
           'strategy': 'analogy_based',
           'plausibility': 0.75,
           'explanatory_power': 0.65
       }
   ]
   A_score = 0.78 ✓
   ```

3. **D (Deduction):**
   ```python
   # For "Incremental AI layer"
   deduction_trace = {
       'steps': [
           'Incremental → lower upfront cost',
           'Lower cost → faster ROI',
           'Existing customers → no migration disruption',
           'AI layer → modular, testable independently'
       ],
       'conclusions': [
           'Risk is lower than full rewrite',
           'Value delivery is faster',
           'Optionality preserved (can pivot later)'
       ]
   }
   D_score = 0.82 ✓
   ```

4. **I (Induction):**
   ```python
   fit = {
       'coverage': 0.80,  # Explains 80% of customer requests
       'accuracy': 0.75,  # Predictions align with pilot results
       'consistency': 0.85,  # No internal contradictions
       'counterexamples': [
           'One customer requires full AI-native (outlier)'
       ]
   }
   I_score = 0.77 ✓
   ```

5. **F (Falsification):**
   ```python
   falsification = {
       'test_cases': [
           'Can AI layer handle 10x traffic?',
           'Does incremental delay competitive response?',
           'Will tech debt accumulate?'
       ],
       'counterexamples': [
           'Tech debt may accumulate if not planned'
       ],
       'verdict': 'weakened',
       'revised_hypothesis': 'Incremental AI layer + 2-year roadmap to full AI-native'
   }
   F_score = 0.73 ✓
   ```

6. **P (Paradigm):**
   ```python
   paradigm_alignment = {
       'current_paradigm': 'Cloud-first SaaS',
       'consistency': 0.70,
       'shift_type': 'anomaly',  # AI requires rethinking, but not full revolution
       'implications': [
           'Infrastructure costs will rise (GPU)',
           'Hiring needs shift (ML engineers)',
           'Customer expectations change (AI = baseline)'
       ]
   }
   P_score = 0.76 ✓
   ```

7. **IRF Score:**
   ```python
   IRF = calculate_IRF_score(
       M=0.75, A=0.78, D=0.82,
       I=0.77, F=0.73, P=0.76
   )
   # Global: 0.767 → R_global = 77
   # FAILED: 0.767 < 0.78 threshold

   # Action: Improve weakest component (F = 0.73)
   # → More rigorous falsification tests
   # → Revised hypothesis stronger

   # After revision:
   F_score = 0.78
   IRF_global = 0.79 ✓
   ```

8. **DR3 Decision:**
   ```python
   decision = DR3_decision_protocol(
       candidates=[
           'Full AI-native rewrite',
           'Incremental AI layer + roadmap',
           'Partner with vendor'
       ],
       IRF_scores={...}
   )

   # Result:
   {
       'selected': 'Incremental AI layer + 2-year roadmap',
       'realism': 0.78,
       'stability': 0.81,
       'conservative_rationality': 0.74,
       'final_score': 0.79
   } ✓
   ```

**Output:**
- Decision: Incremental AI layer with 2-year full AI-native roadmap
- IRF Score: 0.79 (passed)
- Drift: JSD=0.03, L2=0.02 (passed)
- Confidence: High (all axes ≥0.6)

## Verification Checklist

- [ ] M: Premises extracted (explicit + implicit)
- [ ] M: Suspect premises flagged
- [ ] M: M_score ≥ 0.70
- [ ] A: 3-5 hypotheses generated
- [ ] A: Multiple abductive strategies used
- [ ] A: A_score ≥ 0.70
- [ ] D: Logical consequences derived
- [ ] D: Deduction trace validated
- [ ] D: D_score ≥ 0.70
- [ ] I: Empirical fit calculated
- [ ] I: Counterexamples identified
- [ ] I: I_score ≥ 0.70
- [ ] F: Falsification tests executed
- [ ] F: Verdict determined (rejected/weakened/inconclusive)
- [ ] F: F_score ≥ 0.70
- [ ] P: Paradigm alignment assessed
- [ ] P: Shift type identified
- [ ] P: P_score ≥ 0.70
- [ ] IRF: Global score ≥ 0.78
- [ ] IRF: All component scores ≥ 0.70
- [ ] Drift: JSD ≤ 0.06, L2 ≤ 0.04
- [ ] DR3: All axes ≥ 0.6 OR abstained
- [ ] TraceVault logged

## Final Rule

```
Philosophical Conclusion → IRF ≥ 0.78 AND all(M,A,D,I,F,P ≥ 0.70) AND drift_ok AND DR3_passed
Otherwise → refine or abstain
```

Shallow reasoning misleads. Philosophical rigor reveals truth.
