# Examples

**Document:** API Reference Guide (45 pages)

**Execution:**

1. **Structural Assessment:**
   ```python
   structural = {
       'metadata': 1.0,      # All fields present
       'hierarchy': 0.92,    # Well-organized, depth=3
       'citations': 0.95,    # All citations formatted consistently
       'graph': 0.89         # High connectivity, balanced
   }
   layer1_score = (0.95 * 0.6) + (0.89 * 0.4) = 0.93
   ```

2. **Textual Assessment:**
   ```python
   textual = {
       'coherence': 0.88,    # Sections flow logically
       'consistency': 0.91,  # No contradictions
       'language': {
           'grammar': 0.96,
           'readability': 0.82,  # Technical but clear
           'clarity': 0.89,
           'conciseness': 0.85
       }
   }
   language_score = 0.89
   layer2_score = (0.88 * 0.3) + (0.91 * 0.3) + (0.89 * 0.4) = 0.89
   ```

3. **Integrity Assessment:**
   ```python
   integrity = {
       'citation_verification': 0.92,  # 23/25 citations verified
       'glossary_score': 0.88,          # 45/51 terms defined
       'merkle_root': '0x7f3a9b2e...'   # Generated ✓
   }
   layer3_score = (0.92 * 0.5) + (0.88 * 0.3) + (1.0 * 0.2) = 0.92
   ```

4. **HSTA Ω Calculation:**
   ```python
   omega = (0.93 * 0.35) + (0.89 * 0.40) + (0.92 * 0.25)
         = 0.3255 + 0.356 + 0.23
         = 0.91 ✓
   ```

**Output:**
- Ω Score: 0.91 ✓
- Classification: Excellent
- Action: ACCEPT for citation
- Merkle Root: 0x7f3a9b2e...
- Glossary: 45 terms extracted

