# Refactoring: Improving the Design of Existing Code - Martin Fowler (2000/2018)

welche zeilen im code stehen: [im_code.md](im_code.md).

> Vollständige Zusammenfassung. Mit Kent Beck u.a. Diese Ausgabe ist die Java-basierte Erstauflage; die Prinzipien gelten unverändert.

## Kernbotschaft

**Refactoring** = das Verändern der **internen Struktur** von Code, **ohne sein beobachtbares Verhalten zu ändern**, um ihn verständlicher und billiger änderbar zu machen. Es ist eine **disziplinierte Technik** in kleinen, verhaltenserhaltenden Schritten - abgesichert durch **Tests**. Refactoring ist kein separates Großprojekt, sondern ständige Hygiene während der Entwicklung.

---

## Kapitel 1: Ein einführendes Beispiel
- Fowler refaktoriert ein Beispiel (Video-Verleih) schrittweise: viele kleine Schritte, nach jedem laufen die Tests. Zeigt, wie aus verworrenem Code klare Struktur entsteht (Extract Method, Move Method, Replace Conditional with Polymorphism).

## Kapitel 2: Prinzipien des Refactorings
- **Definition:** Substantiv = eine kleine, verhaltenserhaltende Strukturänderung; Verb = solche Änderungen anwenden.
- **Die zwei Hüte (Two Hats):** Entweder **Feature hinzufügen** oder **refaktorieren** - nie beides gleichzeitig. Bewusst zwischen den Hüten wechseln.
- **Warum refaktorieren?** Verbessert Design, macht Code lesbar, hilft Bugs finden, beschleunigt Entwicklung.
- **Wann?** Nach der **Rule of Three** (beim dritten Mal Duplikation refaktorieren), beim Hinzufügen von Features, beim Bugfixing, beim Code Review - "Preparatory", "Comprehension", "Litter-Pickup"-Refactoring.
- **Voraussetzung:** **Selbsttestender Code.** Ohne verlässliche Tests kein sicheres Refactoring.
- Probleme/Trade-offs: Performance, Datenbanken, veröffentlichte Schnittstellen.

## Kapitel 3: Bad Smells in Code (Code-Gerüche) - die Diagnose
Hinweise, dass refaktoriert werden sollte (Auswahl der klassischen Smells):
- **Mysterious Name** - unklare Namen.
- **Duplicated Code** - dieselbe Struktur mehrfach.
- **Long Function / Long Method** - zu lange Funktionen.
- **Long Parameter List** - zu viele Parameter.
- **Global Data / Mutable Data** - schwer nachvollziehbarer Zustand.
- **Divergent Change** (eine Klasse ändert sich aus vielen Gründen) und **Shotgun Surgery** (eine Änderung erzwingt viele kleine Edits) - gegensätzliche Probleme.
- **Feature Envy** - Methode interessiert sich mehr für eine andere Klasse.
- **Data Clumps** - dieselben Datenfelder treten immer zusammen auf.
- **Primitive Obsession** - Primitive statt kleiner Objekte.
- **Switch Statements / Repeated Switches** - oft Polymorphismus-Kandidaten.
- **Large Class**, **Lazy Element**, **Speculative Generality** (auf Vorrat gebaut), **Temporary Field**, **Message Chains**, **Middle Man**, **Insider Trading**, **Comments** (oft Deodorant für schlechten Code), **Refused Bequest**.

## Kapitel 4: Building Tests
- Selbsttestender Code ist die Grundlage. Tests vor dem Refactoring schreiben/haben. Tests sollen schnell laufen und **risikobehaftete Stellen** abdecken; jeder gefundene Bug bekommt erst einen Test.

## Kapitel 5+: Der Katalog (über 70 Refactorings)
Beispiele der wichtigsten Refactorings, jeweils mit Name, Motivation, Mechanik, Beispiel:
- **Extract Function/Method** und sein Gegenstück **Inline Function** - das fundamentalste Refactoring.
- **Extract Variable / Inline Variable**, **Rename Variable/Function** (Namen verbessern).
- **Move Function/Field**, **Move Statements**.
- **Replace Temp with Query**, **Split Variable**.
- **Encapsulate Variable / Encapsulate Record / Encapsulate Collection**.
- **Replace Primitive with Object**, **Introduce Parameter Object**, **Preserve Whole Object**.
- **Decompose Conditional**, **Consolidate Conditional Expression**, **Replace Conditional with Polymorphism**, **Introduce Special Case (Null Object)**, **Replace Nested Conditional with Guard Clauses**.
- **Replace Type Code with Subclasses**, **Pull Up / Push Down Method/Field**, **Extract Superclass/Class**, **Replace Inheritance with Delegation** und umgekehrt.
- **Separate Query from Modifier**, **Parameterize Function**, **Remove Flag Argument**.

---

## Die wichtigsten Lehren fürs tägliche Coden

1. **In kleinen, verhaltenserhaltenden Schritten** arbeiten; nach jedem Schritt Tests laufen lassen.
2. **Selbsttestender Code** ist Pflicht - ohne Tests kein sicheres Refactoring.
3. **Die zwei Hüte trennen:** Feature-Arbeit und Refactoring nie vermischen (auch nicht im selben Commit).
4. **Code Smells als Signale** lesen (lange Funktionen, Duplikation, Feature Envy, Primitive Obsession ...).
5. **Extract Function** als wichtigstes Werkzeug; **sprechende Namen** statt Kommentare.
6. **Rule of Three:** spätestens beim dritten Auftreten Duplikation beseitigen.
7. **Continuous Refactoring:** vor einer Änderung den Code "aufräumen" (Preparatory Refactoring), damit die Änderung leicht wird.
