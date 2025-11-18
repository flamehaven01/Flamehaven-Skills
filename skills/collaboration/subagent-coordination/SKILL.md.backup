---
name: subagent-coordination
description: Multi-agent orchestration with governance - coordinates parallel execution, task delegation, and result synthesis while maintaining Constitutional Requirements and drift control
---

# Subagent Coordination & Multi-Agent Orchestration

## Overview

Single-agent execution is slow. Uncoordinated agents create chaos.

**Core principle:** ALWAYS orchestrate with governance. Parallelism = controlled.

## The Iron Law

```
NO MULTI-AGENT EXECUTION WITHOUT COORDINATION PROTOCOL
Coordination Confidence ≥ 0.85 REQUIRED
```

## When to Use

Use for ANY parallelizable task:
- Independent research tasks
- Multi-file code generation
- Parallel data processing
- Distributed testing
- Multi-perspective analysis
- Concurrent document generation
- Complex workflow execution

**Use this ESPECIALLY when:**
- Tasks can run in parallel
- Execution time is critical
- Multiple specializations needed
- Resource utilization matters
- Dependencies are manageable
- Results need synthesis

## Three-Layer Coordination

### Layer 1: Task Decomposition (Identify Parallelizable Work)

**BEFORE agent spawn:**

1. **Analyze Task Structure**
   ```python
   def analyze_task_dependencies(task):
       subtasks = decompose_task(task)
       dependency_graph = build_dependency_graph(subtasks)

       analysis = {
           'total_subtasks': len(subtasks),
           'parallelizable': [],
           'sequential': [],
           'critical_path': find_critical_path(dependency_graph),
           'estimated_speedup': calculate_speedup(dependency_graph)
       }

       for subtask in subtasks:
           dependencies = get_dependencies(subtask, dependency_graph)
           if not dependencies:
               analysis['parallelizable'].append(subtask)
           else:
               analysis['sequential'].append({
                   'subtask': subtask,
                   'depends_on': dependencies
               })

       return analysis

   # Example:
   # Task: "Implement user authentication system"
   # Analysis:
   # {
   #   'total_subtasks': 5,
   #   'parallelizable': [
   #     'Design database schema',
   #     'Research OAuth providers',
   #     'Write security policy'
   #   ],
   #   'sequential': [
   #     {'subtask': 'Implement auth logic', 'depends_on': ['database schema']},
   #     {'subtask': 'Write tests', 'depends_on': ['auth logic']}
   #   ],
   #   'critical_path': ['database schema', 'auth logic', 'tests'],
   #   'estimated_speedup': 2.1  # 2.1x faster with parallelization
   # }
   ```

2. **Agent Specification**
   ```python
   def specify_agents(subtasks, constitutional_requirements):
       agents = []

       for subtask in subtasks:
           agent_spec = {
               'id': generate_agent_id(),
               'task': subtask,
               'specialization': determine_specialization(subtask),
               'resources': estimate_resources(subtask),
               'timeout': estimate_timeout(subtask),
               'constitutional_requirements': constitutional_requirements,
               'validation_gates': define_validation_gates(subtask),
               'communication': {
                   'report_frequency': determine_reporting(subtask),
                   'result_schema': define_output_schema(subtask)
               }
           }
           agents.append(agent_spec)

       return agents

   # Example agent spec:
   # {
   #   'id': 'agent_001',
   #   'task': 'Design database schema',
   #   'specialization': 'database-design',
   #   'resources': {'memory': '2GB', 'cpu': '1 core'},
   #   'timeout': '5 minutes',
   #   'constitutional_requirements': {...},
   #   'validation_gates': ['schema_valid', 'normalized', 'indexed'],
   #   'communication': {
   #     'report_frequency': 'on_completion',
   #     'result_schema': 'database_schema_v1'
   #   }
   # }
   ```

3. **Coordination Protocol**
   ```python
   coordination_protocol = {
       'execution_mode': 'parallel',  # or 'sequential', 'hybrid'
       'synchronization_points': identify_sync_points(dependency_graph),
       'conflict_resolution': 'coordinator_arbitration',
       'error_handling': {
           'retry_strategy': 'exponential_backoff',
           'max_retries': 3,
           'fallback': 'coordinator_takeover'
       },
       'result_aggregation': {
           'method': 'merge_with_validation',
           'schema': define_aggregate_schema()
       }
   }
   ```

**Threshold:** Clear task decomposition, all dependencies mapped

### Layer 2: Agent Orchestration (Spawn, Monitor, Coordinate)

**DURING execution:**

