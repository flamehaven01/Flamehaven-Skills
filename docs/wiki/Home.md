# Flamehaven Skills Wiki

Welcome to the Flamehaven Skills documentation. This wiki explains the philosophy, architecture, and technical implementation of Flamehaven's token-optimized AI skill system.

## What is Flamehaven Skills?

Flamehaven Skills is a **production-grade AI capability framework** that extends Claude Code with 40+ specialized expert-level skills while achieving **83% token reduction** compared to traditional skill implementations.

**Core Metrics:**
- **40 specialized skills** across 8 domains
- **83% token reduction** (79,909 → 13,500 tokens base load)
- **100% functionality preservation** (zero deletions)
- **90.5% average compression** per skill
- **Flamehaven governance integration** (DriftLock, Scriptoria, IRF-Calc)

## Quick Navigation

### Core Documentation
- **[What are Skills?](What-are-Skills.md)** - Understanding Claude Code Skills system
- **[Why Flamehaven is Different](Why-Flamehaven-is-Different.md)** - Our unique philosophy and approach
- **[Token Optimization Architecture](Token-Optimization-Architecture.md)** - Technical deep-dive into Progressive Disclosure
- **[Traditional vs Flamehaven Comparison](Traditional-vs-Flamehaven.md)** - Side-by-side analysis
- **[Optimization Report](Optimization-Report.md)** - Detailed metrics and results

### Skill Categories
- **Coding & Development**: policy-driven-coding, systematic-debugging, test-driven-development
- **Collaboration**: subagent-coordination, dispatching-parallel-agents, sharing-skills
- **Validation & Quality**: drift-detection, principle-validation, document-quality, self-validation
- **Thinking & Analysis**: philosophical-reasoning, intent-classification, strategic-consulting
- **Writing**: academic-writing, drift-free-writing, structured-output
- **Research**: fact-checking, sentiment-analysis
- **Sovereign (Meta-Cognitive)**: sovereign-code, sovereign-core, sovereign-debug, sovereign-refactor, sovereign-definition, sovereign-search

### Philosophy

> **"우린 무조건 지우지 않는다"**
> *"We never delete anything"*

Flamehaven's core principle: **Optimize through organization, not deletion.**

Traditional approaches sacrifice functionality for performance. Flamehaven achieves both through intelligent architecture:
- **Progressive Disclosure**: Load minimal, expand on demand
- **Governance-First**: Preserve all Iron Laws and constitutional requirements
- **Pattern Extraction**: Automated identification of critical vs. reference content
- **Zero Loss**: 100% functionality maintained across all optimizations

## Architecture Overview

```
Traditional Skills (per skill):
├─ SKILL.md (8-24KB)           ← Everything in one file
└─ Load 2,000-6,000 tokens     ← All or nothing

Flamehaven Skills (per skill):
├─ SKILL.md (600-1,500 bytes)  ← Essentials only
│  ├─ Iron Law                 ← Constitutional requirements
│  ├─ Thresholds               ← Quantitative metrics
│  ├─ Overview                 ← Core principle (200 words)
│  └─ When to Use              ← Trigger conditions (5 bullets)
└─ references/ (on-demand)     ← Progressive loading
   ├─ workflow.md              ← Detailed step-by-step
   ├─ algorithms.md            ← Python pseudocode
   ├─ examples.md              ← Usage demonstrations
   └─ governance.md            ← Validation rules

Token load: 150-370 tokens base (85-95% reduction)
```

## Key Innovations

### 1. Progressive Disclosure Pattern
**Problem**: Traditional skills load entire documentation (2,000-6,000 tokens) even when only trigger detection is needed.

**Solution**: Three-tier loading system
- **Tier 1 (Always)**: Iron Law + Thresholds + Overview + Triggers (150-370 tokens)
- **Tier 2 (On-demand)**: Load specific reference when workflow details needed
- **Tier 3 (CLI fallback)**: Complex operations via subprocess (0 tokens)

### 2. Governance Integration
Every Flamehaven Skill enforces:
- **DriftLock**: Semantic drift prevention (D < 0.3)
- **Scriptoria**: Document quality scoring (Ω ≥ 0.90)
- **IRF-Calc**: Philosophical reasoning depth (≥ 0.78)
- **Constitutional Compliance**: Policy adherence (≥ 0.80)

### 3. Automated Pattern Extraction
`FlamehavenOptimizer` automatically identifies and extracts:
- **Iron Laws**: "NO X WITHOUT Y" statements
- **Quantitative Thresholds**: All metrics (≥, <, =, %)
- **Core Workflows**: High-level process flows
- **Detailed Content**: Moves to references/

### 4. Zero-Deletion Philosophy
**Not implemented:**
- ❌ Content summarization (loses nuance)
- ❌ Example removal (loses practical guidance)
- ❌ Workflow simplification (loses completeness)

**Implemented:**
- ✓ Strategic reorganization (essentials vs. details)
- ✓ Progressive loading (minimal → full as needed)
- ✓ Complete preservation (references/ holds everything)

## Results at a Glance

| Metric | Before | After | Reduction |
|--------|--------|-------|-----------|
| **Total Repository Size** | 319,636 bytes | 53,499 bytes | **83.3%** |
| **Base Token Load** | 79,909 tokens | 13,500 tokens | **83.1%** |
| **Average Skill Size** | 7,991 bytes | 818 bytes | **89.8%** |
| **Largest Skill** | 24,267 bytes | 1,071 bytes | **95.6%** |
| **Skills Optimized** | - | 34 skills | - |
| **Functionality Lost** | - | **0%** | - |

**Top 5 Reductions:**
1. `philosophical-reasoning`: 95.6% (24,267 → 1,071 bytes)
2. `structured-output`: 95.6% (17,054 → 752 bytes)
3. `subagent-coordination`: 94.8% (16,108 → 844 bytes)
4. `policy-driven-coding`: 94.4% (16,568 → 930 bytes)
5. `document-quality`: 94.4% (16,603 → 930 bytes)

## Getting Started

### For Users
Browse the skill categories above to find the capability you need. Each skill page includes:
- **Purpose**: What problem it solves
- **Iron Law**: Constitutional requirements that MUST be followed
- **Thresholds**: Quantitative success criteria
- **When to Use**: Trigger conditions for automatic activation

### For Developers
See [Token Optimization Architecture](Token-Optimization-Architecture.md) to understand:
- How Progressive Disclosure works
- Pattern extraction algorithms
- Governance validation system
- How to create new optimized skills

### For Researchers
Compare [Traditional vs Flamehaven](Traditional-vs-Flamehaven.md) to analyze:
- Token efficiency trade-offs
- Architectural design decisions
- Performance vs. functionality balance
- Real-world optimization results

## Contributing

Flamehaven Skills follows strict governance standards. To contribute:

1. **Understand the Philosophy**: Read [Why Flamehaven is Different](Why-Flamehaven-is-Different.md)
2. **Follow the Pattern**: Use `FlamehavenOptimizer` for new skills
3. **Preserve Governance**: All Iron Laws and Thresholds must be maintained
4. **Test Thoroughly**: Dry-run optimization before committing
5. **Document Metrics**: Include before/after token measurements

## License & Attribution

Flamehaven Skills v1.2.0
Built on Sovereign-Tools v1.1.0 architecture
Integrates ASDP DriftLock + AEGIS-C governance frameworks

---

**Philosophy**: "우린 무조건 지우지 않는다" - Optimization through intelligence, not deletion
**Architecture**: Progressive Disclosure + Governance-First + Zero Loss
**Result**: 83% token reduction, 100% functionality preservation
