# IRF-Calc v0.0.2 Infrastructure

Philosophical reasoning infrastructure for Flamehaven-Skills, implementing the M-A-D-I-F-P framework with quantitative quality gates.

## Overview

This directory contains the complete infrastructure for training, validating, and deploying IRF-Calc philosophical reasoning models.

### Components

**M (Methodic Doubt)** - Premise Purification
**A (Abduction)** - Hypothesis Generation
**D (Deduction)** - Logical Consequence Derivation
**I (Induction)** - Empirical Consistency
**F (Falsification)** - Killer Counterexample Search
**P (Paradigm)** - Paradigm Alignment

## Directory Structure

```
infrastructure/irf-calc/
├── README.md                      # This file
├── config/
│   └── helm-values.yaml           # IRF-Calc configuration (thresholds, drift limits, DR3)
├── schemas/
│   ├── schema_M_premise_purification.json
│   ├── schema_D_deduction_pairwise.json
│   ├── schema_F_falsification_pairwise.json
│   ├── schema_golden_M_premise_purification.json
│   ├── schema_golden_D_deduction_pairwise.json
│   └── schema_golden_F_falsification_pairwise.json
├── scripts/
│   ├── collect_pilot_data.py      # GitHub PR review crawler for M/D/F data
│   ├── compute_iaa.py              # Inter-Annotator Agreement (Cohen/Fleiss Kappa)
│   ├── validate_annotation.py      # JSON Schema validator
│   ├── convert_golden_to_train.py  # Golden → training format converter
│   └── validate_labelstudio_annotations.py  # Label Studio export validator
├── golden_examples/
│   ├── M/                          # 4+ golden M examples
│   ├── D/                          # 4+ golden D examples
│   └── F/                          # 4+ golden F examples
├── data/
│   ├── pilot/                      # Pilot data collection
│   ├── train/                      # Training datasets (JSONL)
│   └── annotations/                # Label Studio exports
└── docs/
    ├── annotation_guide.md         # Annotator manual
    └── calibration_quiz.md         # Quality calibration test
```

## Quick Start

### 1. Install Dependencies

```bash
pip install requests tqdm jsonschema numpy pandas scikit-learn statsmodels
```

### 2. Collect Pilot Data

```bash
export GITHUB_TOKEN="your_github_token"

# Collect M (Premise Purification) data
python scripts/collect_pilot_data.py --component M --count 30

# Collect D (Deduction) data
python scripts/collect_pilot_data.py --component D --count 40

# Collect F (Falsification) data
python scripts/collect_pilot_data.py --component F --count 30

# Or collect all
python scripts/collect_pilot_data.py --component all
```

### 3. Validate Golden Examples

```bash
# Validate all golden examples
python scripts/validate_annotation.py golden_examples

# Validate specific file
python scripts/validate_annotation.py golden_examples/M/M_000001.json
```

### 4. Convert Golden to Training Format

```bash
python scripts/convert_golden_to_train.py

# Output:
# data/train/train_M.jsonl
# data/train/train_D.jsonl
# data/train/train_F.jsonl
```

### 5. Label Studio Annotation

```bash
# Import golden examples to Label Studio
# Use templates in config/label_studio_*.xml

# Export annotations
# data/annotations/ls_export.json
```

### 6. Validate Label Studio Annotations

```bash
python scripts/validate_labelstudio_annotations.py \
    --input data/annotations/ls_export.json \
    --output data/annotations/ls_valid.jsonl
```

### 7. Compute Inter-Annotator Agreement

```bash
python scripts/compute_iaa.py \
    --input data/annotations/ls_export.json \
    --output data/annotations/iaa_report.json
```

## Quality Thresholds

| Metric | Threshold | Component |
|--------|-----------|-----------|
| **IRF Global Score** | ≥ 0.78 | All components |
| **M Score** | ≥ 0.70 | Premise purification |
| **A Score** | ≥ 0.70 | Hypothesis generation |
| **D Score** | ≥ 0.70 | Deduction quality |
| **I Score** | ≥ 0.70 | Empirical consistency |
| **F Score** | ≥ 0.70 | Falsification rigor |
| **P Score** | ≥ 0.70 | Paradigm alignment |
| **JSD Drift** | ≤ 0.06 | Distribution drift |
| **L2 Drift** | ≤ 0.04 | Component vector drift |
| **Calibration Corr** | ≥ 0.90 | Reference benchmark |

## Training Pipeline

### Stagewise Instruction Tuning

```python
# 1. M (Premise Purification) - 30K steps
# 2. A (Abduction) - 40K steps
# 3. D (Deduction) - 40K steps
# 4. I (Induction) - 30K steps
# 5. F (Falsification) - 25K steps
# 6. P (Paradigm) - 25K steps
# 7. Joint Multi-Task - 60K steps
```

Total: ~250K steps

### Data Requirements

| Component | Minimum | Target | Source |
|-----------|---------|--------|--------|
| M | 100 | 500 | GitHub PR reviews + synthetic |
| D | 100 | 500 | Logic proofs + code reviews |
| F | 100 | 500 | Bug reports + adversarial tests |
| A | 100 | 500 | Research papers + abductive reasoning |
| I | 100 | 500 | Empirical studies + data analysis |
| P | 100 | 500 | Paradigm shift papers + Socratic dialogue |

## DR3 Decision Protocol

After IRF scoring, apply 3-axis decision fusion:

```yaml
axes:
  realism:                      # Based on I, F
    weight: 0.4
    threshold: 0.6
  stability:                    # Based on D, M
    weight: 0.4
    threshold: 0.6
  conservative_rationality:     # Based on A, P
    weight: 0.2
    threshold: 0.6

selection_rule: "argmax score s.t. all axes ≥ 0.6"
fallback_rule: "abstain_and_request_more_evidence"
```

