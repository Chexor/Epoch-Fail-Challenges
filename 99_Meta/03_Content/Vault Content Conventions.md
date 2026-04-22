# Vault Content Conventions

## Purpose
Define the canonical conventions for note structure, tags, tasks, note types, and content-level SSOT behavior.

## Scope
- note types and their roles
- tags and task syntax
- content SSOT rules
- naming rules that affect vault consistency

## Out of Scope
- assistant tone and identity
- didactic explanation strategy
- sync troubleshooting
- tooling instructions

## Authority
Canonical for content conventions across the vault.

## Related Documents
- `99_Meta/01_Architecture/Vault Architecture.md`
- `99_Meta/02_Method/Study Didactics.md`
- `99_Meta/04_Operations/Operational Workflow.md`

## General Rules
- use exactly one H1 for normal notes
- use headings logically and avoid needless hierarchy jumps
- prefer short, scannable paragraphs
- use fenced code blocks with language tags when possible
- use `[[WikiLinks]]` in the vault unless a subproject has its own link style

## Tags
- tags live inline in the note body, not in YAML frontmatter
- use a module tag for course-specific material where relevant
- use a type tag to identify the note role
- use a domain tag for concept notes when useful
- use status tags only when they add real value

### Common Type Tags
- `#concept`
- `#oefeningen`
- `#lesnotitie`
- `#ssot`
- `#hub`

## Tasks
- tasks must use Tasks-compatible Markdown syntax
- each task should end with the relevant module tag

Example:

```markdown
- [ ] Oefening 13 uitwerken #ps2
- [ ] Hoofdstuk 5 samenvatten #da
```

## Note Types

### Concept Notes
- usually live in `20_Domains/`
- should be atomic, reusable, and compact
- should follow the study didactic method
- should normally use `#concept` plus a domain tag
- should start with one short explanatory sentence directly under the title so backlink pop-ups are immediately useful
- should include a `## Korte kern` section before the deeper explanation starts

### Concept Domain Structure
- the default pattern for a concept domain is `01_Atlas/`, `02_Theory/`, and `03_Atom/`
- `04_Practice/` and `05_Versus/` are optional and should be created only when the note type recurs and adds clear value
- visual support should stay embedded in notes by default and only become a separate structure when a domain clearly benefits from it
- `theme` defines the conceptual context or paradigm, while `domain` defines the vault location
- `01_Atlas/` notes are didactic navigation hubs; `Bases` are operational index views and do not replace atlas notes

### Theory Notes
- live in `20_Domains/.../02_Theory/`
- explain one reusable concept
- may represent a specific member of a larger concept family
- may also act as an umbrella concept when the category itself needs real conceptual explanation
- should follow this default body shape unless there is a strong reason not to:
  - short opening sentence
  - `Korte kern`
  - `Probleem`
  - `Intuïtie`
  - `Toepassing`
  - `Formeel`
  - `Verbanden`
- may include at most one short, neutral Python snippet when code genuinely clarifies the concept
- longer code, multiple variants, output discussion, or step-by-step implementation should move to a `Practice` note

### Atom Notes
- live in `20_Domains/.../03_Atom/`
- capture one compact term or definition with minimal scope
- should stay short and strongly linked to a parent `Theory` note when relevant

### Atlas Notes
- usually live in `20_Domains/.../01_Atlas/`
- organize a domain, concept family, or study path
- may act as umbrella concept notes when a category needs explanation plus links to child concepts
- their main job is navigation, ordering, and didactic overview
- if a category needs substantial reusable explanation as a concept in its own right, prefer an umbrella `Theory` note plus an `Atlas` note for navigation

### Comparison Notes
- usually live in `20_Domains/.../05_Versus/`
- exist to distinguish related concepts where the contrast itself is the learning value

### Execution Notes
- usually live in `20_Domains/.../04_Practice/`
- capture worked examples, implementation notes, or applied walkthroughs
- should support a concept note rather than replace it
- are the default place for substantial code examples
- should prefer neutral, readable Python with small inputs and minimal dependencies when code is useful

### Parent-Child Concept Rule
- use a **parent-first** model
- store one primary `parent` explicitly when a note belongs under a clear umbrella concept
- do **not** store separate `siblings` or `children` properties in notes
- derive siblings as notes with the same `parent`
- derive children as notes that point to the current note as `parent`
- parent-child structure is a navigation aid, not a rigid ontology
- use `related` plus explicit `[[WikiLinks]]` to preserve network-like relationships beyond the primary parent

### Exercise Notes
- usually live under `10_Modules/`
- should use the module tag plus `#oefeningen`
- should include a `## Gebruikte Concepten` section with `[[WikiLinks]]`

### SSOT Notes
- a `#ssot` note is the canonical content source for a specific topic within a course or domain
- summaries and derivative notes should point back to that source

### Hub Notes
- a `#hub` note is for navigation, status, and overview
- a hub is not automatically the content authority unless explicitly marked as such

## Content SSOT Rules
- update the canonical source first
- only update derivative notes after the source is correct
- avoid parallel notes that explain almost the same thing
- if a note is only a pointer, make that obvious

## Naming Guidance
- follow the naming pattern already established in the target folder
- keep names descriptive and stable
- avoid renames unless they improve clarity or remove duplication
- when Windows-safe filenames are needed, keep the visible wiki link human-readable and use aliases where useful

### Lesson Naming Convention
- for new lesson folders in `10_Modules/`: `[vakafkorting] - Les [#] - [thema]`
- for new lesson notes in that folder: `[vakafkorting]-Les[#]-[thema].md`
- if a lesson already uses an older naming pattern, reuse it by default; rename only on explicit user request

## Recommended Concept Metadata
- `type`
- `domain`
- `parent`
- `related`
- `theme`
- `aliases`

### Field Intent
- `type` = role of the note (`theory`, `atlas`, `atom`, `practice`, `versus`)
- `domain` = durable knowledge domain
- `parent` = primary umbrella concept or left empty for root-level domain concepts
- `related` = strongest lateral links, usually 2-5 useful connections rather than a dump list
- `theme` = overkoepelend thema / conceptual cluster
- `aliases` = readable alternative names for linking and retrieval

## Simplicity Rule
- prefer the simplest domain structure that still supports the learning goal
- do not create optional concept-domain subfolders in advance
- create `04_Practice/` or `05_Versus/` only when there is at least one real note ready to live there

## Boundary Rules
- didactic note structure belongs in `99_Meta/02_Method/Study Didactics.md`
- assistant identity belongs in root `AGENTS.md`
- routing and operational handling belong in `99_Meta/04_Operations/Operational Workflow.md`
