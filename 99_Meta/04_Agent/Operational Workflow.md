# Operational Workflow

## Purpose
Define how the vault should be used operationally, including routing, processing behavior, and sync-safe working rules.

## Scope
- default folder routing
- intake and processing workflow
- edit discipline for a multi-device vault
- high-level sync safety rules

## Out of Scope
- assistant tone and identity
- detailed sync incident recovery
- tags and note content conventions
- template structure

## Authority
Canonical for operational workflow in this vault.

## Related Documents
- `99_Meta/01_Architecture/Vault Architecture.md`
- `99_Meta/03_Content/Vault Content Conventions.md`

## Canonical Sync Model
- this vault is treated as a local filesystem
- it is synced in the background by the official Obsidian Sync service running on a separate headless device
- sync stays outside the assistant workflow
- if an Obsidian Sync conflict file appears, stop operations and alert the user

## Default Folder Routing
- `00_Inbox/` -> quick capture and raw intake
- `10_Modules/` -> course and module-specific notes
- `20_Concepts/` -> reusable cross-module concept notes
- `30_Resources/` -> attachments, screenshots, and supporting materials
- `99_Meta/` -> methods, conventions, workflows, and templates
- `Z_Archive/` -> inactive or retired material

## Intake Workflow
1. capture fast and imperfect input in `00_Inbox/`
2. route course-specific material to the correct module area
3. distill reusable ideas into `20_Concepts/` when they have lasting value
4. improve links and structure once the destination is clear

## Live Lesson Workflow (Default)
Use this flow as the default for active lessons in `10_Modules/`.

1. user starts a new OpenCode session inside the study vault
2. user runs `/class <module> <class>` to set the active lesson context
3. assistant creates the lesson folder in the target module and ensures a lesson note is present as the primary anchor file
4. assistant treats that module and lesson as the active context for the rest of the session
5. user gives exact instructions for what should be added to the lesson note while actively following the lesson
6. assistant applies fast, minimal edits only, without proactive synthesis during live capture
7. user runs `/class log` at the end of the lesson
8. assistant stores a log file of the lesson conversation in the active lesson folder
9. post-lesson processing such as summaries or concept extraction may happen afterward, but only on explicit request

### Guardrails For Live Lesson Sessions
- do not prefill or pre-structure lesson content unless explicitly requested
- do not auto-create concept notes or derivative notes during live capture
- prioritize fast, minimal edits that mirror the user's exact instructions
- every lesson folder must keep a lesson note present at all times
- lesson notes should be optimized for fast live capture first, with post-lesson synthesis sections kept separate
- assume the user is actively attending class and keep interruption cost low
- after `/class log`, keep the lesson context available for explicit post-lesson processing

## OpenCode Command Shortcuts For Class Sessions
These command intents are canonical in OpenCode chat:

- `/class <module> <class>`: create or activate a lesson context for the current session
- `/class log`: save the lesson conversation log into the active lesson folder

### `/class <module> <class>` Behavior
- treat user input as the active class context (module path plus lesson identifier)
- create or reuse the lesson folder inside the target module
- ensure the lesson folder contains a lesson note as its primary anchor file
- confirm the active context in one short line
- apply live-capture guardrails immediately
- avoid summaries, concept extraction, and proactive restructuring during the live part of the lesson unless explicitly requested

### `/class log` Behavior
- use the current active lesson context
- save the conversation log into the lesson folder as a markdown file
- keep the lesson context active after logging
- keep the option open to create a summary only when explicitly requested

## Editing Rules
- prefer small, targeted changes
- preserve the style already used in the target note or folder
- avoid broad refactors unless explicitly needed
- when uncertain, prefer temporary capture over premature restructuring

## Sync Safety Rules
- keep edits small and easy to validate in the local vault state
- treat sync as external background state
- if a sync conflict file appears, stop operations and alert the user

## Mobile Intake
- quick mobile capture defaults to `00_Inbox/Mobile-Capture.md` when applicable
- captured material should later be processed into its proper long-term location
