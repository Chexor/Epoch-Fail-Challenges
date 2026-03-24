# 20_Concepts Architecture Plan

> Status: DEPRECATED - Fully implemented as the canonical pattern for `20_Concepts/` domain rollout.

## Purpose
Define the target structure, note types, and meta updates needed to turn `20_Concepts/` into a durable, linked, ADHD-friendly concept network rather than a flat collection of notes.

## Scope
- target role of `20_Concepts/`
- allowed subfolder types inside concept domains
- placement rules for concept notes
- visual and map support
- required meta changes to formalize the structure

## Out of Scope
- full migration of `20_Concepts/`
- note-by-note restructuring
- cleanup of `10_Modules/`

## Authority
Planning document for the next refactor phase of `20_Concepts/`.

## Intent
`20_Concepts/` should function as a living knowledge network.

It should:
- store reusable knowledge by domain, not by course
- connect concepts through links, maps, comparisons, and examples
- support visual thinking and concept clustering
- help Tim process and understand material with low cognitive friction

It should not become:
- a second copy of module notes
- a flat archive of isolated definitions
- a folder tree with no meaningful relationships between notes
- an over-engineered metadata system that becomes harder to maintain than the knowledge itself

## Design Constraint
This architecture must work for both:
- Tim's ADD-friendly study flow
- OpenCode's need for clear, predictable structure

The system should therefore be:
- rich enough to support big-picture understanding, linking, comparison, and visuals
- simple enough to stay stable over time
- easy to maintain without turning every note into administration work

## Core Model

### Role of `20_Concepts/`
- `10_Modules/` answers: where did this appear in a course?
- `20_Concepts/` answers: what is this concept, how does it connect, and where else does it apply?

### Concept Granularity
`20_Concepts/` should support both:
- umbrella concepts that explain a family or category
- atomic concepts that explain one specific concept or instance

This is intentional.

The knowledge network should not flatten everything to the same level of abstraction.

Example:
- `Datatypes` explains what datatypes are, why they exist, and how the category is organized
- `uint8`, `uint16`, `float32`, and `float64` explain specific datatype members

In practice:
- umbrella concepts usually belong in `Maps/`
- atomic concepts usually belong in `Topics/`

## Minimal But Powerful Model

### Level 1 - Core structure (default)
This is the baseline that should work everywhere.

- each domain should support `Topics/`
- each domain should support `Maps/`
- each domain should have at least one meaningful map note when the domain is non-trivial
- topic notes should stay compact, reusable, and link to nearby concepts where useful

### Level 2 - High-value extensions (recommended where useful)
Add these only when they clearly improve understanding.

- `Comparisons/`
- `Execution/`
- parent-child concept patterns such as umbrella concept in `Maps/` and child concepts in `Topics/`
- visual canvases or diagrams when they improve big-picture understanding

### Level 3 - Optional AI support
Use only when the value is clear and maintenance stays low.

- compact AI-oriented headers
- a few extra relation fields for difficult or high-value concepts

### What stays out by default
- large metadata schemas
- deep folder nesting without clear learning value
- forcing every domain to use every folder type
- forcing every concept to have comparisons, execution notes, visuals, or advanced relation metadata

### Knowledge Layers Inside A Domain
Each concept domain may use the following note layers.

#### `Topics/`
- atomic concept notes
- the main reusable knowledge objects
- default destination for concept content

#### `Maps/`
- overview notes
- learning paths
- domain navigation hubs
- conceptual cluster notes
- umbrella concept notes that organize a family of related atomic concepts

#### `Comparisons/`
- contrast notes between nearby concepts
- useful when understanding depends on distinctions rather than isolated definitions

#### `Execution/`
- worked examples
- implementation notes
- concrete applications too large for a topic note
- the practical side of a concept when theory and execution are worth separating

#### Visual support
- canvases
- diagram notes
- visual concept networks
- embedded visuals inside map or topic notes by default

## Folder Policy

### Default domain pattern
Unless a domain clearly needs more, use:

```text
Domain/
  Topics/
  Maps/
```

This should be treated as the normal case.

### Expand only for clear value
Add `Comparisons/` or `Execution/` only when they produce a clear learning or retrieval benefit.

Use visual support on demand:
- embed visuals in `Maps/` or `Topics/` by default
- create a separate visual structure only when a domain accumulates enough visual material to justify it

### On-demand subfolder rule
Do not create optional subfolders in advance.

Create them only when there is at least one real note, comparison, execution note, or visual asset that belongs there.

### Hard cap principle
Do not introduce extra folder types unless they solve a repeated real problem in that domain.

## Recommended Domain Pattern

### Small domains
Use a minimal structure:

```text
Domain/
  Topics/
  Maps/
```

### Medium or growing domains
Use:

```text
Domain/
  Topics/
  Maps/
  Comparisons/
  Execution/
  [visual support embedded or separated only when justified]
```

### Large practice-heavy domains
Use:

```text
Domain/
  Topics/
  Maps/
  Comparisons/
  Execution/
  [separate visual structure only if the domain earns it]
```

## Placement Rules

