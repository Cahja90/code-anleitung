# Clean Code Framework

Destilliert aus **9 Standardwerken**. Alltag ist [`regeln/satz.py`](../regeln/satz.py), nicht die lange Liste.

## Dateien

| Datei | Inhalt |
|-------|--------|
| `clean-code-framework.mdc` | kurze fassung für cursor, dieselbe wie `regeln/satz.py` |
| `schreibweise.mdc` | namen, kommentare, kurze texte |
| `editorconfig` | vorlage für `.editorconfig` im zielprojekt |
| `coding-standards.json` | langes nachlesen, nicht die tagesregel |

Pro Buch zusätzlich im Repo-Root unter `1`–`9`:

- `im_code.md` — die zeilen, die im code stehen
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
