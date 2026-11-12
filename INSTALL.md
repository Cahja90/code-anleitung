# Installation — CODE ANLEITUNG

Nach dem Klonen die Regeln **ins Zielprojekt kopieren**. Nur Klonen reicht nicht:
die KI liest die `.mdc` erst, wenn sie in `.cursor/rules/` liegt.

Ob der Code in diesem Repo die Regeln hält: `python -m unittest`.

## Voraussetzungen

- [Cursor](https://cursor.com) (für die automatische Anwendung)
- Dieses Repo geklont oder als ZIP entpackt

Ohne Cursor: trotzdem `_framework/schreibweise.mdc` und `_framework/editorconfig`
ins Projekt legen — Editor und Menschen folgen denselben Tabellen.

## 1. Ein Projekt (empfohlen)

Im Verzeichnis des **Zielprojekts**:

**Windows (PowerShell)**

```powershell
git clone https://github.com/Cahja90/code-anleitung.git
& ".\code-anleitung\INSTALL.ps1" -TargetProject "D:\Pfad\dein-projekt"
```

**macOS / Linux**

```bash
git clone https://github.com/Cahja90/code-anleitung.git
./code-anleitung/INSTALL.sh /pfad/dein-projekt
```

Ergebnis:

```
dein-projekt/
  .editorconfig
  .cursor/
    rules/
      clean-code-framework.mdc
      schreibweise.mdc
    coding-standards.json
```

Diese Dateien **mitcommitten**, damit das Team denselben Maßstab hat.

## 2. Global (alle Cursor-Projekte auf dem Rechner)

**Windows**

```powershell
.\INSTALL.ps1 -Global
```

**macOS / Linux**

```bash
./INSTALL.sh --global
```

→ `~/.cursor/rules/clean-code-framework.mdc`  
→ `~/.cursor/rules/schreibweise.mdc`

## 3. Nach der Installation

1. Cursor neu starten oder Fenster neu laden
2. Neuen Agent-/Chat starten
3. Prüfen: neue Namen `snake_case`, Kommentare klein ohne Leerzeichen nach `#`

Die **aktive** Steuerung sind die beiden `.mdc`. Ordner `1`–`9` und
`coding-standards.json` sind Nachschlagewerk.

## Deinstallieren

- Projekt: `.cursor/rules/clean-code-framework.mdc` und `schreibweise.mdc` löschen
- Global: dieselben Dateien unter `~/.cursor/rules/`
- `.editorconfig` nur löschen, wenn es aus diesem Pack stammt
