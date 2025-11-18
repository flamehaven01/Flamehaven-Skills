# Algorithms

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

```python
clarity_score = intent_classifier.evaluate(constitution)

   if clarity_score < 0.85:
       REQUEST_CLARIFICATION()
   
```

```python
battlefield = {
       'market': analyze_market_landscape(),     # TAM, competition, trends
       'product': analyze_product_maturity(),    # PMF, features, tech debt
       'team': analyze_org_capability(),         # skills, culture, capacity
       'finance': analyze_financial_health(),    # runway, unit economics
       'operations': analyze_execution_risk()    # process maturity, bottlenecks
   }
   
```

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

```python
for strategy in strategies:
       alignment_score = validate_alignment(
           strategy=strategy,
           constitution=constitution
       )

       if alignment_score < 0.9:
           REJECT_STRATEGY(strategy)
   
```

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

```python
constitution = {
       'mission': 'AI-powered analytics for growth teams',
       'values': ['customer-obsessed', 'data-privacy', 'rapid-innovation'],
       'constraints': ['ARR $5M', 'team 30 people', 'runway 18mo'],
       'success': ['enterprise ARR $10M in 24mo', 'NPS > 50']
   }
   Intent Clarity: 0.92 ✓
   
```

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