### Put a note in `Topics/` when
- it explains one concept
- it should remain reusable across multiple modules
- it can stand on its own
- it is a specific member of a larger concept family

### Put a note in `Maps/` when
- it organizes a cluster of concepts
- it provides a study path or overview
- its main job is navigation or context
- it explains an umbrella concept whose main value is to structure and connect a family of sub-concepts

### Default decision rule
If a note could fit in multiple places, prefer the simpler structure.

In practice:
- prefer `Topics/` over inventing a new folder
- prefer `Maps/` over splitting a domain too early
- only create `Comparisons/` or `Execution/` when the note type is clearly distinct and likely to recur
- keep visuals embedded by default unless a separate visual structure clearly improves retrieval

### Put a note in `Comparisons/` when
- the note exists to distinguish related concepts
- the contrast itself is the main learning value

### Put a note in `Execution/` when
- the note is mainly a worked case, implementation, or applied walkthrough
- keeping it inside a topic note would make that topic bloated
- the practical side of the concept deserves its own reusable note

### Use separate visual structure when
- a domain has multiple canvases or visual notes
- visual material becomes hard to navigate when kept inline
- a dedicated visual cluster would clearly improve retrieval

## Note Conventions For `20_Concepts/`

### Topic notes
- one concept per note
- should follow the canonical study didactic structure
- should link to related concepts where useful
- should remain compact enough to stay reusable
- may represent a concrete subtype or member of an umbrella concept

### Map notes
- are hubs, not content authorities by default
- should group concepts into meaningful chunks
- should include a short explanation of the structure, not just a raw link dump
- may also act as umbrella concept notes when a category itself needs explanation and links to child concepts

### Parent-child concept pattern
When a domain contains a category with multiple concrete sub-concepts:
- use one map note for the parent concept
- use separate topic notes for the child concepts
- link downward from the parent note into the child notes
- link upward from child notes back to the parent note

Example:

```text
Computer Science/
  Data Representation/
    Maps/
      Datatypes.md
    Topics/
      uint8.md
      uint16.md
      float32.md
      float64.md
```

In this pattern:
- `Datatypes.md` explains the category, purpose, and major distinctions
- the individual datatype notes explain the specific properties and use cases of each type

### Comparison notes
- should state what is being compared and why the distinction matters
- should favor tables, contrasts, and common-confusion framing

### Execution notes
- should reference the topic note they support
- should focus on application, implementation, or walkthrough rather than re-explaining the entire concept

### Visual support
- should have a matching text hub or map note when the canvas would otherwise be hard to interpret
- should stay embedded unless a separate visual cluster gives clear retrieval value

## AI-Oriented Metadata

### Principle
AI-facing metadata is allowed when it improves retrieval, relationship detection, or visual generation.

It should remain compact enough that the human-facing body stays primary.

### Minimal recommended header
Use only when it creates clear value:

```yaml
---
type:
domain:
parent:
related:
theme:
---
```

### Field intent
- `type` -> note role such as topic, map, comparison, execution, or visual
- `domain` -> domain clustering
- `parent` -> primary umbrella concept when a child note belongs to one
- `related` -> nearby concepts worth surfacing
- `theme` -> the larger knowledge frame or overkoepelend thema this concept belongs to

### Optional fields
Only add these for concepts where they create clear value:
- `used_in`
- `common_confusions`
- `visual_candidates`

### Anti-complexity rule for metadata
- do not require advanced metadata on every note
- do not add fields unless they improve study support or AI behavior in a repeatable way
- if the body and normal links already do the job well, skip extra metadata

## Linking Rules
- topic notes should link laterally to nearby concepts when that improves understanding
- map notes should link downward into topics and sideways into related maps
- child concept notes should link back to their umbrella note when such a primary parent concept exists
- execution notes should link back to the concept they instantiate
- module notes in `10_Modules/` should prefer linking into concept notes rather than duplicating full explanations

## Parent-Child Flexibility
Parent-child structure is useful, but it must not become rigid.

- a concept may have one primary parent for placement and navigation
- `related` links should carry cross-domain or multi-parent-like relationships
- use explicit links to preserve network behavior where a strict tree would be misleading

## Analogy And Transfer Support
The structure should help OpenCode surface useful analogies, not just direct links.

Desired behavior:
- when a new concept resembles an existing one, OpenCode should be able to point to that familiar concept
- when a concept extends a known pattern, OpenCode should be able to use that as a teaching bridge

Examples:
- arrays and matrices
- derivative and gradient
- datatype families and numeric categories

This should mainly be supported through:
- parent-child concept structure
- `related` links
- `theme` positioning
- selective use of `common_confusions` or `used_in` when useful

It should not depend on a heavy relationship ontology.

## Anti-Dump Rules
- avoid creating overview notes that are just long unordered lists of links
- avoid putting broad lecture summaries into `20_Concepts/`
- avoid duplicate concept notes that differ only by course context
- avoid adding folder types unless they create a clear learning benefit
- avoid collapsing umbrella concepts and atomic child concepts into one bloated note when the child concepts deserve their own reusable explanations
- avoid turning every concept into a metadata-heavy database entry
- avoid creating systems that are theoretically elegant but practically too hard to maintain
- avoid creating empty optional subfolders just because the architecture allows them

