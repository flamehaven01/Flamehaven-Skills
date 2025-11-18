# Algorithms

```python
constitution = {
       'mission': 'Core organizational mission',
       'values': ['value1', 'value2', 'value3'],
       'constraints': {
           'forbidden': ['banned_topics', 'restricted_actions'],
           'required': ['mandatory_checks', 'must_include_elements']
       },
       'quality_standards': {
           'drift_threshold': 0.3,
           'confidence_threshold': 0.85,
           'validation_required': True
       }
   }

   # Example:
   # {
   #   'mission': 'Build privacy-first AI tools',
   #   'values': ['transparency', 'user_privacy', 'no_vendor_lock_in'],
   #   'constraints': {
   #     'forbidden': ['user_tracking', 'data_selling', 'dark_patterns'],
   #     'required': ['data_encryption', 'user_consent', 'audit_trail']
   #   }
   # }
   
```

```python
def check_forbidden(output, constitution):
       violations = []

       for forbidden_item in constitution['constraints']['forbidden']:
           if detect_presence(output, forbidden_item):
               violations.append({
                   'type': 'forbidden_content',
                   'item': forbidden_item,
                   'severity': 'critical',
                   'action': 'BLOCK'
               })

       return violations

   # Example checks:
   # - No personal data exposure (PII)
   # - No biased language
   # - No security vulnerabilities
   # - No copyright violations
   
```

```python
def check_required(output, constitution):
       missing = []

       for required_item in constitution['constraints']['required']:
           if not detect_presence(output, required_item):
               missing.append({
                   'type': 'missing_required',
                   'item': required_item,
                   'severity': 'high',
                   'action': 'REFACTOR'
               })

       return missing

   # Example checks:
   # - Audit trail present
   # - Citations included
   # - Error handling implemented
   # - Security best practices followed
   
```

```python
def identify_regulations(output, context):
       applicable = []

       # Data privacy regulations
       if contains_user_data(output):
           applicable.extend(['GDPR', 'CCPA', 'LGPD'])

       # Healthcare data
       if contains_health_data(output):
           applicable.append('HIPAA')

       # Financial data
       if contains_financial_data(output):
           applicable.extend(['PCI-DSS', 'SOX'])

       # Security standards
       if is_security_critical(output):
           applicable.extend(['SOC2', 'ISO27001'])

       # Industry-specific
       applicable.extend(context.get('industry_regulations', []))

       return applicable
   
```

```python
compliance_checks = {
       'GDPR': [
           'user_consent_documented',
           'data_minimization_applied',
           'right_to_deletion_supported',
           'data_portability_enabled',
           'breach_notification_implemented'
       ],
       'HIPAA': [
           'phi_encrypted_at_rest',
           'phi_encrypted_in_transit',
           'access_controls_implemented',
           'audit_logs_maintained',
           'business_associate_agreement'
       ],
       'SOC2': [
           'access_logging',
           'change_management',
           'incident_response',
           'data_backup',
           'vendor_management'
       ]
   }

   def validate_regulation(output, regulation):
       checks = compliance_checks[regulation]
       results = []

       for check in checks:
           passed = execute_check(output, check)
           results.append({
               'check': check,
               'passed': passed,
               'regulation': regulation
           })

       compliance_score = sum(r['passed'] for r in results) / len(results)
       return compliance_score, results
   
```

```python
def calculate_compliance_score(output, regulations):
       if not regulations:
           return 1.0  # No regulations apply

       total_score = 0
       for regulation in regulations:
           score, details = validate_regulation(output, regulation)
           total_score += score

       overall_score = total_score / len(regulations)

       return {
           'overall': overall_score,
           'by_regulation': {
               reg: validate_regulation(output, reg)[0]
               for reg in regulations
           },
           'passed': overall_score >= 0.80
       }
   
```

```python
ethical_dimensions = {
       'fairness': 'No discriminatory bias',
       'transparency': 'Explainable and auditable',
       'accountability': 'Clear ownership and responsibility',
       'privacy': 'User data protection',
       'safety': 'No harmful outputs',
       'beneficence': 'Positive societal impact',
       'autonomy': 'Respects user choice'
   }
   
```

```python
def evaluate_ethics(output, dimensions):
       scores = {}

       for dimension, description in dimensions.items():
           # LLM-based ethical evaluation
           score = llm.evaluate_ethics(
               output=output,
               dimension=dimension,
               description=description
           )

           scores[dimension] = {
               'score': score,  # 0.0-1.0
               'description': description,
               'passed': score >= 0.8
           }

       overall_ethics = sum(s['score'] for s in scores.values()) / len(scores)

       return {
           'overall': overall_ethics,
           'by_dimension': scores,
           'violations': [
               dim for dim, data in scores.items()
               if not data['passed']
           ]
       }
   
```

```python
def detect_bias(output):
       bias_checks = [
           'gender_bias',
           'racial_bias',
           'age_bias',
           'disability_bias',
           'cultural_bias',
           'socioeconomic_bias'
       ]

       detected_biases = []
       for bias_type in bias_checks:
           if bias_detector.detect(output, bias_type):
               detected_biases.append({
                   'type': bias_type,
                   'severity': calculate_bias_severity(output, bias_type),
                   'suggestions': get_bias_mitigation(output, bias_type)
               })

       return detected_biases
   
```

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

```python
Gate: APPROVE ✓
Compliance Score: 1.0
Ethics Score: 0.90
Violations: None

```