# Examples

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

