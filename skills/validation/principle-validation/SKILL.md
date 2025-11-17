---
name: principle-validation
description: LawBinder policy enforcement - validates AI outputs against Constitutional Requirements, regulatory policies, and ethical guidelines with automated compliance scoring
---

# Principle Validation & Policy Enforcement

## Overview

Output without policy check is risk. Compliance without automation is slow.

**Core principle:** ALWAYS validate against Constitutional Requirements before delivery. Governance = mandatory.

## The Iron Law

```
NO OUTPUT DELIVERY WITHOUT LAWBINDER VALIDATION
Compliance Score ≥ 0.80 REQUIRED
```

## When to Use

Use for ANY AI output:
- Code generation
- Content creation
- Strategic decisions
- Academic papers
- API responses
- User-facing communications
- Data processing pipelines

**Use this ESPECIALLY when:**
- Constitutional Requirements defined
- Regulatory compliance required (GDPR, HIPAA, SOC2)
- Ethical considerations present
- High-stakes decisions
- External publication
- User data involved

## Three-Layer Validation

### Layer 1: Constitutional Requirements Check

**BEFORE output delivery:**

1. **Load Constitutional Principles**
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

2. **Forbidden Content Detection**
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

3. **Required Elements Check**
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

**Threshold:** Zero forbidden violations, all required elements present

### Layer 2: Regulatory Compliance Check

**WHEN constitutional check passes:**

1. **Identify Applicable Regulations**
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

2. **Regulation-Specific Validation**
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

3. **Compliance Scoring**
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

**Threshold:** Compliance score ≥ 0.80

### Layer 3: Ethical Alignment Check

**WHEN regulatory compliance passes:**

1. **Ethical Dimensions**
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

2. **Ethical Scoring**
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

3. **Bias Detection**
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

**Threshold:** Ethics score ≥ 0.80, zero high-severity biases

## Integrated Flow

```
AI Output
    ↓
[Constitutional Check]
    ├─ Forbidden content detection
    ├─ Required elements verification
    └─ Values alignment check
    ↓
[Regulatory Compliance]
    ├─ Identify applicable regulations
    ├─ Execute regulation-specific checks
    └─ Calculate compliance score
    ↓
[Ethical Alignment]
    ├─ Evaluate ethical dimensions
    ├─ Detect biases
    └─ Calculate ethics score
    ↓
[Final Gate Decision]
    ├─ Constitutional: PASS/BLOCK
    ├─ Compliance: ≥0.80 required
    └─ Ethics: ≥0.80 required
    ↓
OUTPUT: Validated output + compliance report OR BLOCKED with violations
```

## Gate Decision Matrix

| Constitutional | Compliance | Ethics | Action |
|----------------|------------|--------|--------|
| ✓ | ≥0.80 | ≥0.80 | **APPROVE** |
| ✓ | ≥0.80 | <0.80 | **REFACTOR** (ethics) |
| ✓ | <0.80 | * | **REFACTOR** (compliance) |
| ✗ | * | * | **BLOCK** (critical violation) |

## Red Flags

- "Skip policy check for internal use"
- "Compliance doesn't apply here"
- "Ethics is subjective, ignore it"
- "We'll validate later"
- "Low compliance score is acceptable"

**ALL mean: STOP. Run full validation.**

## Integration

**REQUIRED by:**
- `academic-writing` - IRB and regulatory compliance
- `code-generation` - Security and policy adherence
- `content-creation` - Brand and ethical alignment

**Complementary:**
- `drift-detection` - Principle preservation
- `self-validation` - AI conscience check
- `fact-checking` - Information accuracy

## Example: User Data Processing Code

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

## Verification Checklist

- [ ] Constitutional principles loaded
- [ ] Forbidden content check passed
- [ ] Required elements present
- [ ] Applicable regulations identified
- [ ] Regulation-specific checks executed
- [ ] Compliance score ≥ 0.80
- [ ] Ethical dimensions evaluated
- [ ] Ethics score ≥ 0.80
- [ ] Bias detection completed
- [ ] No high-severity biases detected
- [ ] Gate decision documented
- [ ] TraceVault logged

## Final Rule

```
Output → Constitutional PASS AND Compliance ≥ 0.80 AND Ethics ≥ 0.80
Otherwise → BLOCK or REFACTOR
```

Compliance is not optional. It's a gate.
