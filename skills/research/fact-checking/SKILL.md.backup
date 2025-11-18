---
name: fact-checking
description: Multi-tier truth verification using ALECTA framework - combines FTRI (Fact Trust Index), RWTI (Reality-Weighted Trust Index), and fake news detection for comprehensive information validation
---

# Fact-Checking & Truth Verification

## Overview

Information without verification is noise. Speed without truth is misinformation.

**Core principle:** ALWAYS verify facts before propagation. Truth = structured evidence.

## The Iron Law

```
NO INFORMATION SHARING WITHOUT FACT VERIFICATION
FTRI ≥ 0.61 REQUIRED
```

## Three-Layer Verification

### Layer 1: FTRI (Fact Trust Reliability Index)

**Evaluate information structure:**

| Component | Question | Score (0-1) |
|-----------|----------|-------------|
| **Existence** | Did event actually occur? | e.g., 1.0 |
| **Accuracy** | Are numbers/details correct? | e.g., 0.87 |
| **Evidence** | Is claim backed by sources? | e.g., 0.78 |
| **Context** | Is framing fair/complete? | e.g., 0.55 |

**FTRI = Average of components**

**Interpretation:**
- 0.81-1.0: Very high trust
- 0.61-0.8: High trust
- 0.31-0.6: Low trust, verify further
- 0.0-0.3: Very low trust, likely false

### Layer 2: RWTI (Reality-Weighted Trust Index)

**Predict public perceived credibility:**

**Formula:**
```
RWTI = (0.5 × G) + (0.3 × E) + (0.2 × M)

Where:
G = Approval/support metrics (0-1)
E = Emotional response strength (0-1)
M = Media exposure frequency (0-1)
```

**Example:**
```
G (Support): 0.72
E (Emotion): 0.54
M (Exposure): 0.58
→ RWTI = 0.65 (Medium-High perceived trust)
```

### Layer 3: Fake News Detection

**Classification:**

| Type | Definition | Action |
|------|------------|--------|
| ✅ **Fact** | Sources verified, no distortion | Approve |
| ❌ **Fake** | Fabricated/manipulated | Block |
| 🔶 **Exaggeration** | Truth + emotional framing | Flag |
| 🔷 **Misuse** | Incomplete context | Warn |

**Detection criteria:**
- Title-content mismatch
- Emotional manipulation keywords
- Missing attribution
- Image/video manipulation
- Unverifiable anonymous sources

## Integrated Flow

```
Information Input
    ↓
[FTRI Analysis]
    ├─ Existence check
    ├─ Accuracy verification
    ├─ Evidence assessment
    └─ Context evaluation
    ↓
[RWTI Calculation]
    ├─ Support metrics
    ├─ Emotional response
    └─ Media exposure
    ↓
[Fake News Filter]
    ├─ Pattern detection
    ├─ Source verification
    └─ Manipulation check
    ↓
OUTPUT: Trust score + Classification + Evidence
```

## Red Flags

- "It sounds true"
- "Everyone's sharing it"
- "The source seems credible"
- "No time to verify"
- "It confirms what I believe"

**ALL mean: STOP. Run full verification.**

## Integration

**REQUIRED by:**
- `news-analysis` - Article validation
- `research-writing` - Source verification
- `public-communication` - Statement accuracy

**Complementary:**
- `sovereign-search` - Source quality check
- `sentiment-analysis` - Emotional manipulation detection

## Example: Political Statement

**Statement:** "Employment rate increased 15% this quarter"

**Verification:**
1. **FTRI Analysis:**
   - Existence: ✓ Statement was made (1.0)
   - Accuracy: ✗ Official data shows 3.2% (0.2)
   - Evidence: △ Cited "internal report" (0.4)
   - Context: ✗ Cherry-picked timeframe (0.3)
   - **FTRI = 0.48** (Low trust)

2. **RWTI Calculation:**
   - G: 0.65 (moderate support)
   - E: 0.72 (strong emotional response)
   - M: 0.85 (high media coverage)
   - **RWTI = 0.72** (High perceived trust despite low factual trust)

3. **Classification:** 🔶 Exaggeration (factual basis but misleading)

**Conclusion:** FLAG with correction

## Verification Checklist

- [ ] FTRI calculated (all 4 components)
- [ ] FTRI ≥ 0.61 or flagged
- [ ] RWTI calculated (emotional/social context)
- [ ] Fake news classification determined
- [ ] Sources cross-verified
- [ ] Context checked for cherry-picking
- [ ] Emotional manipulation assessed
- [ ] TraceVault logged

## Final Rule

```
Information → FTRI ≥ 0.61 AND Classification ≠ Fake
Otherwise → block or flag with correction
```

Truth doesn't need speed. It needs structure.
