---
name: policy-driven-coding
description: LawBinder-enforced code generation - integrates Constitutional Requirements, security policies, and compliance rules directly into the development process with automated validation gates
---

# Policy-Driven Coding

## Overview

Code without policy creates security holes. Manual compliance is error-prone.

**Core principle:** ALWAYS enforce policy at generation time. Compliance = built-in.

## The Iron Law

```
NO CODE DELIVERY WITHOUT POLICY GATE VALIDATION
Security Score ≥ 0.90 REQUIRED
```

## When to Use

Use for ALL code generation:
- API endpoint development
- Authentication/authorization logic
- Data processing pipelines
- Configuration management
- Infrastructure as code
- Database queries
- Security-critical components

**Use this ESPECIALLY when:**
- Security is critical
- Compliance required (OWASP, SOC2, HIPAA)
- Handling sensitive data
- External-facing APIs
- Production deployments
- Team lacks security expertise

## Three-Layer Enforcement

### Layer 1: Policy Definition (Pre-Generation)

**BEFORE writing code:**

1. **Define Security Policies**
   ```python
   security_policies = {
       'authentication': {
           'required': True,
           'methods': ['jwt', 'oauth2'],
           'forbidden': ['basic_auth', 'api_key_in_url'],
           'rules': [
               'must_validate_token',
               'must_check_expiration',
               'must_verify_signature'
           ]
       },
       'data_access': {
           'encryption': {
               'at_rest': True,
               'in_transit': True,
               'algorithms': ['AES-256', 'RSA-2048']
           },
           'authorization': {
               'required': True,
               'model': 'RBAC',  # Role-Based Access Control
               'rules': ['least_privilege', 'need_to_know']
           }
       },
       'input_validation': {
           'required': True,
           'rules': [
               'sanitize_all_inputs',
               'parameterized_queries',
               'no_eval_exec',
               'validate_types',
               'length_limits'
           ]
       },
       'error_handling': {
           'no_sensitive_info_in_errors': True,
           'log_security_events': True,
           'fail_securely': True
       },
       'dependencies': {
           'vulnerability_scanning': True,
           'approved_packages_only': True,
           'version_pinning': True
       }
   }
   ```

2. **Compliance Requirements**
   ```python
   compliance_requirements = {
       'OWASP_Top_10': [
           'prevent_injection',
           'broken_authentication_prevention',
           'sensitive_data_exposure_prevention',
           'xml_external_entities_prevention',
           'broken_access_control_prevention',
           'security_misconfiguration_prevention',
           'xss_prevention',
           'insecure_deserialization_prevention',
           'using_components_with_known_vulnerabilities_prevention',
           'insufficient_logging_monitoring_prevention'
       ],
       'SOC2': [
           'access_logging',
           'change_tracking',
           'data_encryption',
           'incident_response'
       ],
       'GDPR': [
           'data_minimization',
           'user_consent',
           'right_to_deletion',
           'data_portability'
       ]
   }
   ```

3. **Code Generation Principles**
   ```python
   code_principles = {
       'architecture': 'Clean, modular, testable',
       'patterns': ['dependency_injection', 'repository_pattern'],
       'testing': 'Unit tests required',
       'documentation': 'Inline comments + docstrings',
       'performance': 'O(n log n) max complexity',
       'security_first': True
   }
   ```

**Threshold:** All policies defined before generation

### Layer 2: Policy-Aware Code Generation

**DURING code generation:**

1. **Security Pattern Injection**
   ```python
   def generate_api_endpoint(spec, policies):
       code = []

       # Enforce authentication if required
       if policies['authentication']['required']:
           auth_code = generate_auth_middleware(
               policies['authentication']['methods']
           )
           code.append(auth_code)

       # Enforce input validation
       if policies['input_validation']['required']:
           validation_code = generate_input_validation(
               spec['parameters'],
               policies['input_validation']['rules']
           )
           code.append(validation_code)

       # Enforce authorization
       if policies['data_access']['authorization']['required']:
           authz_code = generate_authorization_check(
               policies['data_access']['authorization']
           )
           code.append(authz_code)

       # Generate business logic
       business_logic = generate_business_logic(spec)
       code.append(business_logic)

       # Enforce error handling
       error_handling = generate_secure_error_handling(
           policies['error_handling']
       )
       code.append(error_handling)

       # Enforce logging
       logging_code = generate_security_logging(
           policies['error_handling']['log_security_events']
       )
       code.append(logging_code)

       return '\n\n'.join(code)
   ```

