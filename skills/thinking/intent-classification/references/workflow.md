### Layer 1: Intent Category Detection

**BEFORE execution:**

1. **Primary Intent Categories**
   ```python
   intent_categories = {
       'question': 'Seeking information/explanation',
       'command': 'Request for action/execution',
       'creation': 'Generate new content/artifact',
       'analysis': 'Evaluate/assess existing data',
       'navigation': 'Find/locate resource',
       'configuration': 'Modify settings/preferences',
       'troubleshooting': 'Diagnose/fix problem',
       'collaboration': 'Multi-party interaction',
       'validation': 'Verify/check correctness'
   }
   ```

2. **Intent Detection Algorithm**
   ```python
   def classify_intent(user_input):
       # Multi-signal classification
       signals = {
           'keywords': extract_intent_keywords(user_input),
           'syntax': analyze_sentence_structure(user_input),
           'context': retrieve_conversation_history(),
           'entities': extract_named_entities(user_input)
       }

       # LLM-based classification
       classification = llm.classify(
           input=user_input,
           signals=signals,
           categories=intent_categories
       )

       return {
           'primary': classification['category'],
           'confidence': classification['confidence'],
           'secondary': classification.get('secondary_intents', []),
           'ambiguity_flag': classification['confidence'] < 0.85
       }
   ```

3. **Confidence Scoring**
   ```python
   # Factors affecting confidence
   confidence = calculate_confidence(
       keyword_match_strength=0.3,      # Clear intent keywords present
       syntax_clarity=0.25,             # Unambiguous sentence structure
       context_consistency=0.25,        # Aligns with conversation history
       entity_completeness=0.2          # All required entities present
   )

   if confidence < 0.85:
       REQUEST_CLARIFICATION()
   ```

**Threshold:** Confidence ≥ 0.85 required



### Layer 2: Sub-Intent & Parameter Extraction

**WHEN primary intent classified:**

1. **Sub-Intent Taxonomy**
   ```python
   # Example: 'creation' intent has sub-intents
   creation_sub_intents = {
       'code_generation': ['write function', 'implement', 'create script'],
       'content_writing': ['write blog', 'draft email', 'compose'],
       'document_generation': ['create report', 'generate documentation'],
       'data_creation': ['generate dataset', 'create mock data'],
       'design_creation': ['design UI', 'create mockup']
   }
   ```

2. **Parameter Extraction**
   ```python
   def extract_parameters(user_input, intent):
       required_params = get_required_params(intent)
       optional_params = get_optional_params(intent)

       extracted = {}
       missing = []

       for param in required_params:
           value = extract_param_value(user_input, param)
           if value:
               extracted[param] = value
           else:
               missing.append(param)

       if missing:
           REQUEST_MISSING_PARAMS(missing)

       # Optional parameters
       for param in optional_params:
           value = extract_param_value(user_input, param)
           if value:
               extracted[param] = value

       return extracted

   # Example:
   # Intent: code_generation
   # Input: "Write a Python function to sort a list"
   # Extracted: {
   #   'language': 'Python',
   #   'artifact_type': 'function',
   #   'functionality': 'sort a list',
   #   'requirements': [] # missing - might ask user
   # }
   ```

3. **Constraint Identification**
   ```python
   constraints = {
       'time': extract_time_constraint(user_input),      # "urgent", "by tomorrow"
       'quality': extract_quality_constraint(user_input), # "quick draft", "production-ready"
       'format': extract_format_constraint(user_input),   # "markdown", "JSON"
       'length': extract_length_constraint(user_input),   # "brief", "detailed"
       'style': extract_style_constraint(user_input)      # "formal", "casual"
   }
   ```

**Threshold:** All required parameters extracted or requested



### Layer 3: Execution Path Routing

**WHEN intent + parameters complete:**

