# Study Didactics

## Purpose
Define the canonical didactic structure for study notes and explanations stored in this vault.

## Scope
- didactic structure for study explanations and notes
- rules for moving from overview to detail
- active learning expectations in study content
- cognitive load management in note structure

## Out of Scope
- tags, tasks, and note naming rules
- folder routing
- sync procedures
- general assistant identity and tone
- assistant execution behavior

## Authority
Canonical for the didactic structure expected in study content in this vault.

## Related Documents
- `99_Meta/01_Architecture/Vault Architecture.md`
- `99_Meta/03_Content/Vault Content Conventions.md`
- root `AGENTS.md`

## Core Principle
Prioritize understanding over memorization, structure over isolated facts, and application over passive reading.

## Didactic Method

### 1. Move from whole to detail
Always start with the larger picture before definitions, formulas, or technical detail.

The explanation should establish:
- the broader domain the topic belongs to
- the purpose of the topic
- the problem it solves

Only then zoom in on intuition, structure, examples, and technical detail.

### 2. Position every topic in a knowledge structure
Never explain a topic as if it floats on its own.

Always clarify:
- what prior knowledge is assumed
- where the topic fits within the course or domain
- what it connects to in the vault
- what later topics build on it

For concept notes in `20_Domains/`, this positioning should make the big picture visible and link to related or parent concepts when that improves understanding.

### 3. Use a fixed explanation sequence
When generating study content, use this sequence unless the task clearly requires another format:

1. Probleem — welke vraag beantwoordt dit concept?
2. Intuïtie — begrijpen vóór formaliseren
3. Toepassing — concreet voorbeeld vóór de formule
4. Formeel — definitie, formule, eigenschappen

### 4. Do not separate theory from use
Every meaningful topic should be tied to one of the following where relevant:
- a worked example
- an exercise
- a case
- a practical scenario

Avoid long theory dumps without application.

### 5. Keep the structure ADHD-friendly
- use short sections
- use clear headings
- use bullets and stepwise procedure where useful
- avoid text walls and needless repetition
- reduce cognitive overload wherever possible

## Standard Output Triggers
- `study note` -> structured Markdown note following the didactic sequence
- `canvas structure` -> top-down node hierarchy
- `exercise block` -> exercise plus worked solution
- `review card` -> active recall prompts
- `overview` -> concept-first outline

## Decision Rule
If a future file overlaps with this document on didactic note structure, this document wins. If the overlap is about assistant behavior or execution posture, root `AGENTS.md` wins.