2. **Automatic Vulnerability Prevention**
   ```python
   vulnerability_checks = {
       'sql_injection': lambda code: check_parameterized_queries(code),
       'xss': lambda code: check_output_encoding(code),
       'command_injection': lambda code: check_no_shell_exec(code),
       'path_traversal': lambda code: check_path_validation(code),
       'xxe': lambda code: check_xml_parser_config(code),
       'insecure_deserialization': lambda code: check_safe_deserialization(code)
   }

   def check_vulnerabilities(generated_code):
       vulnerabilities_found = []

       for vuln_type, check_func in vulnerability_checks.items():
           if not check_func(generated_code):
               vulnerabilities_found.append(vuln_type)

       return vulnerabilities_found

   # During generation
   code = generate_code_with_policies(spec, policies)
   vulns = check_vulnerabilities(code)

   if vulns:
       code = auto_fix_vulnerabilities(code, vulns)
   ```

3. **Compliance Rule Enforcement**
   ```python
   def enforce_compliance(code, requirements):
       violations = []

       for standard, rules in requirements.items():
           for rule in rules:
               if not validate_compliance_rule(code, rule):
                   violations.append({
                       'standard': standard,
                       'rule': rule,
                       'severity': get_rule_severity(rule)
                   })

       # Auto-fix if possible
       for violation in violations:
           if is_auto_fixable(violation['rule']):
               code = apply_compliance_fix(code, violation)
           else:
               raise ComplianceViolationError(violation)

       return code
   ```

**Threshold:** Zero critical vulnerabilities, zero compliance violations

### Layer 3: Post-Generation Security Validation

**AFTER code generation:**

1. **Static Security Analysis**
   ```python
   def run_security_analysis(code):
       results = {
           'sast': run_static_analysis(code),          # SAST tool
           'dependency': check_dependencies(code),      # Dependency scan
           'secrets': scan_for_secrets(code),          # Secret detection
           'complexity': analyze_complexity(code),      # Cyclomatic complexity
           'coverage': estimate_test_coverage(code)     # Test coverage
       }

       security_score = calculate_security_score(results)

       return {
           'score': security_score,
           'results': results,
           'passed': security_score >= 0.90
       }
   ```

2. **Policy Compliance Verification**
   ```python
   def verify_policy_compliance(code, policies):
       compliance_checks = []

       # Authentication check
       if policies['authentication']['required']:
           has_auth = detect_authentication(code)
           compliance_checks.append({
               'category': 'authentication',
               'passed': has_auth,
               'weight': 0.3
           })

       # Input validation check
       if policies['input_validation']['required']:
           has_validation = detect_input_validation(code)
           compliance_checks.append({
               'category': 'input_validation',
               'passed': has_validation,
               'weight': 0.25
           })

       # Encryption check
       if policies['data_access']['encryption']['at_rest']:
           has_encryption = detect_encryption(code)
           compliance_checks.append({
               'category': 'encryption',
               'passed': has_encryption,
               'weight': 0.25
           })

       # Error handling check
       has_secure_errors = detect_secure_error_handling(code)
       compliance_checks.append({
           'category': 'error_handling',
           'passed': has_secure_errors,
           'weight': 0.2
       })

       # Calculate weighted compliance score
       total_weight = sum(c['weight'] for c in compliance_checks)
       compliance_score = sum(
           c['weight'] for c in compliance_checks if c['passed']
       ) / total_weight

       return {
           'score': compliance_score,
           'checks': compliance_checks,
           'passed': compliance_score >= 0.90
       }
   ```

3. **Test Generation for Security**
   ```python
   def generate_security_tests(code, policies):
       tests = []

       # Generate auth tests
       if policies['authentication']['required']:
           tests.extend([
               'test_unauthorized_access_blocked',
               'test_invalid_token_rejected',
               'test_expired_token_rejected'
           ])

       # Generate input validation tests
       if policies['input_validation']['required']:
           tests.extend([
               'test_sql_injection_prevented',
               'test_xss_prevented',
               'test_invalid_input_rejected'
           ])

       # Generate authorization tests
       if policies['data_access']['authorization']['required']:
           tests.extend([
               'test_unauthorized_data_access_blocked',
               'test_role_based_access_enforced'
           ])

       return generate_test_code(tests)
   ```

**Threshold:** Security score ≥ 0.90, compliance score ≥ 0.90

## Integrated Flow

```
Code Specification + Policies
    ↓
[Policy Loading]
    ├─ Security policies
    ├─ Compliance requirements
    └─ Code principles
    ↓
[Policy-Aware Generation]
    ├─ Inject security patterns
    ├─ Auto-prevent vulnerabilities
    ├─ Enforce compliance rules
    └─ Generate business logic
    ↓
[Static Security Analysis]
    ├─ SAST scan
    ├─ Dependency check
    ├─ Secret detection
    ├─ Complexity analysis
    └─ Calculate security score
    ↓
[Policy Compliance Verification]
    ├─ Verify all policy rules
    ├─ Check compliance standards
    └─ Calculate compliance score
    ↓
[Security Test Generation]
    ├─ Auth tests
    ├─ Input validation tests
    └─ Authorization tests
    ↓
[Gate Decision]
    ├─ Security ≥0.90 AND Compliance ≥0.90 → APPROVE
    ├─ Auto-fixable issues → FIX and RE-VALIDATE
    └─ Critical issues → BLOCK
    ↓
OUTPUT: Secure, compliant code + tests + validation report
```

