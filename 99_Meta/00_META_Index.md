# 99_Meta Index

## Purpose
This file is the canonical entrypoint for the `99_Meta/` instruction layer.

## Scope
- list canonical meta files only
- define the core load order for OpenCode
- define dynamic loading triggers
- define authority boundaries between the meta documents

## Out of Scope
- full policy bodies
- template contents
- legacy path references

## Authority
Canonical index for the `99_Meta/` layer. This file maps where OpenCode should look, but does not replace the underlying policy files.

## Canonical Files
- `[[01_Architecture/Vault Architecture.md|Vault Architecture]]`
- `[[02_Method/Study Didactics and Execution.md|Study Didactics and Execution]]`
- `[[03_Content/Vault Content Conventions.md|Vault Content Conventions]]`
- `[[04_Agent/Core Identity.md|Core Identity]]`
- `[[04_Agent/User Profile.md|User Profile]]`
- `[[04_Agent/Operational Workflow.md|Operational Workflow]]`
- `[[04_Agent/Tooling/Obsidian CLI.md|Obsidian CLI]]`
- `[[05_Templates/Concept Template.md|Concept Template]]`
- `[[05_Templates/Map Template.md|Map Template]]`
- `[[05_Templates/Comparison Template.md|Comparison Template]]`
- `[[05_Templates/Execution Template.md|Execution Template]]`
- `[[05_Templates/Exercise Template.md|Exercise Template]]`
- `[[05_Templates/Daily Memory Template.md|Daily Memory Template]]`
- `[[05_Templates/New Course Template|New Course Template]]`

## Core Load Order For OpenCode
1. root `AGENTS.md`
2. `99_Meta/00_META_Index.md`
3. `99_Meta/04_Agent/Core Identity.md`
4. `99_Meta/04_Agent/User Profile.md`
5. `99_Meta/04_Agent/Operational Workflow.md`
6. `99_Meta/02_Method/Study Didactics and Execution.md`
7. `99_Meta/03_Content/Vault Content Conventions.md`

## Dynamic Loading Triggers
- Load `99_Meta/04_Agent/Tooling/Obsidian CLI.md` only when an Obsidian CLI operation or vault-aware move/rename workflow is needed.
- Load files in `99_Meta/05_Templates/` only when creating, restructuring, or standardizing notes.
- Default to the core load order unless a task clearly needs a specialized reference.

## Authority Boundaries
- root `AGENTS.md` is authoritative for repository-wide agent policy.
- `99_Meta/04_Agent/` governs assistant behavior, user context, workflow, and specialized operational references.
- `99_Meta/02_Method/Study Didactics and Execution.md` governs study explanation behavior and didactic execution.
- `99_Meta/03_Content/Vault Content Conventions.md` governs note structure, tags, tasks, and content-level SSOT rules.
- `99_Meta/01_Architecture/Vault Architecture.md` governs long-term vault structure and knowledge flow.
- files in `99_Meta/05_Templates/` define output shapes.

## Working Rule
- If two files appear to govern the same topic, prefer the more specific canonical file and treat duplication as a refactor issue to be resolved.
