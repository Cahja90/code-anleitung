# Clean Code Framework

Destilliert aus **9 Standardwerken** — steuert den KI-Agenten beim Coden.

## Dateien

| Datei | Inhalt |
|-------|--------|
| `clean-code-framework.mdc` | Always-On Cursor-Rule (Struktur, Tests) |
| `schreibweise.mdc` | Always-On Cursor-Rule (Namen, Kommentare) |
| `editorconfig` | Vorlage für `.editorconfig` im Zielprojekt |
| `coding-standards.json` | Aggregierte Regeln (Themen + Schweregrad + Buch-Belege) |

Pro Buch zusätzlich im Repo-Root unter `1`–`9`:

- `zusammenfassung.md` — ausführliche Zusammenfassung  
- `rules.json` — Regeln dieses Buches  

## Installation

Siehe [../INSTALL.md](../INSTALL.md) bzw. `INSTALL.ps1` / `INSTALL.sh` im Repo-Root.

Kurz (Projekt):

```powershell
Copy-Item "_framework\clean-code-framework.mdc" "DEIN-PROJEKT\.cursor\rules\"
Copy-Item "_framework\schreibweise.mdc" "DEIN-PROJEKT\.cursor\rules\"
```

## Schweregrade

- **MUST** — hart  
- **SHOULD** — starke Default  
- **CONSIDER** — Heuristik  

## Pflege

1. Neue Erkenntnis → passende `N/rules.json`  
2. In `coding-standards.json` aggregieren  
3. Bei MUST-Änderungen auch die `.mdc` anpassen und neu installieren  
