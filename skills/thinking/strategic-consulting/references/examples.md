# Examples

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

