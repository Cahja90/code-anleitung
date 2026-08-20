# Agent instructions

This repository is a **coding standard pack** for coding agents and developers.

Use it when the task is **coding**, code review, refactoring, naming, project
structure, or “how should this be written”.

## Read first

1. `_framework/clean-code-framework.mdc` — operating rules (MUST / SHOULD / CONSIDER)
2. `_framework/coding-standards.json` — full rule set
3. Folders `1`–`9` — book-level why, only if needed

## Apply in a target project

```powershell
.\INSTALL.ps1 -TargetProject <path-to-project>
```

```bash
./INSTALL.sh /path/to/project
```

That installs a Cursor always-on rule: `.cursor/rules/clean-code-framework.mdc`.

## Hard rules (short)

- Names from the domain; small functions; one thing per function
- No silent `except:` / swallowed errors
- Depend on abstractions; domain logic free of frameworks
- Tests and correctness before clever structure
- Conflict order: correctness & tests > conceptual integrity > changeability > simplicity > local taste

Do **not** add book PDFs. Do **not** invent a second style next to this pack.