## Red Flags

- "We'll add security later"
- "Skip compliance for MVP"
- "Manual review is enough"
- "Performance over security"
- "Low security score acceptable"

**ALL mean: STOP. Enforce policy-driven coding.**

## Integration

**REQUIRED by:**
- `api-development` - Secure endpoint generation
- `data-pipeline` - Secure data processing
- `infrastructure-as-code` - Secure config generation

**Complementary:**
- `principle-validation` - Constitutional compliance
- `systematic-debugging` - Security bug fixing
- `test-driven-development` - Security test generation

## Example: Secure API Endpoint

**Request:** "Create user profile update endpoint"

**Execution:**

1. **Load Policies:**
   ```python
   policies = load_security_policies()
   compliance = load_compliance_requirements(['OWASP_Top_10', 'GDPR'])
   ```

2. **Generate with Policy Enforcement:**
   ```python
   # Generated code with security patterns
   code = """
   @app.route('/api/users/<user_id>', methods=['PUT'])
   @require_authentication  # Policy: authentication required
   @require_authorization(['user', 'admin'])  # Policy: RBAC
   @validate_input(UserProfileSchema)  # Policy: input validation
   @rate_limit(max_calls=10, period=60)  # Policy: rate limiting
   def update_user_profile(user_id):
       try:
           # Verify user can only update their own profile (or is admin)
           if not (current_user.id == user_id or current_user.is_admin):
               logger.security_event('unauthorized_access_attempt', user_id)
               return jsonify({'error': 'Forbidden'}), 403

           # Validate and sanitize input
           data = request.get_json()
           validated_data = UserProfileSchema().load(data)

           # Use parameterized query (prevent SQL injection)
           db.execute(
               'UPDATE users SET name=?, email=? WHERE id=?',
               (validated_data['name'], validated_data['email'], user_id)
           )

           # Log security event
           logger.security_event('profile_updated', user_id)

           # Don't expose sensitive info
           return jsonify({'success': True}), 200

       except ValidationError as e:
           # Secure error handling
           logger.error('validation_error', str(e))
           return jsonify({'error': 'Invalid input'}), 400

       except Exception as e:
           # Don't leak stack traces
           logger.error('update_failed', str(e))
           return jsonify({'error': 'Update failed'}), 500
   """
   ```

3. **Security Analysis:**
   ```python
   analysis = run_security_analysis(code)
   # {
   #   'sast': {'issues': [], 'score': 1.0},
   #   'dependency': {'vulnerabilities': 0, 'score': 1.0},
   #   'secrets': {'found': 0, 'score': 1.0},
   #   'complexity': {'cyclomatic': 5, 'score': 0.95},
   #   'security_score': 0.99 ✓
   # }
   ```

4. **Compliance Verification:**
   ```python
   compliance = verify_policy_compliance(code, policies)
   # {
   #   'checks': [
   #     {'category': 'authentication', 'passed': True, 'weight': 0.3},
   #     {'category': 'input_validation', 'passed': True, 'weight': 0.25},
   #     {'category': 'authorization', 'passed': True, 'weight': 0.25},
   #     {'category': 'error_handling', 'passed': True, 'weight': 0.2}
   #   ],
   #   'score': 1.0 ✓,
   #   'passed': True
   # }
   ```

5. **Generated Security Tests:**
   ```python
   tests = generate_security_tests(code, policies)
   # - test_unauthorized_access_blocked()
   # - test_invalid_token_rejected()
   # - test_user_cannot_update_other_profiles()
   # - test_sql_injection_prevented()
   # - test_xss_prevented()
   # - test_rate_limiting_enforced()
   ```

**Output:**
- Secure endpoint code ✓
- Security score: 0.99 ✓
- Compliance score: 1.0 ✓
- 6 security tests generated ✓

## Verification Checklist

- [ ] Security policies defined
- [ ] Compliance requirements loaded
- [ ] Authentication enforced (if required)
- [ ] Input validation implemented
- [ ] Authorization checks present
- [ ] Secure error handling
- [ ] Security logging added
- [ ] SAST scan passed
- [ ] Dependency scan passed
- [ ] Secret scan passed
- [ ] Security score ≥ 0.90
- [ ] Compliance score ≥ 0.90
- [ ] Security tests generated
- [ ] No critical vulnerabilities
- [ ] TraceVault logged

## Final Rule

```
Code → Security ≥ 0.90 AND Compliance ≥ 0.90 AND Zero critical vulnerabilities
Otherwise → BLOCK or AUTO-FIX
```

Security is not optional. It's built-in.
