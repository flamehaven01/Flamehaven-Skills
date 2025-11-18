---
name: condition-based-waiting
description: Use when tests have race conditions, timing dependencies, or inconsistent pass/fail behavior - replaces arbitrary timeouts with condition polling to wait for actual state changes, eliminating flaky tests from timing guesses
---

# Condition-Based Waiting

## Overview

Flaky tests often guess at timing with arbitrary delays. This creates race conditions where tests pass on fast machines but fail under load or in CI.

**Core principle:** Wait for the actual condition you care about, not a guess about how long it takes.

## When to Use

- *Use when:**
- Tests have arbitrary delays (`setTimeout`, `sleep`, `time.sleep()`)
- Tests are flaky (pass sometimes, fail under load)
- Tests timeout when run in parallel
- Waiting for async operations to complete


## Details

See `references/` for complete workflows, algorithms, and examples.