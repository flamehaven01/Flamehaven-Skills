---
name: strategic-consulting
description: SUPREME-CONSULT framework for SaaS strategic analysis - combines Constitutional Requirements mapping, BattleField diagnostics, and drift-free strategy generation with governance gates
---

# Strategic Consulting & SaaS Strategy

## Overview

Generic advice without structure is noise. Strategy without governance creates execution drift.

**Core principle:** ALWAYS ground strategy in Constitutional Requirements and validate with BattleField diagnostics.

## The Iron Law

```
NO STRATEGIC ADVICE WITHOUT CONSTITUTIONAL GROUNDING
Strategy Drift D < 0.3 REQUIRED
```

## When to Use

Use for ANY strategic consulting task:
- SaaS product strategy
- Market positioning analysis
- Competitive landscape evaluation
- Growth strategy development
- Business model validation
- Investment decision support

**Use this ESPECIALLY when:**
- Client has vague requirements
- Strategy must align with company values/mission
- Execution risk is high
- Multiple stakeholders with conflicting priorities
- Long-term commitment required

## Three-Layer Framework

### Layer 1: Constitutional Requirements (Intent Definition)

**BEFORE strategy generation:**

1. **Extract Constitutional Principles**
   ```python
   constitution = extract_requirements(client_context)

   # Example:
   # {
   #   'mission': 'Democratize AI for SMBs',
   #   'values': ['transparency', 'privacy-first', 'no-vendor-lock-in'],
   #   'constraints': ['budget < $50K', 'time-to-market < 6mo'],
   #   'success_metrics': ['ARR > $1M', 'churn < 5%']
   # }
   ```

2. **Validate Intent Clarity**
   ```python
   clarity_score = intent_classifier.evaluate(constitution)

   if clarity_score < 0.85:
       REQUEST_CLARIFICATION()
   ```

**Threshold:** Intent clarity ≥ 0.85 required

### Layer 2: BattleField Diagnostics (Current State Analysis)

**WHEN Constitutional Requirements established:**

1. **5-Dimension Assessment**
   ```python
   battlefield = {
       'market': analyze_market_landscape(),     # TAM, competition, trends
       'product': analyze_product_maturity(),    # PMF, features, tech debt
       'team': analyze_org_capability(),         # skills, culture, capacity
       'finance': analyze_financial_health(),    # runway, unit economics
       'operations': analyze_execution_risk()    # process maturity, bottlenecks
   }
   ```

2. **Threat-Opportunity Matrix**
   ```
   High Impact + High Urgency → CRITICAL
   High Impact + Low Urgency → STRATEGIC
   Low Impact + High Urgency → TACTICAL
   Low Impact + Low Urgency → BACKLOG
   ```

3. **Gap Analysis**
   ```python
   gaps = []
   for dimension in battlefield:
       current_state = battlefield[dimension]
       required_state = derive_from_constitution(constitution, dimension)
       gap = calculate_gap(current_state, required_state)
       if gap > threshold:
           gaps.append({
               'dimension': dimension,
               'gap': gap,
               'priority': calculate_priority(gap, constitution)
           })
   ```

**Threshold:** All CRITICAL gaps must be addressed

### Layer 3: Strategy Generation (Drift-Free Execution)

**WHEN BattleField assessed:**

1. **Generate Strategy Options**
   ```python
   strategies = []
   for gap in sorted(gaps, key=lambda x: x['priority'], reverse=True):
       options = generate_solutions(
           gap=gap,
           constitution=constitution,
           battlefield=battlefield
       )
       strategies.extend(options)
   ```

2. **Constitutional Alignment Check**
   ```python
   for strategy in strategies:
       alignment_score = validate_alignment(
           strategy=strategy,
           constitution=constitution
       )

       if alignment_score < 0.9:
           REJECT_STRATEGY(strategy)
   ```

3. **Drift Detection**
   ```python
   # REQUIRED: Use drift-detection skill
   drift_score = drift_detector.detect(
       original=constitution,
       output=strategy,
       attention=generation_attention
   )

   if drift_score >= 0.3:
       REFACTOR_STRATEGY()
   ```

**Threshold:** Alignment ≥ 0.9 AND Drift D < 0.3

## Integrated Flow

