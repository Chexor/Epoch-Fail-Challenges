# Vault Architecture

## Purpose
Define the long-term structure of the vault as a study-first knowledge system for Tim and OpenCode.

## Scope
- top-level vault zones
- role of modules versus concepts
- knowledge flow from capture to durable understanding
- architectural decisions that shape note placement and reuse

## Out of Scope
- note formatting rules
- agent tone and behavior
- sync troubleshooting
- templates

## Authority
Canonical for vault architecture and high-level information design.

## Related Documents
- `99_Meta/02_Method/Study Didactics.md`
- `99_Meta/03_Content/Vault Content Conventions.md`
- `99_Meta/04_Operations/Operational Workflow.md`

## Architecture Model

The vault is treated as a structured knowledge system, not as a loose folder of notes.

- `00_Inbox/` captures raw input and temporary intake.
- `10_Modules/` stores active course and module material.
- `20_Domains/` stores reusable concept notes that outlive a single course.
- `30_Resources/` stores attachments, screenshots, and external reference material.
- `99_Meta/` stores the canonical instruction layer, methods, conventions, and templates.
- `Z_Archive/` stores inactive or retired material.

## Core Architectural Split

### `10_Modules/` is the active workspace
- use it for course-specific notes, lesson material, summaries, and exercises
- structure each course predictably so navigation and retrieval stay stable
- course material may be temporary or semester-bound
- internal folder structure varies by course format:
  - **AO (afstandsonderwijs):** organised by topic/chapter — `01_Bronnen/`, `02_Topics/` or `02_Hoofdstukken/`, `03_Examenvoorbereiding/`
  - **Dagonderwijs:** organised by lesson — `Bronnen/`, `Lessen/`, `Labs/` (may vary per course)
- this distinction is intentional; do not standardise across formats

### `20_Domains/` is the durable knowledge layer
- use it for reusable domain knowledge that outlives a single course
- treat it as a living knowledge network rather than a flat concept archive
- concept domains should default to `01_Atlas/`, `02_Theory/`, and `03_Atom/`
- larger domains may add `04_Practice/` or `05_Versus/` when those note types provide recurring value
- visual support should be embedded by default and separated only when a domain clearly benefits from a dedicated visual cluster
- concept notes are meant to remain useful after a specific course ends
- `01_Atlas/` is the didactic navigation layer
- Obsidian `Bases` are the dynamic operational index layer
- umbrella concepts may live in `02_Theory/` when they carry real reusable explanation; `01_Atlas/` should not be overloaded with that job by default
- concept hierarchies should use one explicit `parent` field; `siblings` and `children` should be derived rather than stored separately

## Knowledge Flow
1. Capture raw information in `00_Inbox/`.
2. Route course-specific material into the correct location in `10_Modules/`.
3. Distill reusable knowledge into `20_Domains/` when it has cross-course value.
4. Link concepts and applications so retrieval follows understanding instead of folder memory.

## Architectural Rules
- prefer improving an existing note over creating a duplicate
- prefer reusable concept notes for domain knowledge that appears in multiple modules
- keep `99_Meta/` small, explicit, and policy-focused
- avoid parallel structures that describe the same responsibility twice
- keep `20_Domains/` simple by default and expand its domain structure only when the extra layer clearly improves learning or retrieval

## Design Goal
The vault should help the AI and the user answer three questions quickly:
- where does new information belong?
- what is the canonical note for this topic?
- what should remain reusable after the current course ends?
