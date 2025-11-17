---
name: sovereign-definition
description: ASDP Intent→Definition→Execution pipeline - compiles natural language intent into formal, executable definitions with governance and validation gates
---

# Sovereign Definition & Intent Compilation

## Overview

Vague intent creates execution drift. Ambiguous definitions waste resources.

**Core principle:** ALWAYS compile intent into formal definition before execution. Clarity = correctness.

## The Iron Law

```
NO EXECUTION WITHOUT FORMAL DEFINITION
Definition Completeness ≥ 0.95 REQUIRED
```

## When to Use

Use for ANY complex task:
- Multi-step workflows
- System design specifications
- Business logic implementation
- Process automation
- Strategic initiatives
- Policy creation
- Architecture decisions

**Use this ESPECIALLY when:**
- Task is complex or multi-faceted
- Multiple stakeholders involved
- Execution cost is high
- Clarity is critical
- Validation required before execution
- Compliance matters

## Three-Layer Compilation

### Layer 1: Intent Extraction (Natural Language → Structured Intent)

**BEFORE formal definition:**

1. **Parse User Intent**
   ```python
   def extract_intent(user_input):
       parsed = {
           'goal': extract_goal(user_input),           # What to achieve
           'constraints': extract_constraints(user_input), # Limitations
           'requirements': extract_requirements(user_input), # Must-haves
           'preferences': extract_preferences(user_input),   # Nice-to-haves
           'context': extract_context(user_input),     # Background info
           'success_criteria': extract_success_criteria(user_input) # How to measure
       }

       return parsed

   # Example:
   # Input: "Build a payment processing system that handles credit cards
   #         and PayPal, must be PCI-DSS compliant, prefer low latency"
   #
   # Output:
   # {
   #   'goal': 'Build payment processing system',
   #   'constraints': ['PCI-DSS compliance required'],
   #   'requirements': ['credit card support', 'PayPal support'],
   #   'preferences': ['low latency'],
   #   'context': 'payment processing',
   #   'success_criteria': ['processes payments', 'meets PCI-DSS', 'latency < 500ms']
   # }
   ```

2. **Ambiguity Detection**
   ```python
   def detect_ambiguity(parsed_intent):
       ambiguities = []

       # Check for vague terms
       vague_terms = ['somehow', 'maybe', 'approximately', 'some', 'good']
       for field, value in parsed_intent.items():
           if any(term in str(value).lower() for term in vague_terms):
               ambiguities.append({
                   'field': field,
                   'type': 'vague_language',
                   'value': value
               })

       # Check for missing critical info
       if not parsed_intent.get('success_criteria'):
           ambiguities.append({
               'field': 'success_criteria',
               'type': 'missing_critical',
               'reason': 'Cannot validate success without criteria'
           })

       # Check for conflicting requirements
       conflicts = detect_conflicts(
           parsed_intent['requirements'],
           parsed_intent['constraints']
       )
       ambiguities.extend(conflicts)

       return ambiguities
   ```

3. **Clarification Request**
   ```python
   if ambiguities:
       for ambiguity in ambiguities:
           if ambiguity['type'] == 'vague_language':
               ASK_USER(f"Can you clarify '{ambiguity['value']}'?")
           elif ambiguity['type'] == 'missing_critical':
               ASK_USER(f"Please specify {ambiguity['field']}")
           elif ambiguity['type'] == 'conflict':
               ASK_USER(f"Requirements conflict: {ambiguity['details']}")
   ```

**Threshold:** Ambiguity count = 0, all critical fields present

### Layer 2: Formal Definition Compilation (Structured Intent → Executable Spec)

**WHEN intent is clear:**

1. **Compile to Formal Definition**
   ```python
   def compile_definition(intent):
       definition = {
           'metadata': {
               'id': generate_unique_id(),
               'version': '1.0',
               'timestamp': utcnow(),
               'intent_hash': hash(intent)
           },
           'specification': {
               'goal': formalize_goal(intent['goal']),
               'inputs': define_inputs(intent),
               'outputs': define_outputs(intent['success_criteria']),
               'constraints': formalize_constraints(intent['constraints']),
               'dependencies': identify_dependencies(intent)
           },
           'execution_plan': {
               'phases': decompose_into_phases(intent),
               'sequence': determine_execution_sequence(intent),
               'resources': estimate_resources(intent),
               'timeline': estimate_timeline(intent)
           },
           'validation': {
               'gates': define_quality_gates(intent),
               'success_criteria': formalize_success_criteria(intent['success_criteria']),
               'compliance_requirements': identify_compliance(intent)
           },
           'governance': {
               'policies': identify_applicable_policies(intent),
               'audit_requirements': define_audit_trail(intent),
               'approval_required': determine_approval_needs(intent)
           }
       }

       return definition
   ```

