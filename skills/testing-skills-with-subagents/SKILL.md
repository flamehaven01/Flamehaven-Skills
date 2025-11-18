---
name: testing-skills-with-subagents
description: Use when creating or editing skills, before deployment, to verify they work under pressure and resist rationalization - applies RED-GREEN-REFACTOR cycle to process documentation by running baseline without skill, writing to address failures, iterating to close loopholes
---

# Testing Skills With Subagents

## Overview

**Testing skills is just TDD applied to process documentation.**

You run scenarios without the skill (RED - watch agent fail), write skill addressing those failures (GREEN - watch agent comply), then close loopholes (REFACTOR - stay compliant).

**Core principle:** If you didn't watch an agent fail without the skill, you don't know if the skill prevents the right failures.

**REQUIRED BACKGROUND:** You MUST understand superpowers:test-driven-development before using this skill. That skill defines the fundamental RED-GREEN-REFACTOR cycle. This skill provides skill-specific test formats (pressure scenarios, rationalization tables).

**Complete worked example:** See examples/CLAUDE_MD_TESTING.md for a full test campaign testing CLAUDE.md documentation variants.

## When to Use

- Enforce discipline (TDD, testing requirements)
- Have compliance costs (time, effort, rework)
- Could be rationalized away ("just this once")
- Contradict immediate goals (speed over quality)
- Pure reference skills (API docs, syntax guides)


## Details

See `references/` for complete workflows, algorithms, and examples.