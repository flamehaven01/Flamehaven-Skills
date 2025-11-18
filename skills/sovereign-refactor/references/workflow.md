# Sovereign Refactor Workflow

## Meta-Cognitive Refactoring Process

```
User: "이 레거시 코드 리팩토링해줘"

Claude (Meta-Cognitive Refactoring):

[1. ANALYSIS]
Current state:
- Cyclomatic complexity: 25 (high)
- Module coupling: High
- Test coverage: 45%
Complexity: 0.72 (high)

[2. POLICY]
Mode: BALANCED
Strategy: [analyze, plan, refactor, test, validate]

[3. REFACTORING]
Applied:
- Extract methods (5 → 12 smaller functions)
- Dependency injection (reduced coupling)
- Add unit tests

[4. QUALITY (Before → After)]
- Simplicity: 0.45 → 0.88 ✓ (+95% improvement!)
- Cohesion: 0.60 → 0.90 ✓
- Coupling: 0.75 → 0.15 ✓ (inverted metric)
- Testability: 0.45 → 0.92 ✓
- Performance: 0.85 → 0.87 ✓

Grade: C → A (0.68 → 0.90)

[5. EVOLUTION]
Improvement: +32% quality
Pattern learned: "High complexity + low coverage → extract methods strategy"
```

## When to Use

- Code cleanup requests
- Architectural improvements
- Technical debt reduction
- Performance optimization
- Maintainability enhancement

## Common Refactoring Patterns

### Pattern 1: High Complexity
**Indicators**: Cyclomatic complexity > 15
**Strategy**: Extract methods, reduce nesting
**Expected improvement**: Simplicity +40-60%

### Pattern 2: High Coupling
**Indicators**: Many inter-module dependencies
**Strategy**: Dependency injection, interface abstraction
**Expected improvement**: Coupling -50-70%

### Pattern 3: Low Test Coverage
**Indicators**: Coverage < 60%
**Strategy**: Add unit tests, improve testability
**Expected improvement**: Testability +30-50%
