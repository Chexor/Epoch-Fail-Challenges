# Obsidian CLI

## Purpose
Document the Obsidian CLI capabilities that are relevant when file operations should preserve vault-aware behavior.

## Scope
- targeting a vault or file
- safe file operations
- search and task commands
- diagnostics relevant to Obsidian CLI usage

## Out of Scope
- general policy
- sync incident recovery
- note conventions

## Authority
Canonical tooling reference for Obsidian CLI usage in this vault.

## Related Documents
- `99_Meta/04_Operations/Operational Workflow.md`

## Notes
- Obsidian 1.12 includes an `obsidian` CLI for scripting and automation
- when available, it can be safer than raw file moves because Obsidian may update links according to vault behavior
- the Obsidian app may need to be running

## Targeting
- if the terminal already points at the vault, the CLI can use that vault by default
- target a vault by name or id: `obsidian vault="My Vault" search query="TODO"`
- target a file by name: `obsidian read file=Recipe`
- target a file by vault-relative path: `obsidian read path="20_Domains/Recipe.md"`

## File Operations

```bash
obsidian rename path="20_Domains/Old Name.md" name="New Name"
obsidian move path="20_Domains/Note.md" to="10_Modules/Module X/Notes/"
obsidian create path="20_Domains/New Note.md" content="# New Note\n"
obsidian append path="20_Domains/Note.md" content="\n- [ ] Follow up"
obsidian prepend path="20_Domains/Note.md" content="- status: draft"
```

## Search And Tasks

```bash
obsidian search query="meeting notes"
obsidian search:context query="TODO"
obsidian tasks todo
obsidian tasks daily
obsidian task ref="20_Domains/Note.md:12" toggle
```

## Diagnostics

```bash
obsidian version
obsidian help rename
obsidian reload
obsidian plugin:reload id=opencode-obsidian
obsidian devtools
```
