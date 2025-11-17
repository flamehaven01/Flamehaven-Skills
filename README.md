# Flamehaven Skills

A governance-first AI skills library built on mathematical rigor, drift detection, and constitutional enforcement. Forked from [Superpowers](https://github.com/obra/superpowers) and enhanced with Flamehaven's unique philosophy of validated execution.

## Philosophy

**Core Principle:** AI without governance is chaos. Validation without metrics is hope.

Flamehaven-Skills transforms AI execution through:
- **Mathematical Governance** - Quantitative thresholds for every decision (Drift D < 0.3, Ω ≥ 0.90, Confidence ≥ 0.85)
- **Constitutional Requirements** - Policy-driven development with automated compliance gates
- **Drift Detection** - Three-tier validation (Shallow/Deep/Attention) prevents semantic drift
- **Immutable Audit** - TraceVault hash-chained logging for full provenance
- **Quality Gates** - No execution without validation, no delivery without compliance

## What Makes Flamehaven Different

| Aspect | Traditional AI | Flamehaven Skills |
|--------|---------------|-------------------|
| **Validation** | Manual, subjective | Automated, quantitative (D < 0.3) |
| **Compliance** | Optional, post-hoc | Required, built-in (≥0.80) |
| **Quality** | "Looks good" | Mathematical scoring (Ω ≥ 0.90) |
| **Audit** | Logs if you remember | Immutable TraceVault (Merkle roots) |
| **Governance** | Guidelines | Constitutional Requirements (enforced) |

## Installation

### Claude Code (via Plugin Marketplace)

1. Register the marketplace:
```bash
/plugin marketplace add obra/superpowers-marketplace
```

2. Install Flamehaven-Skills:
```bash
/plugin install flamehaven-skills@superpowers-marketplace
```

### Verify Installation

```bash
/help
```

You should see Flamehaven skills available for use.

## Core Skills (16)

### 🧠 Thinking (5 skills)

**sovereign-definition** - ASDP Intent→Definition→Execution pipeline
- Compiles natural language into formal, executable specifications
- Completeness ≥ 0.95 required before execution

**intent-classification** - IntentRouter semantic routing
- Multi-modal intent detection with confidence scoring
- Confidence ≥ 0.85 required, ambiguity resolution built-in

**strategic-consulting** - SUPREME-CONSULT framework
- Constitutional Requirements mapping + BattleField diagnostics
- Strategy drift D < 0.3 enforcement

**philosophical-reasoning** - IRF-Calc v0.0.2 integrated reasoning
- 6-component framework (M-A-D-I-F-P): Methodic doubt, Abduction, Deduction, Induction, Falsification, Paradigm alignment
- IRF global score ≥ 0.78, all components ≥ 0.70 required
- DR3 decision protocol with 3-axis validation (Realism, Stability, Conservative Rationality)
- Drift control: JSD ≤ 0.06, L2 ≤ 0.04

**sovereign-search** - Multi-modal document search with validation
- Google FileSearch + Local RAG + Scriptoria Ω verification
- Only cite documents with Ω ≥ 0.90

### ✍️ Writing (3 skills)

**academic-writing** - Full Meta-Scholar OMEGA pipeline
- 6-stage automation: Generation → Drift Control → Review → Plagiarism → Compliance → Submission
- Zero-tolerance for drift (D < 0.3), plagiarism (similarity < 85%), or compliance violations

**drift-free-writing** - DriftLock v2 for general content
- Three-tier validation: Principle extraction → Shallow check → Deep LLM validation
- Ensures semantic preservation across all writing tasks

**structured-output** - SCL template-based generation
- Schema compliance = 100% required
- JSON/YAML/XML with constitutional validation

### 💻 Coding (1 skill)

**policy-driven-coding** - LawBinder-enforced development
- Security Score ≥ 0.90, Compliance Score ≥ 0.90 required
- Automatic vulnerability prevention (OWASP Top 10, SOC2, GDPR)
- Generates security tests automatically

### 🔬 Research (3 skills)

**sovereign-search** - See Thinking section
- ULTRA-HARVESTER query optimization
- SCRIPTORIA document quality validation (Ω ≥ 0.90)
- LAWBINDER policy compliance (≥ 0.80)

**fact-checking** - ALECTA truth verification
- FTRI (Fact Trust Reliability Index) ≥ 0.61 required
- RWTI (Reality-Weighted Trust Index) for perceived credibility
- Fake news classification (Fact/Fake/Exaggeration/Misuse)

**sentiment-analysis** - EmotionFlowLLM + influence networks
- 10-dimension emotion vectors with temporal tracking
- Regional/demographic segmentation
- Cascade propagation and echo chamber detection

### 🤝 Collaboration (1 skill)

**subagent-coordination** - Multi-agent orchestration with governance
- Task decomposition with dependency analysis
- Real-time monitoring with drift detection
- Result synthesis with conflict resolution

### ✅ Validation (4 skills)

**drift-detection** - Three-tier semantic preservation
- Shallow (keyword) + Deep (LLM) + Attention (SAI metrics)
- Drift Score D < 0.3 required for delivery
- Used by ALL other skills

**self-validation** - AI identity verification
- GDP×IDMR drift correction loop
- Conscience Circuit (BLOCK/REPAIR/ACT)
- Ensures consistent AI identity

**principle-validation** - LawBinder policy enforcement
- Constitutional Requirements check (forbidden/required)
- Regulatory compliance (GDPR, HIPAA, SOC2) ≥ 0.80
- Ethical alignment ≥ 0.80

**document-quality** - Scriptoria HSTA Ω scoring
- Structural (35%) + Textual (40%) + Integrity (25%)
- Ω ≥ 0.90 required for citation
- Merkle root generation for tamper detection

## Key Frameworks

### ASDP (AI Sovereign Definition Protocol)
Intent → Definition → Execution pipeline with governance gates

### AEGIS-C Modal
Autonomous governance with SAI metrics [T, E, C, S]
- D = 1 - (0.3·T + 0.25·E + 0.25·C + 0.2·S)
- D < 0.3 = OBSERVE (deliver), D < 0.7 = REFACTOR, D ≥ 0.7 = INHIBIT

### Scriptoria HSTA
Hybrid Structural-Textual Assessment for document quality
- Ω = 0.35·Structural + 0.40·Textual + 0.25·Integrity
- Ω ≥ 0.90 = ACCEPT for citation

### TraceVault
Immutable audit logging with hash-chained provenance
- All quality gates logged
- Merkle roots for tamper detection

## Quality Thresholds

All Flamehaven skills enforce quantitative thresholds:

| Metric | Threshold | Enforced By |
|--------|-----------|-------------|
| **Drift Score (D)** | < 0.3 | drift-detection |
| **Document Quality (Ω)** | ≥ 0.90 | document-quality |
| **Intent Confidence** | ≥ 0.85 | intent-classification |
| **Compliance Score** | ≥ 0.80 | principle-validation |
| **Security Score** | ≥ 0.90 | policy-driven-coding |
| **FTRI (Fact Trust)** | ≥ 0.61 | fact-checking |
| **Sentiment Confidence** | ≥ 0.75 | sentiment-analysis |
| **Definition Completeness** | ≥ 0.95 | sovereign-definition |
| **IRF Global Score** | ≥ 0.78 | philosophical-reasoning |
| **IRF Component (M/A/D/I/F/P)** | ≥ 0.70 each | philosophical-reasoning |
| **IRF JSD Drift** | ≤ 0.06 | philosophical-reasoning |
| **IRF L2 Drift** | ≤ 0.04 | philosophical-reasoning |
| **DR3 Axis Scores** | ≥ 0.60 each | philosophical-reasoning |

## Quick Start Examples

### Example 1: Academic Paper with Full Validation

```
User: "Write a research paper on transformer architectures"

Flamehaven:
1. Uses sovereign-definition to compile formal spec (completeness ≥ 0.95)
2. Uses academic-writing for 6-stage pipeline:
   - Generation with principles injection
   - Drift control (D < 0.3 at every stage)
   - Automated review (all checks pass)
   - Plagiarism detection (similarity < 85%)
   - IRB/regulatory compliance (100% pass)
   - Journal auto-submission
3. Uses drift-detection throughout (3-tier validation)
4. Uses document-quality to verify Ω ≥ 0.90
5. Logs to TraceVault with Merkle root

Result: Publication-ready paper with full audit trail
```

### Example 2: Secure API with Policy Enforcement

```
User: "Create a user authentication API"

Flamehaven:
1. Uses intent-classification (confidence ≥ 0.85)
2. Uses policy-driven-coding:
   - Load security policies (OWASP, SOC2)
   - Generate with security patterns injected
   - Auto-prevent vulnerabilities (SQL injection, XSS)
   - Static security analysis (SAST)
   - Security score ≥ 0.90 required
3. Uses principle-validation for compliance ≥ 0.80
4. Generates security tests automatically

Result: Production-ready API with zero critical vulnerabilities
```

### Example 3: Multi-Agent Research with Governance

```
User: "Research AI governance frameworks across 5 papers"

Flamehaven:
1. Uses sovereign-definition to decompose task
2. Uses subagent-coordination:
   - Spawn 5 parallel agents
   - Each uses sovereign-search (Ω ≥ 0.90 only)
   - Real-time drift monitoring
   - Result synthesis with conflict resolution
3. Uses fact-checking for FTRI ≥ 0.61
4. Uses document-quality for final report (Ω ≥ 0.90)

Result: Validated research synthesis in fraction of sequential time
```

### Example 4: Philosophical Decision with IRF-Calc

```
User: "Should we pivot our SaaS to AI-native architecture?"

Flamehaven:
1. Uses philosophical-reasoning with full M-A-D-I-F-P analysis:
   - M (Methodic Doubt): Extract premises (explicit + implicit), flag suspects
   - A (Abduction): Generate 3 hypotheses (full rewrite, incremental, partner)
   - D (Deduction): Derive logical consequences for each hypothesis
   - I (Induction): Check empirical fit against pilot data
   - F (Falsification): Generate adversarial tests, search counterexamples
   - P (Paradigm): Assess alignment with "Cloud-first SaaS" paradigm

2. IRF Score Calculation:
   - M=0.75, A=0.78, D=0.82, I=0.77, F=0.78, P=0.76
   - Global IRF = 0.79 ✓ (≥ 0.78 threshold)
   - All components ≥ 0.70 ✓

3. DR3 Decision Protocol:
   - Realism (I,F): 0.78
   - Stability (D,M): 0.81
   - Conservative Rationality (A,P): 0.74
   - Selected: "Incremental AI layer + 2-year roadmap"

Result: Philosophically rigorous decision with full reasoning trace
```

## How It Works

### 1. SessionStart Hook
Loads the Flamehaven governance framework at session start

### 2. Constitutional Requirements
Every task operates under defined principles and constraints

### 3. Quality Gates
No execution phase completes without validation:
- Drift detection (D < 0.3)
- Compliance scoring (≥ 0.80)
- Quality assessment (Ω ≥ 0.90)

### 4. Immutable Audit
TraceVault logs all decisions with Merkle roots for provenance

### 5. Automatic Integration
Skills activate when quality/governance requirements match task context

## Architecture

```
Foundation Layer
├─ ASDP (Intent → Definition → Execution)
├─ TraceVault (Immutable Audit)
└─ Constitutional Requirements

Validation Layer
├─ DriftLock (3-tier validation)
├─ Scriptoria (Document Ω scoring)
├─ LawBinder (Policy enforcement)
└─ GDP×IDMR (AI self-validation)

Application Layer
├─ Thinking (sovereign-definition, intent-classification, strategic-consulting)
├─ Writing (academic-writing, drift-free-writing, structured-output)
├─ Coding (policy-driven-coding)
├─ Research (sovereign-search, fact-checking, sentiment-analysis)
├─ Collaboration (subagent-coordination)
└─ Validation (drift-detection, self-validation, principle-validation, document-quality)
```

See [ARCHITECTURE.md](./ARCHITECTURE.md) for detailed design.

## Contributing

Skills live directly in this repository. To contribute:

1. Fork the repository
2. Create a branch for your skill: `claude/your-feature-name-<session-id>`
3. Follow the Flamehaven template (see existing skills)
4. Ensure quantitative thresholds are defined
5. Include validation gates and TraceVault logging
6. Submit a PR with validation report

### Skill Template Requirements

All Flamehaven skills MUST include:
- **Frontmatter** with name and description
- **The Iron Law** section with quantitative threshold
- **Three-layer architecture** (when applicable)
- **Red Flags** section
- **Integration** section (required/complementary skills)
- **Example** with metrics
- **Verification Checklist**
- **Final Rule** with mathematical expression

## Updating

```bash
/plugin update flamehaven-skills
```

## Philosophy: Why Mathematical Governance?

Traditional AI systems rely on subjective quality assessment:
- "This looks good"
- "Close enough"
- "Seems correct"

Flamehaven enforces objective standards:
- Drift Score D < 0.3 (measured)
- Document Quality Ω ≥ 0.90 (calculated)
- Compliance Score ≥ 0.80 (validated)

**Result:** Reproducible quality, auditable decisions, trustworthy AI.

## Support

- **Issues**: https://github.com/flamehaven01/Flamehaven-Skills/issues
- **Original Superpowers**: https://github.com/obra/superpowers
- **Philosophy**: Governance-first AI execution with mathematical rigor

## License

MIT License - see LICENSE file for details

## Acknowledgments

Forked from [Superpowers by obra](https://github.com/obra/superpowers), enhanced with Flamehaven's governance-first philosophy.

Core frameworks: ASDP, AEGIS-C, Meta-Scholar OMEGA, Scriptoria, TraceVault, LawBinder, ALECTA, SUPREME-CONSULT, EmotionFlowLLM.

---

**Remember:** Output without validation is risk. Quality without measurement is hope. Flamehaven provides certainty.
