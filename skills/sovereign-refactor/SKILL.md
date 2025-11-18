---
name: sovereign-refactor
description: Meta-cognitive refactoring with architectural quality tracking. Auto-activates on refactor/cleanup requests. Uses CGE + 5D quality + evolution. See references/ for details.
---

# Sovereign Refactor v1.1.0

**Triggers**: "리팩토링", "코드 개선", "구조 정리"

**Flow**: Intent → Analysis → Plan → Refactor → Quality → Evolve

**Quality (5D)**: Simplicity 30% | Cohesion 25% | Coupling 20% | Testability 15% | Performance 10%

**Output**: Refactored Code + Grade (F→A→S) + Improvements

**Modes**: MINIMAL (<0.3) | BALANCED (0.3-0.7) | STRICT (>0.7 via CLI)

**CLI**: `python D:/Sanctum/sovereign-tools/cli.py refactor "{file}" "{goal}"`

**Docs**: `references/workflow.md`, `references/quality.md`
