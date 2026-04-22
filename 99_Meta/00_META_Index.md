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
- `[[02_Method/Study Didactics.md|Study Didactics]]`
- `[[03_Content/Vault Content Conventions.md|Vault Content Conventions]]`
- `[[04_Operations/Operational Workflow.md|Operational Workflow]]`
- `[[04_Operations/Tooling/Obsidian CLI.md|Obsidian CLI]]`
- `[[05_Templates/Concept Template.md|Concept Template]]`
- `[[05_Templates/Atlas Template.md|Atlas Template]]`
- `[[05_Templates/Comparison Template.md|Comparison Template]]`
- `[[05_Templates/Execution Template.md|Execution Template]]`
- `[[05_Templates/Exercise Template.md|Exercise Template]]`
- `[[05_Templates/Daily Memory Template.md|Daily Memory Template]]`
- `[[05_Templates/New Course Template|New Course Template]]`

## Responsibility Table
- **Behavior / personality / AI execution posture** -> root `AGENTS.md`
- **Folder structure / placement / routing architecture** -> `[[01_Architecture/Vault Architecture.md|Vault Architecture]]`
- **Study-note didactic method as vault convention** -> `[[02_Method/Study Didactics.md|Study Didactics]]`
- **Note conventions / naming / metadata / tags** -> `[[03_Content/Vault Content Conventions.md|Vault Content Conventions]]`
- **Operational vault workflows / runbooks / command behavior** -> `[[04_Operations/Operational Workflow.md|Operational Workflow]]`
- **Templates / output shapes** -> `99_Meta/05_Templates/`

## Core Load Order For OpenCode
1. root `AGENTS.md`
2. `99_Meta/00_META_Index.md`
3. `99_Meta/04_Operations/Operational Workflow.md`
4. `99_Meta/02_Method/Study Didactics.md`
5. `99_Meta/03_Content/Vault Content Conventions.md`

## Dynamic Loading Triggers
- Load `99_Meta/04_Operations/Tooling/Obsidian CLI.md` only when an Obsidian CLI operation or vault-aware move/rename workflow is needed.
- Load files in `99_Meta/05_Templates/` only when creating, restructuring, or standardizing notes.
- For `20_Domains/` structure, metadata, parent-child rules, or Atlas vs Bases questions, load `99_Meta/01_Architecture/Vault Architecture.md` plus `99_Meta/03_Content/Vault Content Conventions.md` before using templates.
- Default to the core load order unless a task clearly needs a specialized reference.

## Authority Boundaries
- root `AGENTS.md` is authoritative for repository-wide agent policy.
- `99_Meta/04_Operations/` governs vault workflow, runbooks, and specialized operational references.
- `99_Meta/02_Method/Study Didactics.md` governs the didactic structure expected in study content stored in the vault.
- `99_Meta/03_Content/Vault Content Conventions.md` governs note structure, tags, tasks, and content-level SSOT rules.
- `99_Meta/01_Architecture/Vault Architecture.md` governs long-term vault structure, Atlas vs Bases, and high-level domain organization.
- folder and placement questions default to `Vault Architecture`; note format and naming questions default to `Vault Content Conventions`.
- archived material in `Z_Archive/` stays out of active context by default; operational exceptions are defined in `04_Operations/Operational Workflow.md`.
- files in `99_Meta/05_Templates/` define output shapes.

## Working Rule
- If two files appear to govern the same topic, prefer the more specific canonical file and treat duplication as a refactor issue to be resolved.