1. **Agent Spawning**
   ```python
   def spawn_agents(agent_specs, coordination_protocol):
       active_agents = []

       # Spawn parallelizable agents first
       for spec in agent_specs:
           if not spec.get('dependencies'):
               agent = spawn_agent(
                   spec=spec,
                   protocol=coordination_protocol
               )
               active_agents.append(agent)

       # Monitor and spawn dependent agents when ready
       while not all_tasks_complete(active_agents):
           # Check for completed agents
           completed = [a for a in active_agents if a.status == 'complete']

           # Check if new agents can be spawned
           for spec in agent_specs:
               if spec not in spawned and dependencies_met(spec, completed):
                   agent = spawn_agent(spec, coordination_protocol)
                   active_agents.append(agent)

           # Wait for next update
           await asyncio.sleep(coordination_protocol['poll_interval'])

       return active_agents
   ```

2. **Real-Time Monitoring**
   ```python
   def monitor_agents(active_agents):
       monitoring_data = {
           'timestamp': utcnow(),
           'agents': []
       }

       for agent in active_agents:
           agent_status = {
               'id': agent.id,
               'task': agent.task,
               'status': agent.status,  # 'running', 'complete', 'error', 'stalled'
               'progress': agent.progress,  # 0.0 - 1.0
               'drift_score': agent.drift_score,
               'validation_gates_passed': agent.gates_passed,
               'resource_usage': {
                   'cpu': agent.cpu_usage,
                   'memory': agent.memory_usage,
                   'runtime': agent.runtime
               },
               'issues': agent.issues  # List of detected problems
           }
           monitoring_data['agents'].append(agent_status)

       # Detect coordination issues
       issues = detect_coordination_issues(monitoring_data)

       return monitoring_data, issues

   # Example issues:
   # - Agent stalled (no progress for 2 minutes)
   # - Drift score ≥ 0.3
   # - Resource exhaustion
   # - Validation gate failed
   # - Deadlock detected
   ```

3. **Dynamic Intervention**
   ```python
   def intervene_if_needed(monitoring_data, issues):
       for issue in issues:
           if issue['type'] == 'agent_stalled':
               # Restart agent
               restart_agent(issue['agent_id'])

           elif issue['type'] == 'drift_detected':
               # Refactor agent task
               agent = get_agent(issue['agent_id'])
               refactor_agent_task(agent, issue['drift_details'])

           elif issue['type'] == 'validation_failed':
               # Block agent, request coordinator review
               block_agent(issue['agent_id'])
               coordinator_review(issue['agent_id'], issue['validation_details'])

           elif issue['type'] == 'resource_exhaustion':
               # Allocate more resources or reschedule
               if can_allocate_more_resources():
                   allocate_resources(issue['agent_id'])
               else:
                   reschedule_agent(issue['agent_id'])

           elif issue['type'] == 'deadlock':
               # Break deadlock by prioritizing critical path
               resolve_deadlock(issue['agents'])
   ```

**Threshold:** All agents monitored, issues resolved in real-time

### Layer 3: Result Synthesis (Merge, Validate, Unify)

**AFTER execution:**

1. **Result Collection**
   ```python
   def collect_results(completed_agents):
       results = []

       for agent in completed_agents:
           result = {
               'agent_id': agent.id,
               'task': agent.task,
               'output': agent.output,
               'validation': {
                   'drift_score': agent.drift_score,
                   'gates_passed': agent.gates_passed,
                   'compliance_score': agent.compliance_score
               },
               'metadata': {
                   'runtime': agent.runtime,
                   'resource_usage': agent.resource_usage
               }
           }

           # Validate individual result
           if not validate_agent_result(result):
               raise InvalidAgentResultError(agent.id)

           results.append(result)

       return results
   ```

2. **Result Merging**
   ```python
   def merge_results(results, merge_strategy):
       if merge_strategy == 'concatenate':
           merged = concatenate_results(results)

       elif merge_strategy == 'merge_with_conflict_resolution':
           merged = merge_with_resolution(results)

       elif merge_strategy == 'synthesize':
           # Use LLM to synthesize coherent output
           merged = llm_synthesize(results)

       elif merge_strategy == 'parallel_outputs':
           # Keep separate but validated outputs
           merged = {
               'type': 'parallel_outputs',
               'results': results
           }

       return merged
   ```

3. **Unified Validation**
   ```python
   def validate_unified_result(merged_result, original_task):
       validation = {}

       # Drift check: Does merged result fulfill original task?
       drift_score = drift_detector.detect(
           original=original_task,
           output=merged_result
       )
       validation['drift'] = {
           'score': drift_score,
           'passed': drift_score < 0.3
       }

       # Completeness: All subtasks represented?
       completeness = calculate_completeness(
           merged_result,
           original_task['subtasks']
       )
       validation['completeness'] = {
           'score': completeness,
           'passed': completeness >= 0.95
       }

       # Consistency: No conflicts between agent results?
       conflicts = detect_conflicts(merged_result)
       validation['consistency'] = {
           'conflicts': conflicts,
           'passed': len(conflicts) == 0
       }

       # Constitutional compliance
       compliance = validate_constitutional_compliance(
           merged_result,
           original_task['constitutional_requirements']
       )
       validation['compliance'] = {
           'score': compliance,
           'passed': compliance >= 0.80
       }

       overall_passed = all(v['passed'] for v in validation.values())

       return {
           'passed': overall_passed,
           'validation': validation
       }
   ```