1. **Route Decision Matrix**
   ```python
   routing_matrix = {
       ('question', 'factual'): 'sovereign-search',
       ('question', 'opinion'): 'llm-direct',
       ('command', 'system'): 'bash-execution',
       ('command', 'ai'): 'agent-task',
       ('creation', 'code'): 'code-generation',
       ('creation', 'content'): 'drift-free-writing',
       ('creation', 'academic'): 'academic-writing',
       ('analysis', 'data'): 'data-analysis-agent',
       ('analysis', 'sentiment'): 'sentiment-analysis',
       ('validation', 'drift'): 'drift-detection',
       ('validation', 'fact'): 'fact-checking',
       ('troubleshooting', 'code'): 'systematic-debugging',
       ('troubleshooting', 'system'): 'diagnostic-agent'
   }

   def route_request(intent, sub_intent, constraints):
       key = (intent, sub_intent)
       execution_path = routing_matrix.get(key)

       if not execution_path:
           execution_path = select_default_path(intent)

       # Apply constraints to execution path
       execution_config = configure_execution(
           path=execution_path,
           constraints=constraints
       )

       return execution_config
   ```

2. **Multi-Intent Handling**
   ```python
   # If multiple intents detected
   if len(classified_intents) > 1:
       # Prioritize by confidence
       sorted_intents = sorted(
           classified_intents,
           key=lambda x: x['confidence'],
           reverse=True
       )

       primary = sorted_intents[0]
       secondary = sorted_intents[1:]

       # Ask user which to prioritize
       if primary['confidence'] - secondary[0]['confidence'] < 0.1:
           ASK_USER_PRIORITY(primary, secondary)
       else:
           EXECUTE_PRIMARY(primary)
           QUEUE_SECONDARY(secondary)
   ```

3. **Fallback Strategy**
   ```python
   if confidence < 0.85:
       fallback_strategies = [
           'ask_clarification',           # Best: get user input
           'show_intent_options',         # Show likely intents
           'execute_with_confirmation',   # Execute but ask to confirm
           'default_safe_path'            # Most conservative execution
       ]

       strategy = select_fallback_strategy(
           confidence_score=confidence,
           risk_level=calculate_risk(intent),
           user_preferences=get_user_preferences()
       )

       execute_fallback(strategy)
   ```

**Threshold:** Route confidence ≥ 0.85 or fallback engaged

## Integrated Flow

```
User Input
    ↓
[Intent Category Detection]
    ├─ Primary intent (9 categories)
    ├─ Confidence scoring
    └─ Ambiguity detection
    ↓
[Sub-Intent & Parameters]
    ├─ Sub-intent classification
    ├─ Required parameter extraction
    └─ Constraint identification
    ↓
[Execution Path Routing]
    ├─ Route decision matrix
    ├─ Multi-intent handling
    └─ Fallback strategy (if needed)
    ↓
[Execution with Validation]
    ├─ Route to appropriate skill
    ├─ Apply constraints
    └─ Track execution
    ↓
OUTPUT: Correctly routed execution + confidence metadata
```

## Red Flags

- "Just guess the intent"
- "Execute first, classify later"
- "Low confidence is fine"
- "Skip parameter extraction"
- "Ignore ambiguity"

**ALL mean: STOP. Run full classification.**

## Integration

**REQUIRED by:**
- `multi-agent-orchestration` - Task delegation
- `chatbot-interaction` - Message routing
- `api-gateway` - Request routing

**Complementary:**
- `drift-detection` - Validate intent preservation
- `self-validation` - AI decision verification
- `principle-validation` - Policy compliance check

## Example: Ambiguous Request

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

## Verification Checklist

- [ ] Primary intent classified
- [ ] Confidence score ≥ 0.85 (or clarification requested)
- [ ] Sub-intent identified
- [ ] Required parameters extracted
- [ ] Constraints identified
- [ ] Execution path determined
- [ ] Ambiguity resolved (if detected)
- [ ] Fallback strategy applied (if needed)
- [ ] Route confidence validated
- [ ] TraceVault logged

## Final Rule

```
Execution → Intent classified with confidence ≥ 0.85 AND all parameters extracted
Otherwise → request clarification
```

Correct routing prevents wasted execution.