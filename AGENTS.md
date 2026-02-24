# AGENTS

This repository is primarily an Obsidian study vault (Markdown notes + resources). There is also a small TypeScript Obsidian plugin under `.obsidian/plugins/opencode-obsidian/`.

## Core Mandates
- **Follow the vault:** Optimize for readable, ADHD-friendly notes; keep edits small and local.
- **Follow precedent:** Mimic the surrounding note style (Dutch/English, headings, list style, terminology).
- **Data integrity:** Do not modify PDFs/images unless explicitly asked.
- **Links stay valid:** When changing/adding links, ensure wiki links and URLs resolve.

## Repository Map
- Notes: typically under folders like `10_Modules/`, `20_Concepts/`, `99_Meta/`.
- Attachments: images live in `30_Resources/Images/`.
- Code: Obsidian plugin in `.obsidian/plugins/opencode-obsidian/` (TypeScript + Bun + esbuild).

## Required Policy Sources
- Cursor rules: none found (`.cursor/rules/` and `.cursorrules` not present).
- Copilot rules: none found (`.github/copilot-instructions.md` not present).

## Build / Lint / Test

### Vault content (root)
- Build: none.
- Lint: none.
- Tests: none.

### Obsidian plugin (`.obsidian/plugins/opencode-obsidian/`)
- Install: `bun install`
- Dev (watch rebuild): `bun run dev`
- Build (type-check + bundle): `bun run build` (outputs bundled `main.js`)
- Lint: none configured (formatting is convention-based; no ESLint/Prettier in repo).

Tests (Bun)
- Run all tests: `bun test`
- Run a single file: `bun test ./tests/ServerManager.test.ts` (note the leading `./`)
- Run a single test by name/regex: `bun test --test-name-pattern "Unicode path support"`
- Run tests by path substring filter: `bun test ServerManager` (runs matching files)
- Watch mode: `bun test --watch`

Notes for tests
- Plugin tests spawn `opencode`; ensure `opencode --version` works in your PATH or tests will fail.

### Plugin files of interest
- Source: `.obsidian/plugins/opencode-obsidian/src/`
- Tests: `.obsidian/plugins/opencode-obsidian/tests/`
- Build config: `.obsidian/plugins/opencode-obsidian/esbuild.config.mjs`
- Generated bundle: `.obsidian/plugins/opencode-obsidian/main.js` (do not edit by hand)

### Release/version scripts (plugin)
- `bun run version:patch|minor|major` will create commits/tags and push to remote.
- Do not run version scripts unless you intend to publish a release.

## Editing Workflow
- Prefer minimal diffs; avoid renames/moves unless requested.
- For notes: keep paragraphs short; prefer headings + lists; avoid deep nesting.
- For code: change the smallest surface area; keep behavior stable; add tests when fixing bugs.

## Markdown & Obsidian Conventions
- Each note starts with a single H1 title.
- Use `##` / `###` for structure; keep heading hierarchy consistent.
- Keep paragraphs short; prefer lists for scannability; avoid deep nesting.
- Preserve the note's language (Dutch/English) and terminology.
- Use wiki links for internal references (e.g. `[[Meetniveaus]]`); if renaming a note, update backlinks.
- Use task lists (`- [ ]`) for actionable study items.
- Images: store new images under `30_Resources/Images/`; do not edit/recompress existing media.
- Frontmatter: do not add unless the note already uses it; preserve key order when present.

## Vault Hygiene
- Do not mass-edit vault content unless explicitly asked.
- Avoid reorganizing folder structures; add new notes near related notes.
- Keep filenames consistent with the folder's existing convention (spaces vs underscores).

## Folder Placement (convention)
- Concepts: `20_Concepts/`
- Module notes: `10_Modules/<Module>/Notes/`
- Exercises: `10_Modules/<Module>/Oefeningen/`
- Templates: `99_Meta/Templates/`
- Images: `30_Resources/Images/`

## Links, References, Snippets
- Prefer internal wiki links over raw paths; link to existing notes instead of duplicating.
- When adding an external URL, include a short label/context.
- Code in notes: use fenced blocks with a language tag; keep snippets minimal and relevant.

## Code Style (TypeScript plugin)

### Scope
- This repo is note-first; only apply the TypeScript rules inside `.obsidian/plugins/opencode-obsidian/`.
- Prefer behavior-preserving changes; avoid broad refactors unless requested.

### Project structure
- Entry point: `src/main.ts` (extends Obsidian `Plugin`).
- UI: `src/ui/` (views, view manager).
- Server/process: `src/server/` (spawn/stop OpenCode, platform-specific process logic).
- Settings: `src/settings/`.
- Shared types/constants: `src/types.ts`.

### Imports
- No path aliases; use relative imports within `src/`.
- Prefer stable grouping: Node built-ins, third-party, Obsidian API, then local files.
- Keep import specifiers ordered and avoid unused imports.

### Formatting
- Match existing formatting: 2-space indent, semicolons, double quotes.
- Prefer trailing commas in multiline objects/arrays.
- Keep logs prefixed consistently (`[OpenCode]`, `[OpenCode Error]`).
- Do not hand-edit generated/bundled output: `.obsidian/plugins/opencode-obsidian/main.js`.

### Types
- `noImplicitAny` + `strictNullChecks` are enabled; handle `null`/`undefined` explicitly.
- Add explicit return types on exported/public methods (especially plugin API surface).
- Avoid `any`; use it only at Obsidian boundary points where types are missing (and keep it local).
- Prefer narrow unions for state (e.g. `"stopped" | "starting" | "running" | "error"`).

### Naming
- Classes / types / interfaces: `PascalCase`.
- Functions / variables: `camelCase`.
- Constants: `UPPER_CASE` (or existing camelCase constants in `src/types.ts`).
- Filenames: `PascalCase.ts` for class modules; `main.ts` as plugin entry.

### Error handling & UX
- Prefer `false`/`null` returns + `getLastError()` style access over throwing at runtime.
- Use `Notice` for user-facing failures (include actionable text, short duration).
- Log enough context for debugging (mode, command, cwd, port), but avoid leaking sensitive data.

### Error handling & logging
- Prefer predictable results over throwing in production code: return `false`/`null` and store an error string when needed.
- Use `Notice` for user-facing failures; use console logs with the `[OpenCode]` prefix for diagnostics.
- When spawning processes, handle early exits and timeouts explicitly.

### Async & lifecycle
- Use `async`/`await`; avoid blocking the UI thread.
- Register and clean up listeners (`this.registerEvent`, `offref`, `onunload`).
- For fire-and-forget async callbacks, use `void someAsync()` to make intent explicit.

### Obsidian API patterns
- `Plugin`: implement `onload()`/`onunload()`; register commands/views in `onload()`.
- Views: extend `ItemView`; implement `getViewType()` + `onOpen()`/`onClose()`.
- Settings: extend `PluginSettingTab`; implement `display()`.
- DOM: use Obsidian helpers (`createEl`, `createDiv`) over raw `document.createElement`.

### Tests
- Prefer Bun's `bun:test` APIs (`describe`, `test`, `beforeAll`, `afterEach`, `expect`).
- Keep tests hermetic and clean up spawned processes; avoid long sleeps unless necessary.
- Do not leave `test.only` / `describe.only` committed.

### Platform constraints
- Desktop-only plugin: `child_process` and filesystem access are not available on mobile.
- When adding OS-specific behavior, keep it behind `process.platform` checks and add tests when possible.
