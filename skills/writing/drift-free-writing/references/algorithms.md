# Algorithms

```python
principles = {
       'intent': extract_intent(user_request),
       'tone': identify_tone(context),          # professional, casual, technical
       'audience': identify_audience(context),   # experts, beginners, general
       'constraints': extract_constraints(request), # length, format, keywords
       'requirements': extract_requirements(request) # must-include points
   }

   # Example:
   # {
   #   'intent': 'explain API authentication to developers',
   #   'tone': 'technical but approachable',
   #   'audience': 'mid-level developers',
   #   'constraints': {'length': '800-1000 words', 'format': 'tutorial'},
   #   'requirements': ['OAuth2', 'code examples', 'security best practices']
   # }
   
```

```python
clarity_score = validate_clarity(principles)

   if clarity_score < 0.8:
       ASK_USER_FOR_CLARIFICATION()
   
```

```python
validation_checklist = generate_checklist(principles)

   # Example:
   # - [ ] Explains OAuth2 flow
   # - [ ] Includes 2+ code examples
   # - [ ] Mentions security best practices
   # - [ ] Tone is technical but approachable
   # - [ ] Length 800-1000 words
   
```

```python
required_keywords = extract_keywords(principles['requirements'])

   for keyword in required_keywords:
       if keyword.lower() not in content.lower():
           FLAG_MISSING_KEYWORD(keyword)
   
```

```python
# Length check
   word_count = len(content.split())
   if constraints['length']:
       min_words, max_words = parse_length(constraints['length'])
       if not (min_words <= word_count <= max_words):
           FLAG_LENGTH_VIOLATION()

   # Format check
   if constraints['format'] == 'tutorial':
       if not has_step_by_step_structure(content):
           FLAG_FORMAT_VIOLATION()

   # Required elements
   for requirement in principles['requirements']:
       if requirement not in content:
           FLAG_MISSING_REQUIREMENT(requirement)
   
```

```python
detected_tone = analyze_tone(content)
   expected_tone = principles['tone']

   tone_match = calculate_tone_similarity(detected_tone, expected_tone)

   if tone_match < 0.75:
       FLAG_TONE_MISMATCH()
   
```

```python
prompt = f"""
   Evaluate if this content adheres to the specified principles.

   Principles:
   {json.dumps(principles, indent=2)}

   Content:
   {content}

   Score 0.0-1.0 where:
   - 1.0 = Perfect adherence to all principles
   - 0.9 = Minor deviations, core principles intact
   - 0.7 = Some principles violated
   - 0.5 = Significant drift from intent
   - 0.0 = Complete failure to follow principles

   Provide:
   1. Score (0.0-1.0)
   2. Violations (list any principle violations)
   3. Suggestions (how to improve adherence)
   """

   result = llm.evaluate(prompt)

   if result['score'] < 0.9:
       REFACTOR_WITH_SUGGESTIONS(result['suggestions'])
   
```

```python
# Does the content actually achieve the original intent?
   intent_check = llm.evaluate(f"""
   Original intent: {principles['intent']}
   Content produced: {content}

   Does this content fulfill the original intent? Yes/No and explain.
   """)

   if intent_check['answer'] != 'Yes':
       REFACTOR_TO_FULFILL_INTENT()
   
```

```python
{
  'intent': 'educate readers on topic X',
  'tone': 'conversational yet authoritative',
  'audience': 'general tech-savvy readers',
  'structure': ['intro', 'main_points', 'examples', 'conclusion'],
  'requirements': ['actionable takeaways', 'real-world examples']
}

```

```python
{
  'intent': 'enable developers to implement feature Y',
  'tone': 'precise and technical',
  'audience': 'developers',
  'structure': ['overview', 'prerequisites', 'step-by-step', 'troubleshooting'],
  'requirements': ['code examples', 'API references', 'error handling']
}

```

```python
{
  'intent': 'convert visitors to trial signups',
  'tone': 'compelling and benefit-focused',
  'audience': 'potential customers',
  'structure': ['headline', 'problem', 'solution', 'benefits', 'CTA'],
  'requirements': ['clear value prop', 'social proof', 'strong CTA']
}

```

```python
{
     'intent': 'teach OAuth2 implementation',
     'tone': 'technical but accessible',
     'audience': 'mid-level developers',
     'constraints': {'length': '1000-1200 words', 'format': 'tutorial'},
     'requirements': [
       'explain OAuth2 flow',
       'provide Node.js code example',
       'cover token refresh',
       'mention security best practices'
     ]
   }
   Clarity: 0.91 ✓
   
```

```python
Keywords: ✓ OAuth2, ✓ authorization, ✓ token, ✓ refresh, ✓ security
   Length: 1,087 words ✓ (within 1000-1200)
   Format: ✓ Step-by-step tutorial structure
   Requirements:
     ✓ OAuth2 flow explained
     ✓ Node.js code example (3 code blocks)
     ✓ Token refresh covered (section 4)
     ✓ Security best practices (section 5)
   Tone: Technical but accessible ✓
   Coverage: 100% ✓
   
```

```python
Semantic adherence: 0.94 ✓
   Intent fulfilled: Yes ✓
   Violations: None
   Suggestions: "Consider adding error handling example" (optional)
   
```

```python
D = 0.21 ✓ (OBSERVE - deliver)
   
```