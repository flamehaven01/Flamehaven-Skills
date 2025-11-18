# Sovereign Core Architecture

## System Architecture

```
sovereign-core/           # Foundation layer
├── meta_engine/
│   ├── base.py          # MetaCognitiveEngine (universal)
│   ├── quality_tensor.py # N-dimensional quality
│   └── evolution_engine.py # Learning & convergence
│
sovereign-code/          # Domain: Code generation
sovereign-debug/         # Domain: Debugging
sovereign-refactor/      # Domain: Refactoring
sovereign-architect/     # Domain: Architecture (future)
sovereign-test/          # Domain: Test generation (future)
```

## Core Pattern (CGE v2.3)

All domain skills inherit this 8-step pattern:

```python
1. INTENT ANALYSIS
   - Understand user request
   - Extract task details
   - Calculate complexity (0-1)

2. VALIDATION
   - Verify context
   - Check constraints
   - Assess confidence

3. POLICY RESOLUTION
   - Select mode (MINIMAL/BALANCED/STRICT)
   - Decide resource allocation
   - Set quality targets

4. PLAN GENERATION
   - Create execution steps
   - Define validation points
   - Plan rollback strategy

5. EXECUTION
   - Execute task (inline or CLI)
   - Token-optimized delegation
   - Resource-aware processing

6. QUALITY MEASUREMENT
   - Measure N dimensions
   - Calculate weighted grade
   - Identify weak points

7. EVOLUTION TRACKING
   - Record cycle
   - Detect learning
   - Predict convergence

8. EXPLANATION
   - Summarize result
   - Present quality metrics
   - Recommend improvements
```

## Usage by Domain Skills

Domain skills extend `MetaCognitiveEngine`:

```python
from sovereign_core.meta_engine import MetaCognitiveEngine

class CodeGenerationEngine(MetaCognitiveEngine):
    def __init__(self):
        super().__init__(domain="code")

    def get_quality_dimensions(self):
        return ["correctness", "readability", "performance",
                "security", "maintainability"]

    def get_quality_weights(self):
        return {
            "correctness": 0.30,
            "readability": 0.25,
            "performance": 0.20,
            "security": 0.15,
            "maintainability": 0.10
        }

    # ... implement domain-specific methods
```

## Integration

Sovereign Core is **never directly invoked**. It serves as the foundation that domain skills build upon. Users interact with domain-specific skills (sovereign-code, sovereign-debug, etc.), which automatically leverage Sovereign Core's meta-cognitive capabilities.

## Token Optimization

Adaptive resource delegation based on complexity:

- **MINIMAL** (< 0.3): Skills inline (500-2,000 tokens)
- **BALANCED** (0.3-0.7): Hybrid (1,000 tokens)
- **STRICT** (> 0.7): CLI subprocess (500 tokens)