2. **Decomposition into Phases**
   ```python
   def decompose_into_phases(intent):
       phases = []

       # Phase 1: Discovery/Research
       if requires_research(intent):
           phases.append({
               'name': 'Discovery',
               'tasks': identify_research_tasks(intent),
               'duration': estimate_phase_duration('discovery', intent),
               'outputs': ['requirements_doc', 'technical_spec']
           })

       # Phase 2: Design
       phases.append({
           'name': 'Design',
           'tasks': identify_design_tasks(intent),
           'duration': estimate_phase_duration('design', intent),
           'outputs': ['architecture_diagram', 'api_spec', 'data_model']
       })

       # Phase 3: Implementation
       phases.append({
           'name': 'Implementation',
           'tasks': identify_implementation_tasks(intent),
           'duration': estimate_phase_duration('implementation', intent),
           'outputs': ['working_code', 'unit_tests', 'documentation']
       })

       # Phase 4: Validation
       phases.append({
           'name': 'Validation',
           'tasks': identify_validation_tasks(intent),
           'duration': estimate_phase_duration('validation', intent),
           'outputs': ['test_results', 'compliance_report', 'security_audit']
       })

       # Phase 5: Deployment (if applicable)
       if requires_deployment(intent):
           phases.append({
               'name': 'Deployment',
               'tasks': identify_deployment_tasks(intent),
               'duration': estimate_phase_duration('deployment', intent),
               'outputs': ['deployed_system', 'deployment_report']
           })

       return phases
   ```

3. **Quality Gate Definition**
   ```python
   def define_quality_gates(intent):
       gates = []

       # Discovery gate
       gates.append({
           'phase': 'Discovery',
           'criteria': [
               'requirements_complete',
               'technical_feasibility_validated',
               'risks_identified'
           ],
           'threshold': 'All criteria met'
       })

       # Design gate
       gates.append({
           'phase': 'Design',
           'criteria': [
               'architecture_reviewed',
               'scalability_validated',
               'security_considerations_addressed'
           ],
           'threshold': 'All criteria met'
       })

       # Implementation gate
       gates.append({
           'phase': 'Implementation',
           'criteria': [
               'code_coverage >= 80%',
               'security_scan_passed',
               'drift_score < 0.3',
               'peer_review_approved'
           ],
           'threshold': 'All criteria met'
       })

       # Validation gate
       gates.append({
           'phase': 'Validation',
           'criteria': [
               'all_tests_passed',
               'compliance_verified',
               'performance_benchmarks_met',
               'user_acceptance_complete'
           ],
           'threshold': 'All criteria met'
       })

       return gates
   ```

**Threshold:** Definition completeness ≥ 0.95

### Layer 3: Definition Validation (Formal Check)

**BEFORE execution:**

1. **Completeness Check**
   ```python
   def validate_definition_completeness(definition):
       required_sections = [
           'metadata',
           'specification',
           'execution_plan',
           'validation',
           'governance'
       ]

       missing = []
       for section in required_sections:
           if section not in definition:
               missing.append(section)
           else:
               # Check subsections
               if not validate_section_complete(definition[section], section):
                   missing.append(f"{section} (incomplete)")

       completeness_score = 1.0 - (len(missing) / len(required_sections))

       return {
           'complete': completeness_score >= 0.95,
           'score': completeness_score,
           'missing': missing
       }
   ```

2. **Consistency Check**
   ```python
   def validate_consistency(definition):
       inconsistencies = []

       # Check goal-outputs alignment
       if not outputs_align_with_goal(
           definition['specification']['goal'],
           definition['specification']['outputs']
       ):
           inconsistencies.append({
               'type': 'goal_output_mismatch',
               'details': 'Outputs do not fulfill stated goal'
           })

       # Check resource-timeline feasibility
       if not resources_support_timeline(
           definition['execution_plan']['resources'],
           definition['execution_plan']['timeline']
       ):
           inconsistencies.append({
               'type': 'resource_timeline_conflict',
               'details': 'Timeline not achievable with allocated resources'
           })

       # Check constraint satisfaction
       if not constraints_satisfiable(
           definition['specification']['constraints'],
           definition['execution_plan']
       ):
           inconsistencies.append({
               'type': 'unsatisfiable_constraints',
               'details': 'Execution plan violates constraints'
           })

       return inconsistencies
   ```

3. **Drift Prediction**
   ```python
   def predict_definition_drift(definition, original_intent):
       # Check if formal definition still matches original intent
       drift_indicators = []

       # Goal drift
       if not semantic_similarity(
           original_intent['goal'],
           definition['specification']['goal']
       ) >= 0.9:
           drift_indicators.append('goal_drift')

       # Requirement drift
       original_reqs = set(original_intent['requirements'])
       formal_reqs = extract_requirements_from_definition(definition)
       if not original_reqs.issubset(formal_reqs):
           drift_indicators.append('requirement_drift')

       # Constraint drift
       if constraints_weakened(
           original_intent['constraints'],
           definition['specification']['constraints']
       ):
           drift_indicators.append('constraint_weakening')

       drift_score = len(drift_indicators) / 3  # Normalize

       return {
           'drifted': drift_score >= 0.3,
           'score': drift_score,
           'indicators': drift_indicators
       }
   ```

