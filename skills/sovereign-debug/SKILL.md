---
name: sovereign-debug
description: Meta-cognitive debugging with root cause analysis. Auto-activates on bug/error reports. Uses CGE + 5D quality + pattern learning. See references/ for details.
---

# Sovereign Debug v1.1.0

**Triggers**: "버그 고쳐줘", "에러 해결", "디버깅"

**Flow**: Intent → Hypothesis → Root Cause → Fix → Quality → Learn

**Quality (5D)**: Root Cause 30% | Fix Effectiveness 25% | Regression Risk 20% | Time 15% | Learning 10%

**Output**: Fix + Grade (F→A→S) + Pattern Analysis

**Modes**: MINIMAL (<0.3) | BALANCED (0.3-0.7) | STRICT (>0.7 via CLI)

**CLI**: `python D:/Sanctum/sovereign-tools/cli.py debug "{file}" "{issue}"`

**Docs**: `references/workflow.md`, `references/patterns.md`
