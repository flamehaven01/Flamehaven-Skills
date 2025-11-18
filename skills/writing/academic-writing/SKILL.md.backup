---
name: academic-writing
description: Full Meta-Scholar pipeline for academic content - from AI generation to journal submission with drift control, plagiarism detection, and automated review
---

# Academic Writing with AI

## Overview

Manual academic writing is slow. AI without governance produces plagiarized or drifted content.

**Core principle:** ALWAYS use full Meta-Scholar pipeline for academic content. Quality gates prevent drift.

## The Iron Law

```
NO ACADEMIC PAPER WITHOUT AUTOMATED VALIDATION PIPELINE
```

## Pipeline Stages

### Stage 1: AI Generation

**Before writing:**

1. **Define Research Parameters**
   ```python
   paper = {
       'topic': 'Quantum Neural Networks',
       'principles': [
           'Original research',
           'Peer-reviewed sources only',
           'No fabricated data',
           'Proper citations'
       ],
       'length': 6000,  # words
       'style': 'IEEE',
       'target_journal': 'Nature Machine Intelligence'
   }
   ```

2. **Generate Draft**
   - Use AI generation with principles injection
   - Structured output (abstract, intro, methods, results, discussion)
   - Auto-citation from verified sources

3. **Validate Generation**
   - **REQUIRED SUB-SKILL:** Use `drift-detection` for semantic preservation
   - Ensure principles maintained

### Stage 2: Drift Control

**MANDATORY after generation:**

1. **Shallow Check**
   ```python
   # All principles must be present
   for principle in paper['principles']:
       assert principle in draft_content
   ```

2. **Deep LLM Evaluation**
   ```
   "Does this paper adhere to academic standards?
   Principles: {principles}
   Content: {draft}
   Score violations 0-10 where 0=perfect."
   ```

   **Threshold:** Violations ≤ 2

3. **Attention SAI Validation**
   ```
   drift_score = unified_drift_detector.detect(
       original=paper['principles'],
       output=draft,
       attention=generation_attention
   )

   if drift_score >= 0.3:
       REFACTOR()
   ```

### Stage 3: Automated Review

**BEFORE plagiarism check:**

1. **Reviewer Agent**
   ```python
   review_result = reviewer_agent.evaluate(draft)

   checks = [
       'methodology_sound',
       'results_reproducible',
       'citations_valid',
       'no_forbidden_content',
       'ethical_compliance'
   ]

   for check in checks:
       if not review_result[check]:
           REJECT(reason=review_result['violations'])
   ```

2. **Address Violations**
   - Regenerate sections with violations
   - Re-run drift detection
   - Iterate until all checks pass

### Stage 4: Plagiarism Detection

**MANDATORY before submission:**

1. **Semantic Hash**
   ```python
   paper_hash = sha256(draft.encode()).hexdigest()

   # Check against known papers
   if paper_hash in plagiarism_db:
       REJECT('Exact match detected')
   ```

2. **Similarity Analysis**
   ```python
   for existing_paper in corpus:
       similarity = cosine_similarity(
           embed(draft),
           embed(existing_paper)
       )

       if similarity > 0.85:
           FLAG_HIGH_SIMILARITY(existing_paper)
   ```

3. **Citation Verification**
   - All citations must exist in verified sources
   - No fabricated references
   - Proper attribution

**Threshold:** Similarity < 85%, all citations verified

### Stage 5: Translation (Optional)

**If multi-language required:**

1. **Translate with Drift Preservation**
   ```python
   for target_lang in ['es', 'fr', 'de', 'ja']:
       translated = translate(draft, target_lang)

       # CRITICAL: Validate semantic preservation
       drift = drift_detector.detect(
           original=draft,
           output=back_translate(translated, 'en')
       )

       if drift['drift_score'] >= 0.4:
           REFINE_TRANSLATION()
   ```

2. **Multi-Language Quality**
   - Each translation validated independently
   - Technical terms preserved
   - Cultural adaptation where appropriate

### Stage 6: Journal Auto-Submission

**FINAL stage:**

1. **Format Conversion**
   ```python
   # Convert to journal-specific format
   formatted_paper = format_for_journal(
       draft,
       journal=paper['target_journal'],
       style=paper['style']
   )
   ```

