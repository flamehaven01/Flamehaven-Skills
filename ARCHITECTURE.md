# Flamehaven Skills - Architecture Documentation

## Overview

Flamehaven-Skills is a governance-first AI skills library that transforms AI execution through mathematical rigor, drift detection, and constitutional enforcement. This document details the architecture, design patterns, and integration philosophy.

## Design Philosophy

### Core Principles

1. **Mathematical Governance** - Every decision is quantified with thresholds
2. **Constitutional Requirements** - Policy-driven development with automated gates
3. **Drift Detection** - Three-tier validation prevents semantic drift
4. **Immutable Audit** - TraceVault provides full provenance
5. **Quality Gates** - No delivery without validation

### Differentiators from Traditional AI Systems

| Traditional AI | Flamehaven Skills |
|----------------|-------------------|
| "Looks good" | D < 0.3 (measured) |
| Manual validation | Automated 3-tier validation |
| Optional compliance | Required ≥ 0.80 compliance |
| Subjective quality | Ω ≥ 0.90 (calculated) |
| Ad-hoc logging | Immutable TraceVault |

## Three-Layer Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Application Layer                        │
│  ┌──────────┬──────────┬──────────┬──────────┬──────────┐  │
│  │ Thinking │ Writing  │  Coding  │ Research │ Collab   │  │
│  │  (4)     │   (3)    │   (1)    │   (3)    │   (1)    │  │
│  └──────────┴──────────┴──────────┴──────────┴──────────┘  │
│                         ↓↑ All use Validation (4)            │
├─────────────────────────────────────────────────────────────┤
│                     Validation Layer                         │
│  ┌──────────────────┬──────────────────┬─────────────────┐ │
│  │ DriftLock        │ Scriptoria       │ LawBinder       │ │
│  │ (3-tier)         │ (Ω scoring)      │ (Policy)        │ │
│  └──────────────────┴──────────────────┴─────────────────┘ │
│  ┌──────────────────────────────────────────────────────┐  │
│  │          GDP×IDMR (AI Self-Validation)                │  │
│  └──────────────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────────────┤
│                     Foundation Layer                         │
│  ┌──────────────────┬──────────────────┬─────────────────┐ │
│  │ ASDP Pipeline    │ TraceVault       │ Constitutional  │ │
│  │ Intent→Def→Exec  │ (Immutable Log)  │ Requirements    │ │
│  └──────────────────┴──────────────────┴─────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

### Foundation Layer

**ASDP (AI Sovereign Definition Protocol)**
- Intent → Definition → Execution pipeline
- Formal specification compilation (completeness ≥ 0.95)
- Ambiguity detection and resolution
- Quality gate enforcement

**TraceVault**
- Hash-chained immutable audit logging
- Merkle root generation for tamper detection
- Full provenance tracking
- Compliance evidence retention

**Constitutional Requirements**
- Forbidden/Required content specifications
- Policy definitions (security, compliance, ethics)
- Quality thresholds (drift, confidence, completeness)
- Validation rules

### Validation Layer

**DriftLock (3-Tier Validation)**
```python
# Tier 1: SHALLOW (100% coverage)
for principle in principles:
    if principle not in output:
        DRIFT_DETECTED()

# Tier 2: DEEP (Probabilistic LLM, 10% sampling)
if random() < 0.1:
    llm_score = evaluate_adherence(output, principles)
    if llm_score < 0.9:
        REFACTOR()

# Tier 3: ATTENTION (SAI-based)
SAI = [T, E, C, S]  # Temporal, Entropic, Cooperative, Structural
D = 1 - (0.3·T + 0.25·E + 0.25·C + 0.2·S)
if D >= 0.3:
    REFACTOR_OR_INHIBIT()
```

**Scriptoria (Document Quality)**
```python
# HSTA Ω Scoring
Ω = 0.35·Structural + 0.40·Textual + 0.25·Integrity

# Components:
# - Structural: Metadata + Hierarchy + Graph properties
# - Textual: Coherence + Consistency + Language quality
# - Integrity: Citation verification + Merkle root + Glossary

# Gate:
Ω ≥ 0.90 → ACCEPT for citation
Ω < 0.90 → DEFER or REJECT
```