## Pilot Proposal: `Machine Learning/`

### Target structure
```text
20_Concepts/Machine Learning/
  Maps/
    00_Overzicht Machine Learning Concepten.md
  Topics/
    ...atomic ML concept notes...
  Comparisons/
    ...contrast notes where useful...
  Execution/
    ...worked examples and implementation notes...
  [visual support embedded or separated only when justified]
```

### Why this domain is a good pilot
- it already has a meaningful concept set
- it already has a domain overview note
- it benefits strongly from visual clustering and comparison notes
- it contains both theory and application-heavy material

### First useful additions for the pilot
- move the current overview note into `Maps/`
- keep concept definitions in `Topics/`
- create comparison notes such as `MAE vs MSE vs RMSE.md`
- create execution notes such as `Gradient Descent Worked Example.md`
- add at least one ML concept canvas, embedded or grouped only if retrieval justifies it
- keep the pilot intentionally small so the structure proves its value before scaling

## Meta Changes Required

### 1. `99_Meta/01_Architecture/Vault Architecture.md`
Add a clearer statement that `20_Concepts/` is a domain-organized knowledge network, not just a concept folder.

Add that concept domains may contain:
- `Topics/`
- `Maps/`
- `Comparisons/`
- `Execution/`
- optional visual support structure when justified

### 2. `99_Meta/03_Content/Vault Content Conventions.md`
Add explicit note-type conventions for:
- topic notes
- map notes
- comparison notes
- execution notes
- visual support

Add a parent-child concept rule so it is clear that:
- umbrella category concepts usually live in `Maps/`
- specific reusable sub-concepts usually live in `Topics/`
- parent-child is a navigation aid, not a rigid ontology

Add placement rules so it is clear when a note belongs in:
- `20_Concepts/.../Topics/`
- `20_Concepts/.../Maps/`
- `20_Concepts/.../Comparisons/`
- `20_Concepts/.../Execution/`
- embedded visual support versus separate visual structure

Add a simplicity rule that:
- `Topics/` and `Maps/` are the default domain pattern
- all other concept-domain folders are optional and must justify themselves by repeated use and clear learning value
- optional subfolders should be created on demand, not in advance

### 3. `99_Meta/02_Method/Study Didactics and Execution.md`
Add a short rule that concept explanations in `20_Concepts/` should not only define a concept, but also position it in a knowledge structure and connect it to related ideas where useful.

### 4. `99_Meta/05_Templates/`
Add or revise templates for:
- concept topic note
- comparison note
- execution note
- map note

The map note template should explicitly support umbrella concepts, not only navigation hubs.

Any visual wrapper template should stay optional.

### 5. `99_Meta/00_META_Index.md`
No structural change required.

The index already routes correctly; only the canonical content and architecture files need to absorb the new `20_Concepts/` conventions.

## Safe Migration Sequence
1. formalize the conventions in meta first
2. choose one pilot domain, starting with `Machine Learning/`
3. create only the folders that have immediate value
4. migrate overview notes and obvious execution/comparison notes first
5. leave stable topic notes in place unless a move gives clear value
6. update links after each domain-level change
7. only scale the pattern to other domains after the pilot works well

## Success Criteria
- `20_Concepts/` becomes a concept network rather than a loose archive
- concept domains can support text, navigation, examples, comparisons, and visuals
- note placement becomes predictable
- module notes can link into a clearer reusable knowledge layer
- the structure remains lightweight enough to stay maintainable
- the architecture stays simple enough that both Tim and OpenCode can use it consistently without overhead fatigue
- optional structure appears only when the domain has earned it through real content

## Implementation TODO

### Phase 1 - Formalize the meta rules
- update `99_Meta/01_Architecture/Vault Architecture.md` with the role of `20_Concepts/` as a living domain-based knowledge network
- update `99_Meta/03_Content/Vault Content Conventions.md` with note-type and placement rules for `Topics/`, `Maps/`, `Comparisons/`, and `Execution/`
- update `99_Meta/02_Method/Study Didactics and Execution.md` so concept notes are expected to position ideas in a larger structure and highlight useful links or applications
- create or revise templates in `99_Meta/05_Templates/` for topic, map, comparison, and execution notes

### Phase 2 - Pilot the domain model
- use `20_Concepts/Machine Learning/` as the pilot domain
- move the overview note into `Maps/`
- keep stable atomic concepts in `Topics/`
- create `Comparisons/` only when the first comparison note is ready
- create `Execution/` only when the first execution note is ready
- keep visual support embedded unless a separate visual structure becomes clearly useful

### Phase 3 - Validate the model
- check whether the pilot domain is easier to navigate and understand
- check whether parent-child patterns improve understanding without forcing rigid trees
- check whether the metadata remains light enough to maintain
- check whether OpenCode can surface analogies, contrasts, and big-picture links more reliably

### Phase 4 - Scale carefully
- apply the same model only to domains that benefit from it
- keep `Topics/` and `Maps/` as the default baseline
- add optional structure on demand, not in advance
