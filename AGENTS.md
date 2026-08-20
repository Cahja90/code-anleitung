# Agent instructions

This repository is a **coding standard pack** for coding agents and developers.

Use it when the task is **coding**, code review, refactoring, naming, project
structure, or “how should this be written”.

## Read first

1. `_framework/clean-code-framework.mdc` — structure, tests, dependencies (MUST / SHOULD / CONSIDER)
2. `_framework/schreibweise.mdc` — names, comments, short text (MUST)
3. `_framework/coding-standards.json` — full rule set
4. Folders `1`–`9` — book-level why, only if needed

## Apply in a target project

Clone, then install into the project that should follow the rules:

```powershell
.\INSTALL.ps1 -TargetProject <path-to-project>
```

```bash
./INSTALL.sh /path/to/project
```

That copies:

- `.cursor/rules/clean-code-framework.mdc`
- `.cursor/rules/schreibweise.mdc`
- `.editorconfig` (only if missing)

Commit those files in the target repo. Restart Cursor / start a new chat.

Without Cursor: copy the two `.mdc` files and `editorconfig` the same way and
follow the tables by hand.

## Hard rules (short)

- New identifiers: `snake_case` functions/vars, PascalCase types, ALL_CAPS constants, lowercase files
- One name, one spelling. Copy existing names exactly. Do not rename working code for style
- Comments (when needed): lowercase, no space after `#` / `//` — `#lädt die daten`
- Markdown headings: space after `#` (`# titel`)
- Short everyday text in comments, commits, README — no hub/layer/center jargon
- Small functions; no silent `except:`; domain names
- Conflict order: correctness & tests > conceptual integrity > changeability > simplicity > local taste

Do **not** add book PDFs. Do **not** invent a second style next to this pack.