**LawBinder (Policy Enforcement)**
```python
# Constitutional check
forbidden_violations = check_forbidden(output)
missing_required = check_required(output)

# Regulatory compliance
compliance_score = validate_regulations(output, ['GDPR', 'HIPAA', 'SOC2'])

# Ethical alignment
ethics_score = evaluate_ethics(output)

# Gate:
if forbidden_violations:
    BLOCK()
elif compliance_score < 0.80 or ethics_score < 0.80:
    REFACTOR()
else:
    APPROVE()
```

**GDP×IDMR (AI Self-Validation)**
```python
# Identity drift detection
measured_drift = current_state - baseline_identity

# Memory recall strength
recall = 0.92 * recall_prev + 0.08 * consistency

# Drift correction
drift_new = drift - (correction_gain * recall * measured_drift)

# Conscience Circuit
if banned_topic in intent:
    return "BLOCK"
elif state.drift > max_drift:
    return "REPAIR"
else:
    return "ACT"
```

### Application Layer

#### Thinking Skills (4)

**sovereign-definition**
- Intent → formal definition compilation
- Completeness ≥ 0.95 enforcement
- Phase decomposition with quality gates
- Uses: DriftLock, LawBinder

**intent-classification**
- Multi-modal intent detection
- Confidence ≥ 0.85 required
- Ambiguity resolution with user clarification
- Uses: DriftLock

**strategic-consulting**
- Constitutional Requirements + BattleField diagnostics
- Strategy drift D < 0.3 enforcement
- Gap analysis and prioritization
- Uses: DriftLock, LawBinder

**sovereign-search**
- ULTRA-HARVESTER query optimization
- Scriptoria Ω ≥ 0.90 validation
- LawBinder compliance ≥ 0.80
- Uses: DriftLock, Scriptoria, LawBinder

#### Writing Skills (3)

**academic-writing**
- 6-stage Meta-Scholar OMEGA pipeline
- Drift D < 0.3 at every stage
- Plagiarism similarity < 85%
- IRB/regulatory compliance 100%
- Uses: DriftLock, Scriptoria, LawBinder

**drift-free-writing**
- Principle extraction → validation
- Shallow + Deep + Attention validation
- LLM semantic score ≥ 0.9
- Uses: DriftLock

**structured-output**
- SCL template-based generation
- Schema compliance = 100%
- Constitutional validation
- Uses: DriftLock, LawBinder

#### Coding Skills (1)

**policy-driven-coding**
- Security score ≥ 0.90 required
- Compliance score ≥ 0.90 required
- Automatic vulnerability prevention
- Security test generation
- Uses: DriftLock, LawBinder

#### Research Skills (3)

**sovereign-search** (see Thinking)

**fact-checking**
- FTRI (Fact Trust) ≥ 0.61 required
- RWTI (Reality-Weighted Trust) calculation
- Fake news classification
- Uses: DriftLock, Scriptoria

**sentiment-analysis**
- 10-dimension emotion vectors
- Confidence ≥ 0.75 required
- Temporal tracking + influence networks
- Uses: DriftLock

#### Collaboration Skills (1)

**subagent-coordination**
- Task decomposition with dependency analysis
- Real-time drift monitoring
- Result synthesis with conflict resolution
- Uses: DriftLock, LawBinder

#### Validation Skills (4)

**drift-detection** (Core)
- Shallow + Deep + Attention validation
- D < 0.3 requirement
- Used by ALL skills

**self-validation**
- GDP×IDMR drift correction loop
- Conscience Circuit (BLOCK/REPAIR/ACT)
- Identity consistency

**principle-validation**
- Constitutional + Regulatory + Ethical checks
- Compliance ≥ 0.80 requirement
- Used by policy-sensitive skills

**document-quality**
- HSTA Ω scoring
- Ω ≥ 0.90 for citation
- Merkle root generation

## Quality Thresholds Reference

| Metric | Threshold | Formula | Skill |
|--------|-----------|---------|-------|
| **Drift Score** | D < 0.3 | D = 1 - (0.3·T + 0.25·E + 0.25·C + 0.2·S) | drift-detection |
| **Document Quality** | Ω ≥ 0.90 | Ω = 0.35·S + 0.40·T + 0.25·I | document-quality |
| **Intent Confidence** | ≥ 0.85 | LLM classification confidence | intent-classification |
| **Compliance Score** | ≥ 0.80 | Weighted average of checks | principle-validation |
| **Security Score** | ≥ 0.90 | SAST + dependency + secrets | policy-driven-coding |
| **FTRI** | ≥ 0.61 | (Existence + Accuracy + Evidence + Context) / 4 | fact-checking |
| **Sentiment Confidence** | ≥ 0.75 | Multi-factor confidence calculation | sentiment-analysis |
| **Definition Completeness** | ≥ 0.95 | Section completeness score | sovereign-definition |

