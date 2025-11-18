# Examples

**Input:** "Fix the login problem"

**Execution:**

1. **Intent Classification:**
   ```python
   primary_intent: 'troubleshooting'
   confidence: 0.72  # Low - ambiguous
   ambiguity_flag: True
   potential_intents: [
       ('troubleshooting', 0.72),
       ('question', 0.58),  # "What is the login problem?"
       ('command', 0.45)    # "Debug the login code"
   ]
   ```

2. **Ambiguity Resolution:**
   ```python
   # Confidence < 0.85, trigger clarification
   ASK_USER: "I detected a troubleshooting request. Can you clarify:
   1. Are you experiencing a login problem? (question)
   2. Do you want me to debug the login code? (command/troubleshooting)
   3. Something else?"
   ```

3. **User Response:** "Debug the login code"

4. **Re-Classification:**
   ```python
   primary_intent: 'troubleshooting'
   sub_intent: 'code_debugging'
   confidence: 0.94 ✓

   parameters: {
       'artifact': 'login code',
       'issue_type': 'unspecified',
       'severity': 'unspecified'
   }

   missing_params: ['issue_type', 'severity']
   ```

5. **Parameter Request:**
   ```python
   ASK_USER: "What specific issue are you seeing with login?
   - Authentication failure
   - Performance issue
   - Error message
   - Other"
   ```

6. **User Response:** "Users getting 401 errors"

7. **Final Routing:**
   ```python
   intent: 'troubleshooting'
   sub_intent: 'code_debugging'
   confidence: 0.96 ✓

   parameters: {
       'artifact': 'login code',
       'issue_type': 'authentication_failure',
       'error_code': '401'
   }

   route_to: 'systematic-debugging'
   constraints: {
       'focus': 'authentication logic',
       'priority': 'high'
   }
   ```

**Output:** Routed to `systematic-debugging` with full context ✓