**Threshold:** Drift < 0.3, completeness ≥ 0.95, zero conflicts, compliance ≥ 0.80

## Integrated Flow

```
Complex Task
    ↓
[Task Decomposition]
    ├─ Analyze dependencies
    ├─ Identify parallelizable work
    └─ Create agent specifications
    ↓
[Agent Orchestration]
    ├─ Spawn agents (parallel + sequential)
    ├─ Monitor progress in real-time
    ├─ Detect and resolve issues
    └─ Coordinate synchronization points
    ↓
[Result Synthesis]
    ├─ Collect agent results
    ├─ Merge with strategy
    ├─ Validate unified result
    └─ Check completeness, drift, consistency
    ↓
[Final Validation]
    ├─ Drift < 0.3
    ├─ Completeness ≥ 0.95
    ├─ Zero conflicts
    └─ Compliance ≥ 0.80
    ↓
OUTPUT: Unified, validated result + execution report + agent metrics
```

## Red Flags

- "Just run everything in parallel"
- "Skip dependency analysis"
- "No need to monitor agents"
- "Don't validate individual results"
- "Merge without conflict resolution"

**ALL mean: STOP. Use proper coordination.**

## Integration

**REQUIRED by:**
- `complex-workflows` - Multi-step task execution
- `parallel-research` - Concurrent information gathering
- `distributed-testing` - Test parallelization

**Complementary:**
- `intent-classification` - Task routing to agents
- `drift-detection` - Agent output validation
- `principle-validation` - Constitutional compliance

## Example: Multi-File Codebase Refactoring

**Task:** "Refactor authentication logic across 5 files"

**Execution:**

1. **Task Decomposition:**
   ```python
   analysis = {
       'total_subtasks': 5,
       'parallelizable': [
           'Refactor auth.js',
           'Refactor middleware.js',
           'Refactor routes.js',
           'Update tests',
           'Update documentation'
       ],
       'dependencies': {
           'tests': ['auth.js', 'middleware.js', 'routes.js'],
           'documentation': ['auth.js', 'middleware.js', 'routes.js']
       },
       'estimated_speedup': 3.5
   }
   ```

2. **Agent Spawning:**
   ```python
   # Spawn 3 agents in parallel
   agent_1 = spawn_agent(task='Refactor auth.js')
   agent_2 = spawn_agent(task='Refactor middleware.js')
   agent_3 = spawn_agent(task='Refactor routes.js')

   # Wait for completion
   wait_for_completion([agent_1, agent_2, agent_3])

   # Spawn dependent agents
   agent_4 = spawn_agent(task='Update tests')
   agent_5 = spawn_agent(task='Update documentation')

   wait_for_completion([agent_4, agent_5])
   ```

3. **Monitoring:**
   ```python
   monitoring = {
       'agent_1': {'status': 'complete', 'drift': 0.18, 'runtime': '2m 15s'},
       'agent_2': {'status': 'complete', 'drift': 0.22, 'runtime': '1m 58s'},
       'agent_3': {'status': 'complete', 'drift': 0.19, 'runtime': '2m 32s'},
       'agent_4': {'status': 'complete', 'drift': 0.14, 'runtime': '3m 10s'},
       'agent_5': {'status': 'complete', 'drift': 0.11, 'runtime': '1m 45s'}
   }
   Issues: None ✓
   ```

4. **Result Synthesis:**
   ```python
   results = collect_results([agent_1, agent_2, agent_3, agent_4, agent_5])

   merged = merge_results(results, strategy='concatenate')

   validation = validate_unified_result(merged, original_task)
   # {
   #   'passed': True,
   #   'validation': {
   #     'drift': {'score': 0.19, 'passed': True},
   #     'completeness': {'score': 1.0, 'passed': True},
   #     'consistency': {'conflicts': [], 'passed': True},
   #     'compliance': {'score': 0.95, 'passed': True}
   #   }
   # }
   ```

**Output:**
- 5 files refactored ✓
- Total time: 7m 12s (vs ~15m sequential)
- Speedup: 2.1x ✓
- Validation: All passed ✓

## Verification Checklist

- [ ] Task decomposed with dependency analysis
- [ ] Parallelizable work identified
- [ ] Agent specifications created
- [ ] Constitutional requirements propagated
- [ ] Coordination protocol defined
- [ ] Agents spawned in optimal order
- [ ] Real-time monitoring active
- [ ] Issues detected and resolved
- [ ] All agents completed successfully
- [ ] Results collected
- [ ] Results merged with strategy
- [ ] Drift < 0.3
- [ ] Completeness ≥ 0.95
- [ ] Zero conflicts
- [ ] Compliance ≥ 0.80
- [ ] TraceVault logged

## Final Rule

```
Multi-Agent Result → Validated unification with drift < 0.3 AND completeness ≥ 0.95
Otherwise → resolve conflicts or re-execute
```

Coordination transforms parallelism into power.
