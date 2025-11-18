# Examples

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

