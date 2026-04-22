# Sync Runbook

## Purpose
Keep a user-facing reference note about sync handling without making sync part of the assistant workflow.

## Scope
- user reference for sync-related follow-up
- conflict awareness

## Out of Scope
- assistant operations
- automatic recovery steps
- server administration

## Authority
Reference note for the user. This file is not part of the assistant's active instruction load.

## Working Assumption
- the vault is treated as a local filesystem
- Obsidian Sync runs in the background on a separate system
- assistant actions should be based on the local vault state only

## If A Sync Conflict Appears
- stop editing the conflicted file
- inspect which note is the canonical current version
- resolve the conflict manually in Obsidian or by user review
- keep the assistant out of sync troubleshooting unless the user explicitly asks for document-level comparison help

## Note
This runbook stays in the vault as a user reference. The assistant should rely on `AGENTS.md` and `99_Meta/04_Operations/Operational Workflow.md` for active behavior.
