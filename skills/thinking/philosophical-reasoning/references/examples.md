# Examples

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

