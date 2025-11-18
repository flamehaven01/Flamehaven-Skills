### Tier 1: Principle Extraction (Pre-Writing)

**BEFORE starting to write:**

1. **Extract Writing Principles**
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

2. **Validate Principle Clarity**
   ```python
   clarity_score = validate_clarity(principles)

   if clarity_score < 0.8:
       ASK_USER_FOR_CLARIFICATION()
   ```

3. **Create Validation Checklist**
   ```python
   validation_checklist = generate_checklist(principles)

   # Example:
   # - [ ] Explains OAuth2 flow
   # - [ ] Includes 2+ code examples
   # - [ ] Mentions security best practices
   # - [ ] Tone is technical but approachable
   # - [ ] Length 800-1000 words
   ```

**Threshold:** Clarity ≥ 0.8 required before writing



### Tier 2: Shallow Validation (Post-Writing)

**IMMEDIATELY after writing:**

1. **Keyword Matching**
   ```python
   required_keywords = extract_keywords(principles['requirements'])

   for keyword in required_keywords:
       if keyword.lower() not in content.lower():
           FLAG_MISSING_KEYWORD(keyword)
   ```

2. **Constraint Verification**
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

3. **Tone Consistency**
   ```python
   detected_tone = analyze_tone(content)
   expected_tone = principles['tone']

   tone_match = calculate_tone_similarity(detected_tone, expected_tone)

   if tone_match < 0.75:
       FLAG_TONE_MISMATCH()
   ```

**Threshold:** ≥ 80% principle coverage required



### Tier 3: Deep LLM Validation (Semantic Check)

**WHEN Tier 2 passes:**

1. **Semantic Adherence Evaluation**
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

2. **Intent Preservation Check**
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

**Threshold:** LLM score ≥ 0.9 required

## Integrated Flow

```
User Request
    ↓
[Principle Extraction]
    ├─ Extract intent, tone, audience
    ├─ Identify constraints
    └─ List requirements
    ↓
[Content Generation]
    ├─ Write with principles in mind
    └─ Follow validation checklist
    ↓
[Shallow Validation]
    ├─ Keyword matching (100%)
    ├─ Constraint verification
    └─ Tone consistency check
    ↓
[Deep LLM Validation]
    ├─ Semantic adherence (≥0.9)
    └─ Intent preservation
    ↓
[Drift Score Calculation]
    ├─ If attention available: D < 0.3
    └─ Else: rely on Shallow + Deep
    ↓
OUTPUT: Validated content + adherence report
```

## Common Writing Patterns

### Pattern 1: Blog Post

**Principles:**
```python
{
  'intent': 'educate readers on topic X',
  'tone': 'conversational yet authoritative',
  'audience': 'general tech-savvy readers',
  'structure': ['intro', 'main_points', 'examples', 'conclusion'],
  'requirements': ['actionable takeaways', 'real-world examples']
}
```

**Validation:**
- ✓ Intro hooks reader
- ✓ 3+ main points covered
- ✓ 2+ real-world examples
- ✓ Actionable takeaways listed
- ✓ Tone conversational
- ✓ Drift D < 0.3

### Pattern 2: Technical Documentation

**Principles:**
```python
{
  'intent': 'enable developers to implement feature Y',
  'tone': 'precise and technical',
  'audience': 'developers',
  'structure': ['overview', 'prerequisites', 'step-by-step', 'troubleshooting'],
  'requirements': ['code examples', 'API references', 'error handling']
}
```

**Validation:**
- ✓ Prerequisites listed
- ✓ Step-by-step instructions
- ✓ Code examples working
- ✓ API references linked
- ✓ Error handling covered
- ✓ Tone technical
- ✓ Drift D < 0.3

### Pattern 3: Marketing Copy

**Principles:**
```python
{
  'intent': 'convert visitors to trial signups',
  'tone': 'compelling and benefit-focused',
  'audience': 'potential customers',
  'structure': ['headline', 'problem', 'solution', 'benefits', 'CTA'],
  'requirements': ['clear value prop', 'social proof', 'strong CTA']
}
```

**Validation:**
- ✓ Headline compelling
- ✓ Problem resonates
- ✓ Solution clear
- ✓ Benefits quantified
- ✓ Social proof included
- ✓ CTA actionable
- ✓ Drift D < 0.3

## Red Flags

- "Just write it, we'll check later"
- "Close enough to the requirements"
- "Tone doesn't matter that much"
- "Skip validation for short content"
- "We can fix drift in revision"

**ALL mean: STOP. Run full validation.**

## Integration

**REQUIRED by:**
- `academic-writing` - Scholarly content validation
- `documentation-generation` - Technical writing
- `content-marketing` - Brand consistency

**Complementary:**
- `drift-detection` - Core validation framework
- `structured-output` - Template-based content
- `self-validation` - AI output verification

## Example: API Tutorial

**Request:** "Write a tutorial on OAuth2 implementation for developers"

**Execution:**

1. **Principles:**
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

2. **Content Generated:** (1,087 words)
   ```
   # OAuth2 Implementation Guide

   OAuth2 is an authorization framework...
   [full tutorial content]
   ...Always validate tokens and use HTTPS.
   ```

3. **Shallow Validation:**
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

4. **Deep LLM Validation:**
   ```python
   Semantic adherence: 0.94 ✓
   Intent fulfilled: Yes ✓
   Violations: None
   Suggestions: "Consider adding error handling example" (optional)
   ```

5. **Drift Score:**
   ```python
   D = 0.21 ✓ (OBSERVE - deliver)
   ```

**Output:** Tutorial delivered with 100% principle adherence ✓

## Verification Checklist

- [ ] Principles extracted (clarity ≥ 0.8)
- [ ] Validation checklist created
- [ ] Content generated
- [ ] Keywords present (≥80%)
- [ ] Constraints verified
- [ ] Tone consistent (≥0.75 match)
- [ ] LLM semantic score ≥ 0.9
- [ ] Intent preservation confirmed
- [ ] Drift score D < 0.3 (if available)
- [ ] No red flags triggered
- [ ] TraceVault logged

## Final Rule

```
Content → Principles validated AND Drift D < 0.3 AND LLM score ≥ 0.9
Otherwise → refactor until compliant
```

Writing is not done until validation passes.