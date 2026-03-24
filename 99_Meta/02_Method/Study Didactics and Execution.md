# Study Didactics and Execution

## Purpose
Define both the canonical study explanation method and how OpenCode should operationalize it.

## Scope
- didactic structure for study explanations and notes
- rules for moving from overview to detail
- active learning defaults
- cognitive load management
- context-aware execution by the AI

## Out of Scope
- tags, tasks, and note naming rules
- folder routing
- sync procedures
- general assistant identity and tone

## Authority
Canonical for study didactics and the AI's execution of that didactic method.

## Related Documents
- `99_Meta/01_Architecture/Vault Architecture.md`
- `99_Meta/03_Content/Vault Content Conventions.md`
- `99_Meta/04_Agent/Core Identity.md`

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

For concept notes in `20_Concepts/`, this positioning should make the big picture visible and link to related or parent concepts when that improves understanding.

### 3. Use a fixed explanation sequence
When generating study content, use this sequence unless the task clearly requires another format:

1. Core problem
2. Intuitive explanation
3. Formal structure
4. Application
5. Exam-oriented translation

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

## Execution Rules For OpenCode

### Context-first behavior
- check existing vault context before generating new explanation
- prefer building on existing notes over rewriting what already exists well
- make useful relationships explicit when they improve understanding

### Top-down execution
- start from orientation and structure before detail
- split large topics into subproblems or layers
- propose a hierarchy or canvas structure when a topic is complex

### Active learning defaults
- include retrieval prompts, exercises, mini-cases, or worked steps when useful
- explain the thinking process, not only the answer
- surface common mistakes when the material is exam-relevant

### Output discipline
- keep the explanation scan-friendly
- keep paragraphs short
- end with a concise recap, checklist, or next step when that improves usability

## Standard Output Triggers
- `study note` -> structured Markdown note following the didactic sequence
- `canvas structure` -> top-down node hierarchy
- `exercise block` -> exercise plus worked solution
- `review card` -> active recall prompts
- `overview` -> concept-first outline

## Decision Rule
If a future file overlaps with this document on study explanation behavior, this document wins unless root `AGENTS.md` explicitly says otherwise.