```
Client Request
    ↓
[Constitutional Requirements]
    ├─ Mission extraction
    ├─ Values identification
    ├─ Constraints mapping
    └─ Success metrics definition
    ↓
[BattleField Diagnostics]
    ├─ 5-dimension assessment
    ├─ Threat-opportunity matrix
    └─ Gap analysis
    ↓
[Strategy Generation]
    ├─ Solution options
    ├─ Constitutional alignment
    └─ Drift validation
    ↓
[Execution Roadmap]
    ├─ Prioritized initiatives
    ├─ Resource allocation
    └─ Success metrics tracking
    ↓
OUTPUT: Validated strategy + roadmap + governance checkpoints
```

## Red Flags

- "Let's skip the Constitutional Requirements"
- "We can define values later"
- "BattleField analysis is overkill"
- "Strategy looks good enough"
- "No time for drift validation"

**ALL mean: STOP. Run full SUPREME-CONSULT framework.**

## Integration

**REQUIRED by:**
- `business-planning` - Strategic foundation
- `product-strategy` - Product roadmap alignment
- `investment-analysis` - Due diligence validation

**Complementary:**
- `drift-detection` - Strategy quality validation
- `fact-checking` - Market data verification
- `sentiment-analysis` - Customer feedback integration

## Example: SaaS Expansion Strategy

**Client Request:** "Help us expand into enterprise market"

**Execution:**

1. **Constitutional Requirements:**
   ```python
   constitution = {
       'mission': 'AI-powered analytics for growth teams',
       'values': ['customer-obsessed', 'data-privacy', 'rapid-innovation'],
       'constraints': ['ARR $5M', 'team 30 people', 'runway 18mo'],
       'success': ['enterprise ARR $10M in 24mo', 'NPS > 50']
   }
   Intent Clarity: 0.92 ✓
   ```

2. **BattleField Diagnostics:**
   ```python
   battlefield = {
       'market': {
           'TAM': '$2B enterprise analytics',
           'competition': 'High (Tableau, Looker)',
           'trend': 'AI-native tools gaining traction'
       },
       'product': {
           'PMF': 'Strong in SMB, unknown in enterprise',
           'gaps': ['SSO', 'role-based access', 'audit logs']
       },
       'team': {
           'enterprise_exp': 'Low (2/30 people)',
           'sales_process': 'Self-serve, no enterprise motion'
       },
       'finance': {
           'runway': '18mo',
           'CAC': '$500 (SMB), unknown (enterprise)'
       },
       'operations': {
           'compliance': 'SOC2 Type I (need Type II)',
           'support': '9-5, need 24/7 for enterprise'
       }
   }

   Gaps Identified:
   - CRITICAL: Product gaps (SSO, RBAC) - blocks sales
   - CRITICAL: Team gaps (enterprise sales) - no GTM motion
   - STRATEGIC: Compliance (SOC2 Type II) - trust requirement
   - TACTICAL: Support coverage - customer expectation
   ```

3. **Strategy Generation:**
   ```python
   strategy = {
       'phase_1': [
           'Hire VP Enterprise Sales (3mo)',
           'Build SSO + RBAC (4mo)',
           'Achieve SOC2 Type II (6mo)'
       ],
       'phase_2': [
           'Pilot with 3 enterprise customers',
           'Validate CAC < $10K',
           'Refine sales process'
       ],
       'phase_3': [
           'Scale enterprise sales team',
           'Expand 24/7 support',
           'Target $10M enterprise ARR'
       ]
   }

   Constitutional Alignment: 0.94 ✓
   Drift Score: 0.18 ✓
   ```

**Output:**
- Roadmap: 24-month phased expansion
- Investment: $2M (sales + product + compliance)
- Success metrics: Enterprise ARR $10M, CAC < $10K, NPS > 50
- Governance: Quarterly Constitutional alignment checks

## Verification Checklist

- [ ] Constitutional Requirements extracted (clarity ≥ 0.85)
- [ ] BattleField 5-dimension assessment completed
- [ ] All CRITICAL gaps identified
- [ ] Strategy options generated
- [ ] Constitutional alignment ≥ 0.9
- [ ] Drift score D < 0.3
- [ ] Execution roadmap with milestones
- [ ] Governance checkpoints defined
- [ ] TraceVault logged

## Final Rule

```
Strategy → Constitutionally grounded AND BattleField validated AND D < 0.3
Otherwise → not actionable
```

Strategy without governance is just advice.
