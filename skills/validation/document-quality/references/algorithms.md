# Algorithms

```python
def parse_document_structure(document):
       structure = {
           'metadata': extract_metadata(document),
           'hierarchy': {
               'title': extract_title(document),
               'sections': extract_sections(document),
               'subsections': extract_subsections(document),
               'depth': calculate_hierarchy_depth(document)
           },
           'elements': {
               'headings': count_headings(document),
               'paragraphs': count_paragraphs(document),
               'lists': count_lists(document),
               'tables': count_tables(document),
               'figures': count_figures(document),
               'code_blocks': count_code_blocks(document)
           },
           'citations': {
               'count': count_citations(document),
               'format': detect_citation_format(document),
               'bibliography': extract_bibliography(document)
           }
       }

       return structure
   
```

```python
def score_structural_completeness(structure):
       scores = {}

       # Metadata completeness
       required_metadata = ['title', 'author', 'date', 'version']
       metadata_present = sum(
           1 for field in required_metadata
           if field in structure['metadata']
       )
       scores['metadata'] = metadata_present / len(required_metadata)

       # Hierarchy completeness
       has_title = 'title' in structure['hierarchy']
       has_sections = len(structure['hierarchy']['sections']) > 0
       hierarchy_depth = structure['hierarchy']['depth']
       scores['hierarchy'] = (
           (1.0 if has_title else 0.0) +
           (1.0 if has_sections else 0.0) +
           (min(hierarchy_depth / 3, 1.0))  # Ideal depth: 3 levels
       ) / 3

       # Citation integrity
       if structure['citations']['count'] > 0:
           has_bibliography = structure['citations']['bibliography'] is not None
           format_consistent = check_citation_format_consistency(
               structure['citations']
           )
           scores['citations'] = (
               (1.0 if has_bibliography else 0.5) +
               (1.0 if format_consistent else 0.5)
           ) / 2
       else:
           scores['citations'] = 1.0  # No citations required = OK

       # Overall structural score
       structural_score = (
           scores['metadata'] * 0.3 +
           scores['hierarchy'] * 0.5 +
           scores['citations'] * 0.2
       )

       return structural_score, scores
   
```

```python
def analyze_document_graph(structure):
       # Build document graph (sections → subsections → paragraphs)
       graph = build_document_graph(structure)

       properties = {
           'connectivity': calculate_connectivity(graph),
           'balance': calculate_balance(graph),
           'coherence': calculate_coherence(graph)
       }

       # Connectivity: Are all sections reachable?
       # Balance: Is content evenly distributed?
       # Coherence: Do sections flow logically?

       graph_score = (
           properties['connectivity'] * 0.4 +
           properties['balance'] * 0.3 +
           properties['coherence'] * 0.3
       )

       return graph_score, properties
   
```

```python
def analyze_semantic_coherence(document):
       sections = extract_sections(document)
       coherence_scores = []

       for i in range(len(sections) - 1):
           current = sections[i]
           next_section = sections[i + 1]

           # Semantic similarity between consecutive sections
           similarity = calculate_semantic_similarity(
               current['content'],
               next_section['content']
           )

           # Should be related but not redundant
           if 0.3 <= similarity <= 0.7:
               coherence_scores.append(1.0)
           elif 0.2 <= similarity < 0.3 or 0.7 < similarity <= 0.8:
               coherence_scores.append(0.7)
           else:
               coherence_scores.append(0.3)

       return sum(coherence_scores) / len(coherence_scores) if coherence_scores else 0.5
   
```

```python
def check_logical_consistency(document):
       claims = extract_claims(document)
       evidence = extract_evidence(document)

       consistency_checks = []

       for claim in claims:
           # Does claim have supporting evidence?
           supporting_evidence = find_supporting_evidence(claim, evidence)
           if supporting_evidence:
               consistency_checks.append(1.0)
           else:
               consistency_checks.append(0.0)

           # Are there contradictions?
           contradictions = find_contradictions(claim, document)
           if contradictions:
               consistency_checks.append(0.0)
           else:
               consistency_checks.append(1.0)

       return sum(consistency_checks) / len(consistency_checks) if consistency_checks else 0.5
   
```

```python
def assess_language_quality(document):
       text = extract_text(document)

       quality = {
           'grammar': run_grammar_check(text),        # 0.0-1.0
           'readability': calculate_readability(text), # Flesch score
           'clarity': assess_clarity(text),            # Technical clarity
           'conciseness': calculate_conciseness(text)  # Avoid redundancy
       }

       # Normalize readability (Flesch 60-80 = ideal)
       quality['readability'] = normalize_readability(quality['readability'])

       language_score = (
           quality['grammar'] * 0.3 +
           quality['readability'] * 0.3 +
           quality['clarity'] * 0.2 +
           quality['conciseness'] * 0.2
       )

       return language_score, quality
   
```

