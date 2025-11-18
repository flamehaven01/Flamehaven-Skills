# Algorithms

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

```python
constraints = {
       'time': extract_time_constraint(user_input),      # "urgent", "by tomorrow"
       'quality': extract_quality_constraint(user_input), # "quick draft", "production-ready"
       'format': extract_format_constraint(user_input),   # "markdown", "JSON"
       'length': extract_length_constraint(user_input),   # "brief", "detailed"
       'style': extract_style_constraint(user_input)      # "formal", "casual"
   }
   
```

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

```python
# Confidence < 0.85, trigger clarification
   ASK_USER: "I detected a troubleshooting request. Can you clarify:
   1. Are you experiencing a login problem? (question)
   2. Do you want me to debug the login code? (command/troubleshooting)
   3. Something else?"
   
```

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

```python
ASK_USER: "What specific issue are you seeing with login?
   - Authentication failure
   - Performance issue
   - Error message
   - Other"
   
```

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