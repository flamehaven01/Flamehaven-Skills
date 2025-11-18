# Examples

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

