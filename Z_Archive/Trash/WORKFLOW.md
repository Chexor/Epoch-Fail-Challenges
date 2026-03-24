# WORKFLOW.md — StudyVault (Headless Obsidian Sync)

## Setup Truth

Deze vault wordt nu gesynct via **Obsidian Headless Sync** op ErikaHQ.

- Local vault path (ErikaHQ): `/home/chexor/Obsidian/StudyVault`
- Sync service: `obsidian-sync-study.service`
- Sync mode: `ob sync --continuous`

## Folder Routing (default)

- `00_Inbox/` → snelle capture, ruwe input
- `10_Modules/` → vak- en modulegebonden notities
- `20_Concepts/` → herbruikbare conceptnotes (cross-module)
- `30_Resources/` → bronnen, screenshots, attachments
- `99_Meta/` → methodes, templates, runbooks
- `Z_Archive/` → afgewerkte/oude inhoud

## Writing Rules

1. Werk met kleine, gerichte edits.
2. Gebruik bestaande stijl per map/note.
3. Geen massale refactors zonder expliciete vraag.
4. Bij twijfel: eerst in `00_Inbox/`, daarna verwerken.

## Sync Safety Rules

1. Vermijd tegelijk dezelfde file op meerdere hosts bewerken.
2. Heavy edits bij voorkeur op één host per sessie.
3. Geen `occ files:scan`-workarounds meer voor gewone study-notes.
4. Volg voor canonieke workflowregels `99_Meta/04_Agent/Operational Workflow.md`.

## Mobile/Discord intake

Snelle capture standaard naar:
- `00_Inbox/Mobile-Capture.md`

Daarna uitwerken naar `10_Modules/` en/of `20_Concepts/`.
