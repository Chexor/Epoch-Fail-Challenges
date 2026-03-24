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
- `99_Meta/02_Method/Study Didactics and Execution.md`
- `99_Meta/04_Agent/Operational Workflow.md`

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
- usually live in `20_Concepts/`
- should be atomic, reusable, and compact
- should follow the study didactic method
- should normally use `#concept` plus a domain tag

### Concept Domain Structure
- the default pattern for a concept domain is `Topics/` plus `Maps/`
- `Comparisons/` and `Execution/` are optional and should be created only when the note type recurs and adds clear value
- visual support should stay embedded in notes by default and only become a separate structure when a domain clearly benefits from it
- `theme` defines the conceptual context or paradigm, while `domain` defines the vault location

### Topic Notes
- live in `20_Concepts/.../Topics/`
- explain one reusable concept
- may represent a specific member of a larger concept family

### Map Notes
- usually live in `20_Concepts/.../Maps/`
- organize a domain, concept family, or study path
- may act as umbrella concept notes when a category needs explanation plus links to child concepts

### Comparison Notes
- usually live in `20_Concepts/.../Comparisons/`
- exist to distinguish related concepts where the contrast itself is the learning value

### Execution Notes
- usually live in `20_Concepts/.../Execution/`
- capture worked examples, implementation notes, or applied walkthroughs
- should support a concept note rather than replace it

### Parent-Child Concept Rule
- umbrella category concepts usually live in `Maps/`
- specific reusable sub-concepts usually live in `Topics/`
- parent-child structure is a navigation aid, not a rigid ontology
- use explicit `[[WikiLinks]]` to preserve network-like relationships beyond the primary parent

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

## Simplicity Rule
- prefer the simplest domain structure that still supports the learning goal
- do not create optional concept-domain subfolders in advance
- create `Comparisons/` or `Execution/` only when there is at least one real note ready to live there

## Boundary Rules
- didactic behavior belongs in `99_Meta/02_Method/Study Didactics and Execution.md`
- assistant identity belongs in `99_Meta/04_Agent/Core Identity.md`
- routing and operational handling belong in `99_Meta/04_Agent/Operational Workflow.md`