## Drift Control

### JSD (Jensen-Shannon Divergence)

```
p_i^(t) = s_i^(t) / Σ_j s_j^(t)
drift_jsd_irf = JSD(p^(t1), p^(t2)) / log(2)

Threshold: ≤ 0.06
Warning: ≥ 0.04
```

### L2 (Component Vector)

```
q_bar^(t) = mean([M, A, D, I, F, P])
drift_l2_irf = || q_bar^(t1) - q_bar^(t2) ||_2

Threshold: ≤ 0.04
Warning: ≥ 0.03
```

## Integration with Flamehaven-Skills

### Skill Usage

```python
from flamehaven_skills import PhilosophicalReasoning

reasoning = PhilosophicalReasoning()

result = reasoning.analyze(
    problem="Should we pivot our SaaS to AI-native architecture?",
    context="...",
    paradigm="Cloud-first SaaS"
)

# Result includes:
# - IRF scores (M,A,D,I,F,P + global)
# - Drift metrics (JSD, L2)
# - DR3 decision
# - Full reasoning trace
```

### Quality Gates

```python
assert result['irf']['global'] >= 0.78
assert all(result['irf'][c] >= 0.70 for c in ['M','A','D','I','F','P'])
assert result['drift']['jsd'] <= 0.06
assert result['drift']['l2'] <= 0.04
assert result['dr3']['decision'] != 'ABSTAIN' or result['dr3']['confidence'] < 0.6
```

## Validation Workflow

```
Golden Examples (12+)
    ↓
[Schema Validation] → validate_annotation.py
    ↓
[Convert to Training] → convert_golden_to_train.py
    ↓
[Label Studio Import]
    ↓
[Human Annotation]
    ↓
[IAA Computation] → compute_iaa.py (κ ≥ 0.70)
    ↓
[Export Validation] → validate_labelstudio_annotations.py
    ↓
[Training Data Ready] → train_M/D/F.jsonl
```

## Deployment

### Helm Install

```bash
helm install irf-calc ./charts/irf-calc \
    -f infrastructure/irf-calc/config/helm-values.yaml \
    --namespace flamehaven
```

### Environment Variables

```bash
# From inference controller
IRF_LOOP_MAX_CYCLES=2
IRF_LOOP_GLOBAL_MIN=0.78
IRF_LOOP_COMPONENT_MIN_M=0.70
IRF_LOOP_COMPONENT_MIN_A=0.70
IRF_LOOP_COMPONENT_MIN_D=0.70
IRF_LOOP_COMPONENT_MIN_I=0.70
IRF_LOOP_COMPONENT_MIN_F=0.70
IRF_LOOP_COMPONENT_MIN_P=0.70

# From DR3 protocol
IRF_DR3_REALISM_WEIGHT=0.4
IRF_DR3_STABILITY_WEIGHT=0.4
IRF_DR3_CONSERVATIVE_RATIONALITY_WEIGHT=0.2
IRF_DR3_MIN_AXIS_SCORE=0.6
```

## Monitoring

### Prometheus Metrics

```
rex_irf_score{component="M|A|D|I|F|P|global"}
rex_irf_drift_jsd
rex_irf_drift_l2
rex_irf_corr_ref
rex_irf_dr3_realism
rex_irf_dr3_stability
rex_irf_dr3_conservative_rationality
```

### Alerts

```yaml
- alert: IRFDriftHigh
  expr: rex_irf_drift_jsd > 0.06
  severity: critical

- alert: IRFCalibrationLow
  expr: rex_irf_corr_ref < 0.90
  severity: warning

- alert: IRFComponentLow
  expr: rex_irf_score < 0.70
  severity: warning
```

## Contributing

### Adding New Golden Examples

1. Create `golden_examples/{M|D|F}/{ID}_{description}.json`
2. Follow schema: `schemas/schema_golden_{M|D|F}_*.json`
3. Validate: `python scripts/validate_annotation.py golden_examples/{M|D|F}/{new_file}.json`
4. Convert to training: `python scripts/convert_golden_to_train.py`

### Updating Schemas

1. Edit `schemas/schema_*.json`
2. Re-validate all examples: `python scripts/validate_annotation.py golden_examples`
3. Update documentation if fields changed

### Tuning Thresholds

Edit `config/helm-values.yaml`:

```yaml
thresholds:
  effective:
    globalMin: 0.78  # Adjust based on calibration
    componentMin:
      M: 0.70        # Can tune per-component
```

## Troubleshooting

### Low IAA (κ < 0.60)

**Cause:** Annotator disagreement
**Fix:**
1. Review annotation guide
2. Add more golden examples
3. 1:1 annotator coaching
4. Simplify task if too complex

### High Drift (JSD > 0.06 or L2 > 0.04)

**Cause:** Model behavior changed
**Fix:**
1. Check for data distribution shift
2. Verify training pipeline consistency
3. Add drift penalties to loss function
4. Increase calibration dataset size

### Low Calibration (corr < 0.90)

**Cause:** Model not aligned with reference
**Fix:**
1. Review reference benchmark quality
2. Add more calibration examples
3. Fine-tune on reference tasks
4. Check for systematic bias

## References

- **ASDP v1.3**: AI Sovereign Definition Protocol
- **AEGIS-C Modal v2.3**: Autonomous Governance with SAI
- **Meta-Scholar OMEGA**: Academic automation pipeline
- **Socratic Dialogue LLM**: Philosophical reasoning datasets
- **Flamehaven-Skills**: Parent framework

## License

MIT License - see LICENSE file for details

---

**Philosophy:** Shallow reasoning misleads. Quantified philosophical rigor reveals truth.
