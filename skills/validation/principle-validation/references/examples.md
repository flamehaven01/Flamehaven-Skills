# Examples

**Output:** Code that processes user email addresses

**Execution:**

1. **Constitutional Check:**
   ```python
   constitution = {
       'forbidden': ['sell_user_data', 'track_without_consent'],
       'required': ['data_encryption', 'user_consent', 'audit_trail']
   }

   # Check forbidden
   violations = check_forbidden(code_output, constitution)
   # Result: No violations ✓

   # Check required
   missing = check_required(code_output, constitution)
   # Result: Missing 'audit_trail' ✗

   action: REFACTOR to add audit logging
   ```

2. **After Refactor - Regulatory Check:**
   ```python
   regulations = ['GDPR', 'CCPA']

   compliance = {
       'GDPR': {
           'user_consent': ✓,
           'data_minimization': ✓,
           'encryption': ✓,
           'right_to_deletion': ✓,
           'score': 1.0
       },
       'CCPA': {
           'opt_out_mechanism': ✓,
           'data_sale_prohibition': ✓,
           'score': 1.0
       },
       'overall': 1.0 ✓
   }
   ```

3. **Ethics Check:**
   ```python
   ethics = {
       'fairness': 0.95 ✓,
       'transparency': 0.88 ✓,
       'privacy': 0.92 ✓,
       'safety': 0.90 ✓,
       'autonomy': 0.85 ✓,
       'overall': 0.90 ✓
   }

   bias_detected: None ✓
   ```

**Final Decision:**
```python
Gate: APPROVE ✓
Compliance Score: 1.0
Ethics Score: 0.90
Violations: None
```

**Output:** Code approved for deployment with full compliance report

