# Installation — CODE ANLEITUNG in Cursor

Ziel: Die Datei `clean-code-framework.mdc` landet in den Cursor-Rules,
damit die KI die Regeln **automatisch** anwendet (`alwaysApply: true`).

## Voraussetzungen

- [Cursor](https://cursor.com) installiert  
- Dieses Repo geklont oder als ZIP entpackt  

## 1. Projekt-Installation (Team / ein Repo)

Im Verzeichnis deines Projekts:

**Windows (PowerShell)**

```powershell
# von überall, Pfad zum Klon anpassen:
& "D:\Pfad\code-anleitung\INSTALL.ps1" -TargetProject "D:\Pfad\dein-projekt"
```

**macOS / Linux**

```bash
/pfad/code-anleitung/INSTALL.sh /pfad/dein-projekt
```

Ergebnis:

```
dein-projekt/
  .cursor/
    rules/
      clean-code-framework.mdc
    coding-standards.json    # optional, Referenz
```

Committe `.cursor/rules/clean-code-framework.mdc` mit, wenn das Team denselben
Maßstab haben soll.

## 2. Globale Installation (alle Projekte auf dem Rechner)

**Windows**

```powershell
.\INSTALL.ps1 -Global
```

→ `%USERPROFILE%\.cursor\rules\clean-code-framework.mdc`

**macOS / Linux**

```bash
./INSTALL.sh --global
```

→ `~/.cursor/rules/clean-code-framework.mdc`

## 3. Nach der Installation

1. Cursor neu starten oder Fenster neu laden  
2. Neuen Agent-/Chat starten  
3. Kurz prüfen: Agent sollte MUST/SHOULD-Regeln aus dem Framework beachten  

Optional die Ordner `1`–`9` und `coding-standards.json` im Repo lassen —
zum Nachschlagen und für tiefere Begründungen. Die **aktive** Steuerung ist die `.mdc`.

## Deinstallieren

- Projekt: `.cursor/rules/clean-code-framework.mdc` löschen  
- Global: dieselbe Datei unter `~/.cursor/rules/` löschen  