```python
def verify_citations(document):
       citations = extract_citations(document)
       verification_results = []

       for citation in citations:
           result = {
               'citation': citation,
               'exists': False,
               'accessible': False,
               'matches_claim': False
           }

           # Check if citation exists
           try:
               source = retrieve_source(citation)
               result['exists'] = True

               # Check if accessible
               if source.accessible:
                   result['accessible'] = True

                   # Check if supports claim
                   claim = find_claim_for_citation(citation, document)
                   if verify_claim_support(claim, source):
                       result['matches_claim'] = True

           except SourceNotFoundError:
               result['exists'] = False

           verification_results.append(result)

       # Calculate verification score
       if not verification_results:
           return 1.0  # No citations = OK

       verified_count = sum(
           1 for r in verification_results
           if r['exists'] and r['accessible'] and r['matches_claim']
       )

       return verified_count / len(verification_results)
   
```

```python
def generate_merkle_root(document):
       # Create Merkle tree for tamper detection
       sections = extract_sections(document)
       hashes = []

       for section in sections:
           section_hash = sha256(section['content'].encode()).hexdigest()
           hashes.append(section_hash)

       # Build Merkle tree
       merkle_tree = build_merkle_tree(hashes)
       merkle_root = merkle_tree.root

       return {
           'merkle_root': merkle_root,
           'section_hashes': hashes,
           'timestamp': utcnow(),
           'version': document.get('version', '1.0')
       }
   
```

```python
def extract_glossary(document):
       # Extract domain-specific terms
       terms = extract_technical_terms(document)
       glossary = []

       for term in terms:
           definition = extract_definition(term, document)
           if definition:
               glossary.append({
                   'term': term,
                   'definition': definition,
                   'first_occurrence': find_first_occurrence(term, document),
                   'frequency': count_occurrences(term, document)
               })

       # Score glossary completeness
       technical_terms_count = len(terms)
       defined_terms_count = len(glossary)

       glossary_score = (
           defined_terms_count / technical_terms_count
           if technical_terms_count > 0
           else 1.0
       )

       return glossary, glossary_score
   
```

```python
def calculate_hsta_omega(document):
    # Layer 1: Structural
    structural_score, structural_details = score_structural_completeness(
        parse_document_structure(document)
    )
    graph_score, graph_properties = analyze_document_graph(
        parse_document_structure(document)
    )

    layer1_score = (structural_score * 0.6 + graph_score * 0.4)

    # Layer 2: Textual
    coherence_score = analyze_semantic_coherence(document)
    consistency_score = check_logical_consistency(document)
    language_score, language_details = assess_language_quality(document)

    layer2_score = (
        coherence_score * 0.3 +
        consistency_score * 0.3 +
        language_score * 0.4
    )

    # Layer 3: Integrity
    citation_verification = verify_citations(document)
    merkle_data = generate_merkle_root(document)
    glossary, glossary_score = extract_glossary(document)

    layer3_score = (
        citation_verification * 0.5 +
        glossary_score * 0.3 +
        1.0 * 0.2  # Merkle root generated (binary: yes=1.0)
    )

    # Final Ω score (weighted average)
    omega = (
        layer1_score * 0.35 +  # Structure = 35%
        layer2_score * 0.40 +  # Text quality = 40%
        layer3_score * 0.25    # Integrity = 25%
    )

    return {
        'omega': omega,
        'layers': {
            'structural': layer1_score,
            'textual': layer2_score,
            'integrity': layer3_score
        },
        'details': {
            'structural': structural_details,
            'graph': graph_properties,
            'language': language_details,
            'citation_verification': citation_verification,
            'glossary_completeness': glossary_score
        },
        'merkle_root': merkle_data['merkle_root'],
        'glossary': glossary,
        'passed': omega >= 0.90
    }

```

```python
structural = {
       'metadata': 1.0,      # All fields present
       'hierarchy': 0.92,    # Well-organized, depth=3
       'citations': 0.95,    # All citations formatted consistently
       'graph': 0.89         # High connectivity, balanced
   }
   layer1_score = (0.95 * 0.6) + (0.89 * 0.4) = 0.93
   
```

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

```python
integrity = {
       'citation_verification': 0.92,  # 23/25 citations verified
       'glossary_score': 0.88,          # 45/51 terms defined
       'merkle_root': '0x7f3a9b2e...'   # Generated ✓
   }
   layer3_score = (0.92 * 0.5) + (0.88 * 0.3) + (1.0 * 0.2) = 0.92
   
```

```python
omega = (0.93 * 0.35) + (0.89 * 0.40) + (0.92 * 0.25)
         = 0.3255 + 0.356 + 0.23
         = 0.91 ✓
   
```