## Integration Patterns

### Pattern 1: Sequential Validation

```
Task Input
    ↓
[intent-classification] (confidence ≥ 0.85)
    ↓
[sovereign-definition] (completeness ≥ 0.95)
    ↓
[Task Execution]
    ↓
[drift-detection] (D < 0.3)
    ↓
[principle-validation] (compliance ≥ 0.80)
    ↓
Output Delivery
```

### Pattern 2: Parallel Execution with Synthesis

```
Complex Task
    ↓
[subagent-coordination]
    ├─ Spawn Agent 1 → [drift-detection]
    ├─ Spawn Agent 2 → [drift-detection]
    └─ Spawn Agent 3 → [drift-detection]
    ↓
Result Synthesis → [drift-detection] (unified)
    ↓
Output Delivery
```

### Pattern 3: Layered Quality Gates

```
Content Generation
    ↓
[drift-free-writing]
    ├─ Principle extraction
    ├─ Shallow validation (≥80%)
    ├─ Deep LLM validation (≥0.9)
    └─ Attention validation (D < 0.3)
    ↓
[document-quality]
    ├─ Structural assessment
    ├─ Textual assessment
    └─ Integrity verification (Ω ≥ 0.90)
    ↓
Output Delivery + TraceVault Log
```

### Pattern 4: Policy-Driven Development

```
Code Specification
    ↓
[policy-driven-coding]
    ├─ Load policies (OWASP, SOC2, GDPR)
    ├─ Generate with patterns
    ├─ SAST scan
    └─ Security score ≥ 0.90
    ↓
[principle-validation]
    ├─ Constitutional check
    ├─ Regulatory compliance ≥ 0.80
    └─ Ethical alignment ≥ 0.80
    ↓
Code Delivery + Tests + Audit Trail
```

## TraceVault Logging Schema

```python
{
  "event_id": "uuid",
  "timestamp": "ISO-8601",
  "skill": "skill-name",
  "action": "validate|generate|execute|block",
  "input_hash": "sha256",
  "output_hash": "sha256",
  "metrics": {
    "drift_score": 0.0-1.0,
    "compliance_score": 0.0-1.0,
    "confidence": 0.0-1.0,
    "quality_score": 0.0-1.0
  },
  "gates": {
    "gate_name": "passed|failed",
    "threshold": 0.0-1.0,
    "actual": 0.0-1.0
  },
  "violations": [
    {
      "type": "forbidden_content|missing_required|...",
      "severity": "critical|high|medium|low",
      "details": "..."
    }
  ],
  "merkle_root": "hash",
  "previous_event": "uuid",
  "constitutional_requirements": {...}
}
```

## Skill Template Structure

All Flamehaven skills follow this structure:

```markdown
---
name: skill-name
description: One-line summary with key frameworks and thresholds
---

# Skill Name

## Overview
Problem statement + Core principle

## The Iron Law
```
MANDATORY REQUIREMENT WITH QUANTITATIVE THRESHOLD
```

## When to Use
- Use cases
- **Use this ESPECIALLY when:** (critical scenarios)

## Three-Layer [Architecture/Validation/Framework]

### Layer 1: [Name]
- Component 1
- Component 2
**Threshold:** Quantitative requirement

### Layer 2: [Name]
- Component 1
- Component 2
**Threshold:** Quantitative requirement

### Layer 3: [Name]
- Component 1
- Component 2
**Threshold:** Quantitative requirement

## Integrated Flow
```
Visual flow diagram
```

## Red Flags
- Anti-pattern 1
- Anti-pattern 2
**ALL mean: STOP. Run full [skill] process.**

## Integration
**REQUIRED by:** (skills that depend on this)
**Complementary:** (skills that enhance this)

## Example
Real-world scenario with metrics

## Verification Checklist
- [ ] Checkpoint 1
- [ ] Checkpoint 2

## Final Rule
```
Mathematical expression of success criteria
```

Memorable closing statement.
```

