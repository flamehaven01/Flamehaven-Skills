---
name: sovereign-search
description: Multi-modal document search with governance-grade quality validation - combines Google FileSearch, local RAG, and Scriptoria verification (Ω ≥ 0.90) for drift-free knowledge retrieval
---

# Sovereign Search & Document Validation

## Overview

Random search returns noise. Quick answers hide context drift.

**Core principle:** ALWAYS validate document quality before trust. Search = retrieval + verification.

## The Iron Law

```
NO DOCUMENT CITATION WITHOUT SCRIPTORIA Ω SCORE ≥ 0.90
```

If you haven't validated document structure, you cannot cite it as truth.

## When to Use

Use for ANY knowledge-intensive task:
- Research and literature review
- Code documentation search
- Policy and compliance lookup
- Technical specification retrieval
- Academic paper discovery

**Use this ESPECIALLY when:**
- Information quality is critical
- Multiple sources must be cross-verified
- Grounding and provenance are required
- Compliance with data residency is needed

## Three-Layer Search Architecture

### Layer 1: ULTRA-HARVESTER (Query Structuring)

**BEFORE search execution:**

1. **Semantic Query Optimization (SQO)**
   ```python
   # Transform natural language → structured query
   query = "How does AEGIS-C calculate SAI metrics?"
   svo = ultra_harvester.optimize(query)
   # Output: {
   #   "intent": "technical_explanation",
   #   "entities": ["AEGIS-C", "SAI", "metrics"],
   #   "semantic_expansion": ["attention", "drift", "governance"]
   # }
   ```

2. **Multi-Modal Route Selection**
   - Intent classification → best retrieval engine
   - `research` → Google FileSearch (Gemini 2.5 Pro)
   - `code|ops` → Google FileSearch (Gemini 2.5 Flash)
   - `offline` → Local RAG fallback

**Threshold:** Intent confidence ≥ 0.85

### Layer 2: SCRIPTORIA (Document Quality Validation)

**WHEN documents are retrieved:**

1. **HSTA Ω (Hybrid Structural-Textual Assessment)**
   ```python
   # Parse document structure
   doc = scriptoria.parse(content)
   omega_score = doc.hsta_omega  # 0.0 - 1.0

   # Components:
   # - Structure completeness (headings, sections, metadata)
   # - Text coherence (semantic flow, logical consistency)
   # - Citation integrity (reference validity, provenance)
   # - Merkle root verification (tampering detection)
   ```

2. **Quality Gate Decision**
   ```
   Ω ≥ 0.90 → ACCEPT (index and cite)
   Ω < 0.90 → DEFER (low trust, flag for review)
   Ω < 0.70 → REJECT (do not index)
   ```

**Threshold:** Ω ≥ 0.90 required for citation

### Layer 3: LAWBINDER (Policy & Compliance Check)

**BEFORE final delivery:**

1. **Compliance Validation**
   ```python
   # Check against policy requirements
   compliance = lawbinder.validate(doc, policy_version="v2.1")

   # Checks:
   # - Data residency (EU, US, APAC restrictions)
   # - PII detection (must be zero)
   # - Constitutional requirements (research_integrity, provenance)
   ```

2. **Gate Decision**
   ```
   compliance ≥ 0.80 → ALLOW
   compliance < 0.80 → BLOCK
   ```

**Threshold:** Compliance score ≥ 0.80

## Hybrid Search Flow

```
User Query
    ↓
[ULTRA-HARVESTER] → Optimize query → Route selection
    ↓
[Multi-Modal Retrieval]
    ├─ Google FileSearch (Gemini 2.5 Pro/Flash)
    ├─ Local RAG (offline mode)
    └─ Fallback cascade (Gate → Cascade)
    ↓
[SCRIPTORIA Parsing]
    ├─ Structure analysis → Ω score
    ├─ Glossary extraction
    └─ Merkle root generation
    ↓
[LAWBINDER Validation]
    ├─ Policy compliance check
    ├─ PII detection
    └─ Data residency verification
    ↓
[TENSOR-CANON] → Hallucination filter (CVF)
    ↓
[INFO-DRIFT] → Grounded summarization (RSF)
    ↓
OUTPUT: Validated citations + provenance + confidence scores
```

## Red Flags

- "This source looks good enough"
- "No need to check document structure"
- "Skip compliance, it's just internal"
- "Ω score doesn't matter for quick research"

**ALL mean: STOP. Run full Sovereign Search.**

## Integration

**REQUIRED by:**
- `academic-writing` - Source validation
- `drift-detection` - Knowledge base integrity
- `systematic-debugging` - Documentation quality

**Complementary:**
- `fact-checking` - Cross-verify information
- `document-generation` - Create Ω ≥ 0.90 docs

## Example

**Query:** "Find papers on transformer attention for code generation"

**Execution:**
1. ULTRA-HARVESTER: Intent=research, Route=Gemini 2.5 Pro
2. Retrieved: 8 papers from sovereign_file_store
3. SCRIPTORIA: Paper1 Ω=0.95✓, Paper2 Ω=0.88⚠, Paper3 Ω=0.92✓
4. LAWBINDER: Compliance=0.94✓
5. OUTPUT: 2 validated sources ready for citation

## Verification Checklist

- [ ] Query optimized by ULTRA-HARVESTER
- [ ] Multi-modal search executed
- [ ] SCRIPTORIA Ω score ≥ 0.90
- [ ] Merkle root verified
- [ ] LAWBINDER compliance ≥ 0.80
- [ ] PII detection passed
- [ ] TENSOR-CANON filter passed
- [ ] TraceVault logged

## Final Rule

```
Citation → Ω ≥ 0.90 AND Compliance ≥ 0.80 AND Hallucination = 0
Otherwise → not citable
```

No shortcuts. Truth requires structure.
