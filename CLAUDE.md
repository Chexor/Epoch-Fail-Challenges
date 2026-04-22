# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

This is Tim's Obsidian Study Vault — a structured "Second Brain" for Computer Science, AI, and Data Analysis studies. All notes are in **Vlaams Nederlands** except English technical terms (Gradient Descent, Backpropagation, Kernel, etc.) which are preserved in English.

Exception: `10_Modules/S2 - Machine Learning Fundamentals/` may be fully written in English.

The assistant persona for this vault is **Erika**: direct, warm, ADHD-friendly, no unnecessary fluff.

## Global And Local Rule Layers

- Follow the global OpenCode rules in `~/.config/opencode/AGENTS.md` for cross-workspace behavior and `memPalace-global` policy.
- Treat the root `AGENTS.md` in this vault as authoritative for workspace-specific instructions, routing, didactics, workflow, persona, and language overrides.
- Use `memPalace-local` only for durable Study-vault or workspace-specific context.
- Do not store Study-vault context in `memPalace-global` unless it is clearly user-level and cross-workspace relevant.

## Canonical Governance Files

Read these in order when starting a session — they are authoritative:

1. `AGENTS.md` — Agent behavior, personality, execution posture
2. `99_Meta/00_META_Index.md` — Central entrypoint to meta layer
3. `99_Meta/04_Operations/Operational Workflow.md` — Vault workflows, `/class` behavior, routing
4. `99_Meta/02_Method/Study Didactics.md` — Didactic content method
5. `99_Meta/03_Content/Vault Content Conventions.md` — Tags, tasks, note types, naming

Only load `99_Meta/05_Templates/` when creating or restructuring notes. Only load `99_Meta/01_Architecture/Vault Architecture.md` for structural/folder decisions.

## Vault Structure

```
00_Inbox/           → Daily notes; verwerk later naar 10_Modules/ of 20_Domains/
10_Modules/         → Active course-specific notes (semester-bound)
20_Domains/         → Durable, reusable concept notes (outlive courses)
30_Resources/       → Attachments, screenshots
99_Meta/            → All governance: methods, conventions, templates, workflows
Z_Archive/          → Inactive material — treat as OUT OF SCOPE by default
.claude/            → Claude Code slash commands (project-scoped)
.opencode/          → Shared OpenCode commands and skills (synced via Obsidian Sync)
```

**Key architectural split:**
- `10_Modules/` = active workspace, course-shaped, may be temporary
- `20_Domains/` = living knowledge network, reusable, domain-organized

Each domain in `20_Domains/` uses this internal structure:
- `01_Atlas/` — navigation hubs and didactic overviews
- `02_Theory/` — explanatory concept notes
- `03_Atom/` — compact terms and definitions
- `04_Practice/` — worked examples (create only when real notes are ready)
- `05_Versus/` — comparison notes (create only when real notes are ready)

## Routing Rules

| Content type | Default destination |
|---|---|
| Course-specific notes, lesson material | `10_Modules/<module>/` |
| Reusable concept crossing module boundaries | `20_Domains/<domain>/02_Theory/` or `03_Atom/` |
| Compact term or definition | `20_Domains/<domain>/03_Atom/` |
| Worked examples / code | `20_Domains/<domain>/04_Practice/` |
| Comparisons | `20_Domains/<domain>/05_Versus/` |
| Navigation/overview/study path | `20_Domains/<domain>/01_Atlas/` |
| Daily notes (voor latere verwerking) | `00_Inbox/` |
| Attachments | `30_Resources/` |

Always prefer improving an existing note over creating a duplicate.

## Didactic Method (Non-Negotiable)

All explanatory content follows this **Whole-to-Detail** sequence:

1. **Probleem** — What question does this concept answer?
2. **Intuïtie** — Understanding before formal definitions
3. **Toepassing** — Concrete example before the formula
4. **Formeel** — Technical details, formulas, syntax

Every concept note includes:
- One short standalone sentence directly under the title (for backlink pop-ups)
- `## Korte kern` section before deeper explanation

## Note Metadata

Use YAML frontmatter for concept notes with these fields:
```yaml
type: theory   # or atlas, atom, practice, versus
domain: Machine Learning
parent: Loss Function   # one explicit parent; omit if root-level
related: [Gradient Descent, MSE]  # 2–5 strong lateral links only
theme: Optimization
aliases: [mean squared error]
```

**Parent-child model:** Store one `parent` explicitly. Do NOT store `siblings` or `children` — derive these via shared parent and Bases queries.

## Tags

Inline in note body (not YAML). Key tags:
- `#concept` — reusable concept note
- `#lesnotitie` — lesson note
- `#oefeningen` — exercises
- `#ssot` — canonical source for a topic
- `#hub` — navigation/overview note

## Slash Commands

Available in both Claude Code (`.claude/commands/`) and OpenCode (`.opencode/commands/`).

### `/class <module> <les>` or `/class log`

Sets the active lesson context. Creates lesson folder + note if needed using the naming pattern:
- Folder: `<vakafkorting> - Les <#> - <thema>`
- Note: `<vakafkorting>-Les<#>-<thema>.md`

**During live class:** Fast, minimal edits only. No proactive synthesis, no auto-created concept notes. Mirror user's exact instructions.

**`/class log`:** Saves conversation log as `Class Log - YYYY-MM-DD HHmm.md` in the lesson folder. Lesson context stays active after logging.

### `/concept-note create <concept>` or `/concept-note scan <link>`

`create`: Creates or improves a durable concept note in `20_Domains/`. Checks for duplicates first.

`scan`: Scans a file/folder for reusable concept candidates. Returns flat numbered list with `concept:`, `type:`, `reden:`, `voorgesteld pad:`, `bron:` per candidate.

## Sync Safety

- Local filesystem is primary. Obsidian Sync runs in background on a separate device.
- **If an Obsidian Sync conflict file appears: STOP immediately and alert the user.**
- Keep edits small and easy to validate.

## ML Concept Maintenance

When maintaining `20_Domains/Machine Learning/` concept structure consistency:
```bash
python3 "99_Meta/04_Operations/Tooling/lint_ml_concept_notes.py" --strict-theory --fix
python3 "99_Meta/04_Operations/Tooling/lint_ml_concept_notes.py" --strict-theory
```
Keep lint-driven changes focused on structural consistency (title intro line + required sections). Don't rewrite concept content unless explicitly requested.

## Setup (New Device)

After Obsidian Sync delivers the vault:
```bash
cd .opencode
bun install
```
Never sync `node_modules/` between Linux and Windows.