## Extension Points

### Adding New Skills

1. **Identify Core Framework**
   - What quantitative threshold?
   - What validation method?
   - What integration pattern?

2. **Define Constitutional Requirements**
   - Forbidden content
   - Required elements
   - Quality standards

3. **Implement Three-Layer Architecture**
   - Layer 1: Input processing
   - Layer 2: Core logic
   - Layer 3: Output validation

4. **Integrate with Validation Layer**
   - DriftLock for semantic preservation
   - Scriptoria for document quality (if applicable)
   - LawBinder for policy compliance

5. **Add TraceVault Logging**
   - All quality gates
   - Metrics and thresholds
   - Merkle root for output

### Customizing Thresholds

Thresholds can be adjusted per deployment:

```python
# config/thresholds.yaml
drift:
  default: 0.3
  critical_tasks: 0.2

compliance:
  default: 0.80
  regulated_industries: 0.95

document_quality:
  default: 0.90
  academic_papers: 0.95
  internal_docs: 0.85
```

## Performance Considerations

### Drift Detection Overhead

- **Shallow:** ~5ms per validation
- **Deep:** ~200ms (10% sampling)
- **Attention:** ~50ms (when available)

Total overhead: ~10-20ms average per validation

### Document Quality Assessment

- **Structural:** ~100ms
- **Textual:** ~300ms
- **Integrity:** ~200ms

Total: ~600ms per document

### TraceVault Logging

- **Append:** ~5ms per event
- **Merkle root:** ~10ms
- **Minimal impact** on execution time

## Security Considerations

1. **Constitutional Requirements** - Define security policies upfront
2. **Policy-Driven Coding** - Auto-prevent OWASP Top 10
3. **Principle Validation** - Enforce compliance gates
4. **TraceVault** - Immutable audit trail
5. **GDP×IDMR** - AI self-validation prevents drift

## Testing Strategy

### Unit Testing Skills

```python
def test_drift_detection():
    principles = ["requirement1", "requirement2"]
    output = "contains requirement1 and requirement2"

    result = drift_detector.detect(principles, output)

    assert result.drift_score < 0.3
    assert result.passed == True
```

### Integration Testing

```python
def test_academic_writing_pipeline():
    request = {
        'topic': 'Test topic',
        'length': 1000
    }

    paper = academic_writing.execute(request)

    assert paper.drift_score < 0.3
    assert paper.plagiarism_similarity < 0.85
    assert paper.compliance_score >= 0.80
    assert paper.omega_score >= 0.90
```

### Validation Testing

```python
def test_principle_validation():
    code = generate_code_with_vulnerability()

    result = principle_validation.validate(code)

    assert result.security_score < 0.90
    assert result.action == "BLOCK"
```

## Future Enhancements

1. **Adaptive Thresholds** - ML-based threshold optimization
2. **Real-Time Dashboards** - Live quality metrics visualization
3. **Multi-Model Validation** - Ensemble validation for critical tasks
4. **Custom Frameworks** - Pluggable governance frameworks
5. **Distributed TraceVault** - Blockchain-based audit trail

## References

### Core Documents

1. **ASDP v1.3** - AI Sovereign Definition Protocol
2. **AEGIS-C Modal v2.3** - Autonomous Governance with SAI
3. **Meta-Scholar OMEGA** - Academic automation pipeline
4. **SovereignFileSearch v1** - Constitutional file search
5. **Meta-Validation Engine v1** - AI self-validation
6. **SUPREME-CONSULT-GPT** - Strategic consulting modal
7. **Ashur Political Analysis** - Sentiment and political analysis
8. **ALECTA-AUTOEXEC Ultra+** - Fact-checking and truth verification
9. **GSWRM BUTTERFLY** - Causality prediction
10. **ASDP Optimization** - Performance patterns

### External References

- **Superpowers** (original): https://github.com/obra/superpowers
- **Claude Code**: https://docs.claude.com/en/docs/claude-code
- **OWASP Top 10**: https://owasp.org/www-project-top-ten/
- **GDPR**: https://gdpr.eu/
- **SOC2**: https://www.aicpa.org/soc

---

**Architecture Philosophy:** Structure without enforcement is documentation. Enforcement without metrics is hope. Flamehaven provides mathematical certainty.
