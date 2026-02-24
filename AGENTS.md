# AGENTS

This repository is an Obsidian study vault, not a software project.
Use this file to guide agentic edits and keep the vault consistent.

## Build, lint, test
- There is no build system in this repository.
- There are no linting commands.
- There are no automated tests.
- Single test execution is not applicable.
- If you add a build or test tool in the future, update this section.

## Repository overview
- Primary content is Markdown notes and PDFs.
- Notes are organized by domain folders (e.g., 10_Modules, 20_Concepts).
- Obsidian features are used (wiki links, checkboxes, callouts if added).
- This is a personal knowledge base, not an app or library.

## Required policy sources
- Cursor rules: none found (.cursor/rules or .cursorrules not present).
- Copilot rules: none found (.github/copilot-instructions.md not present).
- If these files are added later, incorporate them here.

## Writing style
- Write in clear, concise Dutch or English depending on the note context.
- Match the language of the file you are editing.
- Keep explanations direct and study-focused.
- Prefer short paragraphs and scan-friendly sections.
- Use emphasis sparingly to highlight key ideas.
- Notes must be ADHD-friendly at all times.

## Markdown formatting
- Use Markdown headings for structure (#, ##, ###).
- Keep heading hierarchy consistent within a file.
- Use unordered lists for key points.
- Use task lists for actionable items or study tasks.
- Use horizontal rules only for major section breaks.
- Avoid excessive nested lists; keep lists shallow.

## Note structure
- Start each note with a single H1 title.
- Keep sections focused and logically ordered.
- Use short lead-in sentences before dense lists.
- Prefer one concept per section where possible.
- Avoid wall-of-text paragraphs; split for readability.
- Use clear headings and frequent visual breaks to reduce cognitive load.

## Lists and emphasis
- Use lists for definitions, steps, and key takeaways.
- Keep list items parallel in tense and phrasing.
- Use bold for key terms on first mention.
- Use italics for short clarifications, not for emphasis blocks.
- Avoid mixing multiple emphasis styles in one sentence.

## Tables and callouts
- Use tables only when comparisons benefit from alignment.
- Keep tables small and readable; avoid large multi-line cells.
- Use callouts sparingly and only for true warnings or tips.
- Keep callout text concise and actionable.

## Links and references
- Prefer internal wiki links over raw file paths.
- Link to existing concepts instead of creating duplicates.
- Keep external links stable and descriptive.
- If you add a URL, include a short label for context.

## Images and attachments
- Store images in 30_Resources/Images.
- Reference images with relative links from notes.
- Do not edit or recompress images unless requested.
- Prefer descriptive filenames for new images.

## Metadata and frontmatter
- Do not add frontmatter unless an existing note uses it.
- If frontmatter is present, preserve field order.
- Keep metadata minimal and consistent across similar notes.

## Obsidian conventions
- Use wiki links for internal references (e.g., [[Meetniveaus]]).
- Do not break existing wiki links when renaming files.
- If you must rename a note, update all backlinks.
- Prefer linking to existing concept notes in 20_Concepts.
- Keep backlinks meaningful; avoid linking every occurrence.

## File naming
- Respect existing naming patterns in each folder.
- Use spaces in filenames when that folder already does.
- Use underscores only when consistent with nearby files.
- Avoid renaming files without a clear benefit.
- Keep names short, descriptive, and searchable.

## Folder placement
- Concepts go in 20_Concepts.
- Module-specific notes go in 10_Modules/<Module>/Notes.
- Exercises go in 10_Modules/<Module>/Oefeningen.
- Tasks and quizzes go in 10_Modules/<Module>/Tasks.
- Templates go in 99_Meta/Templates.
- Images belong in 30_Resources/Images.

## Imports and code
- There are no code imports in this repository.
- If you add code snippets, use fenced code blocks with language tags.
- Keep snippets minimal and relevant to the note.
- Avoid introducing new dependencies or tooling unless required.
- If adding scripts, document how to run them in this file.

## Types and notation
- Use standard statistical notation where appropriate.
- Define symbols the first time they appear in a note.
- Keep formulas readable and aligned with the source material.
- Prefer plain text math unless the file already uses LaTeX.

## Naming conventions
- Use consistent terminology for key concepts.
- Keep chapter references consistent (e.g., H1, H2).
- Avoid mixing synonyms for the same concept in one note.
- Use title-style capitalization for headings when consistent.
- Keep note titles aligned with existing module structure.

## Error handling and corrections
- If correcting a mistake, explain the fix briefly.
- Do not delete large sections without providing a reason.
- Preserve original intent; improve clarity rather than rewrite.
- When unsure, add a short question or TODO in the note.

## Data integrity
- Do not alter PDF or image assets unless requested.
- Do not mass-edit vault content without explicit instruction.
- Keep links and references intact when reorganizing.

## Templates and checklists
- Follow existing templates when creating new module notes.
- Use checkboxes for actionable items and deadlines.
- Keep template sections in the same order as the template file.

## Editing workflow
- Make the smallest change that achieves the goal.
- Keep changes localized to the requested files.
- Avoid introducing new structure unless it improves study flow.
- Validate links when you add or change them.

## If you add tooling later
- Add build, lint, and test commands here.
- Include a single-test example if a test runner exists.
- Describe required runtimes or package managers.
- Note any formatting or lint rules to keep in sync.

## Contact and ownership
- This is a personal study vault.
- Be conservative with refactors and reorganizations.
- Prefer clarity and consistency over novelty.