**Threshold:** Completeness ≥ 0.95, zero inconsistencies, drift < 0.3

## Integrated Flow

```
Natural Language Intent
    ↓
[Intent Extraction]
    ├─ Parse goal, constraints, requirements
    ├─ Detect ambiguities
    └─ Request clarifications
    ↓
[Formal Definition Compilation]
    ├─ Formalize specification
    ├─ Decompose into phases
    ├─ Define quality gates
    └─ Identify governance requirements
    ↓
[Definition Validation]
    ├─ Completeness check (≥0.95)
    ├─ Consistency check
    └─ Drift prediction (<0.3)
    ↓
[Approval Gate]
    ├─ Review definition
    ├─ User confirmation
    └─ Lock definition
    ↓
[Execution with Governance]
    ├─ Execute phase by phase
    ├─ Validate at each gate
    └─ Track against definition
    ↓
OUTPUT: Validated results + compliance report + audit trail
```

## Red Flags

- "Just start coding, we'll figure it out"
- "Definition is overkill"
- "Skip validation, intent is clear"
- "We can change definition mid-execution"
- "Low completeness is fine"

**ALL mean: STOP. Compile formal definition first.**

## Integration

**REQUIRED by:**
- `strategic-consulting` - Strategic initiative definition
- `system-architecture` - Architecture specification
- `complex-workflows` - Multi-step task execution

**Complementary:**
- `intent-classification` - Intent parsing
- `drift-detection` - Definition-execution alignment
- `principle-validation` - Governance enforcement

## Example: Payment System

**User Intent:** "Build a payment processing system that handles credit cards and PayPal, must be PCI-DSS compliant, prefer low latency"

**Execution:**

1. **Intent Extraction:**
   ```python
   intent = {
       'goal': 'Build payment processing system',
       'constraints': ['PCI-DSS compliance mandatory'],
       'requirements': ['credit card processing', 'PayPal integration'],
       'preferences': ['low latency (<500ms)'],
       'context': 'e-commerce platform',
       'success_criteria': [
           'processes payments successfully',
           'PCI-DSS compliant',
           'latency < 500ms p95'
       ]
   }
   Ambiguities: 0 ✓
   ```

2. **Formal Definition:**
   ```python
   definition = {
       'specification': {
           'goal': 'Implement secure payment processing with multi-provider support',
           'inputs': ['payment_method', 'amount', 'currency', 'customer_id'],
           'outputs': ['transaction_id', 'status', 'timestamp'],
           'constraints': [
               'PCI-DSS Level 1 compliance',
               'No storage of raw card data',
               'Tokenization required'
           ]
       },
       'execution_plan': {
           'phases': [
               {
                   'name': 'Discovery',
                   'tasks': ['Review PCI-DSS requirements', 'Evaluate payment gateways'],
                   'duration': '1 week'
               },
               {
                   'name': 'Design',
                   'tasks': ['API design', 'Security architecture', 'Data flow diagram'],
                   'duration': '2 weeks'
               },
               {
                   'name': 'Implementation',
                   'tasks': ['Stripe integration', 'PayPal integration', 'Tokenization'],
                   'duration': '4 weeks'
               },
               {
                   'name': 'Validation',
                   'tasks': ['PCI-DSS audit', 'Performance testing', 'Security testing'],
                   'duration': '2 weeks'
               }
           ]
       },
       'validation': {
           'gates': [
               {'phase': 'Implementation', 'criteria': ['Security scan passed', 'Code review approved']},
               {'phase': 'Validation', 'criteria': ['PCI-DSS audit passed', 'p95 latency < 500ms']}
           ]
       }
   }
   Completeness: 0.98 ✓
   ```

3. **Validation:**
   ```python
   completeness = validate_definition_completeness(definition)
   # {'complete': True, 'score': 0.98, 'missing': []}

   consistency = validate_consistency(definition)
   # [] (no inconsistencies)

   drift = predict_definition_drift(definition, intent)
   # {'drifted': False, 'score': 0.15, 'indicators': []}
   ```

**Output:**
- Formal definition ready ✓
- Completeness: 0.98 ✓
- Drift: 0.15 ✓
- Ready for execution approval

## Verification Checklist

- [ ] Intent extracted from user input
- [ ] Ambiguities detected and resolved
- [ ] All critical fields present
- [ ] Formal definition compiled
- [ ] Phases decomposed
- [ ] Quality gates defined
- [ ] Completeness ≥ 0.95
- [ ] Consistency validated
- [ ] Drift score < 0.3
- [ ] User approval obtained
- [ ] Definition locked
- [ ] TraceVault logged

## Final Rule

```
Execution → Formal definition with completeness ≥ 0.95 AND drift < 0.3
Otherwise → refine definition
```

Definition is the contract between intent and execution.
