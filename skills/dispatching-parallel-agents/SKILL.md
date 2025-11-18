---
name: dispatching-parallel-agents
description: Use when facing 3+ independent failures that can be investigated without shared state or dependencies - dispatches multiple Claude agents to investigate and fix independent problems concurrently
---

# Dispatching Parallel Agents

## Overview

When you have multiple unrelated failures (different test files, different subsystems, different bugs), investigating them sequentially wastes time. Each investigation is independent and can happen in parallel.

**Core principle:** Dispatch one agent per independent problem domain. Let them work concurrently.

## When to Use

- *Use when:**
- 3+ test files failing with different root causes
- Multiple subsystems broken independently
- Each problem can be understood without context from others
- No shared state between investigations


## Details

See `references/` for complete workflows, algorithms, and examples.