2. **Compliance Check**
   - **REQUIRED SUB-SKILL:** Use `compliance/irb-validation`
   - **REQUIRED SUB-SKILL:** Use `compliance/regulatory-sync`

   ```python
   irb_check = validate_irb_compliance(draft)
   reg_check = validate_regulatory_compliance(draft, jurisdiction='US')

   if not (irb_check and reg_check):
       BLOCK_SUBMISSION()
   ```

3. **Automated Submission**
   ```python
   submission_result = submit_to_journal(
       paper=formatted_paper,
       journal=paper['target_journal'],
       authors=paper['authors'],
       cover_letter=generate_cover_letter()
   )
   ```

4. **Audit Trail**
   ```python
   trace_vault.log({
       'event': 'paper_submission',
       'paper_hash': paper_hash,
       'journal': paper['target_journal'],
       'timestamp': utcnow(),
       'validation_results': {
           'drift': drift_score,
           'plagiarism': similarity_score,
           'review': review_result,
           'compliance': {'irb': irb_check, 'reg': reg_check}
       }
   })
   ```

## Quality Gates

| Stage | Gate | Threshold | Action if Failed |
|-------|------|-----------|------------------|
| Generation | Drift | D < 0.3 | Regenerate |
| Drift Control | LLM Score | ≥ 0.9 | Refactor |
| Review | All Checks | 100% pass | Address violations |
| Plagiarism | Similarity | < 85% | Rewrite sections |
| Translation | Back-translation drift | < 0.4 | Refine translation |
| Compliance | IRB + Regulatory | 100% pass | Block submission |

**NO stage can be skipped. Gates are sequential.**

## Red Flags - STOP and Follow Process

- "Skip plagiarism check, it's original"
- "Manual submission faster than automation"
- "IRB not needed for this type of research"
- "Translation doesn't need validation"
- "One reviewer agent check is enough"
- "Drift detection slowing me down"

**ALL mean: STOP. Run full pipeline.**

## Integration with Other Skills

**This skill REQUIRES:**
- `drift-detection` - Every stage validation
- `plagiarism-check` - Stage 4
- `compliance/irb-validation` - Stage 6
- `compliance/regulatory-sync` - Stage 6

**Complementary skills:**
- `research/discovery` - Literature review before generation
- `research/quantum-review` - QUPRN peer-review simulation

## Example: Full Pipeline

**Input:**
```python
request = {
    'topic': 'Novel Transformer Architecture for Code Generation',
    'length': 8000,
    'target': 'ACL 2024'
}
```

**Execution:**
```
1. Generate draft (4min)
   ├─ Drift: 0.12 ✓

2. Reviewer agent (30sec)
   ├─ Methodology: ✓
   ├─ Results: ✓
   ├─ Ethics: ✓

3. Plagiarism (2min)
   ├─ Similarity: 23% ✓
   ├─ Citations: 47/47 verified ✓

4. Translation to 4 languages (3min)
   ├─ Each translation drift < 0.35 ✓

5. Compliance (1min)
   ├─ IRB: N/A (no human subjects) ✓
   ├─ Regulatory: Compliant ✓

6. Submit to ACL (automated)
   ├─ Formatted ✓
   ├─ Submitted ✓
   ├─ Confirmation: ACL-2024-0892 ✓

Total: 11min
TraceVault ID: 0x7f3a...
```

## Verification Checklist

Before claiming paper complete:

- [ ] AI generation with principles injection
- [ ] Drift score < 0.3 at every stage
- [ ] Reviewer agent all checks passed
- [ ] Plagiarism similarity < 85%
- [ ] All citations verified
- [ ] Translations validated (if applicable)
- [ ] IRB compliance confirmed
- [ ] Regulatory compliance confirmed
- [ ] Journal-specific formatting applied
- [ ] Submission successful
- [ ] Audit trail in TraceVault
- [ ] No quality gates failed

Can't check all? Pipeline incomplete. Continue.

## Final Rule

```
Academic paper → full pipeline with all gates passed
Otherwise → not submittable
```

No shortcuts. Quality over speed.
