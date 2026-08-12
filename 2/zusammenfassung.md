# Clean Code - Robert C. Martin (2008)

> Vollständige Zusammenfassung. Untertitel: *A Handbook of Agile Software Craftsmanship*.

## Kernbotschaft

Code wird **weit öfter gelesen als geschrieben** (Verhältnis ~10:1). Sauberer Code ist daher vor allem **lesbar, einfach und ausdrucksstark**. Unordnung ("the mess") kostet über die Zeit exponentiell Produktivität. Professionalität bedeutet, jederzeit sauberen Code zu liefern - die **Boy-Scout-Regel**: "Hinterlasse den Code sauberer, als du ihn vorgefunden hast."

---

## Kapitel 1: Clean Code
- Es wird immer Code geben; Anforderungen sind Code auf höchster Präzision.
- **Total Cost of Owning a Mess:** schlechter Code bremst das Team, bis die Produktivität gegen null geht. "The Grand Redesign in the Sky" (Neuschreiben) scheitert meist.
- Definitionen sauberen Codes von Größen (Bjarne Stroustrup: elegant & effizient; Grady Booch: lesbar wie Prosa; Kent Beck: macht eine Sache gut). Gemeinsam: **Care/Sorgfalt**.
- Wir sind **Autoren** - wir schreiben für Leser.

## Kapitel 2: Meaningful Names (Aussagekräftige Namen)
- **Intention-Revealing:** Namen sollen sagen, warum etwas existiert, was es tut, wie es benutzt wird.
- Keine **Desinformation**, sinnvolle **Unterscheidungen** (kein `a1, a2`, keine "noise words" wie `Info`, `Data`).
- **Aussprechbar** und **suchbar**. Keine Encodings (keine Ungarische Notation, keine Member-Präfixe).
- Klassennamen = Substantive, Methodennamen = Verben. Ein Wort pro Konzept. Keine Wortspiele. Kontext hinzufügen, aber nicht überflüssig.

## Kapitel 3: Functions (Funktionen) - das wichtigste Kapitel
- **Klein!** Funktionen sollen sehr klein sein (selten >20 Zeilen). Blöcke in `if/while` sind eine Zeile (ein Funktionsaufruf).
- **Do One Thing:** Eine Funktion tut **genau eine Sache** - auf **einer Abstraktionsebene**.
- **Stepdown Rule:** Code liest sich von oben nach unten wie eine Erzählung, jede Funktion eine Abstraktionsebene tiefer.
- **Argumente minimieren:** 0 (ideal) > 1 > 2 > 3 (vermeiden). Keine Flag-Argumente (bool). Argument-Objekte statt vieler Parameter.
- **Keine Seiteneffekte.** **Command-Query-Separation** (eine Funktion tut entweder etwas oder beantwortet etwas, nicht beides).
- **Exceptions statt Fehlercodes;** `try/catch`-Inhalt in eigene Funktionen extrahieren. **DRY** (keine Duplikation).

## Kapitel 4: Comments (Kommentare)
- "Kommentare sind bestenfalls ein notwendiges Übel." Sie kompensieren oft unser Versagen, uns im Code auszudrücken.
- **Gute Kommentare:** rechtliche, erklärende Absichten, Warnungen, TODOs, Verstärkung wichtiger Punkte, Doc-APIs.
- **Schlechte Kommentare:** redundante, irreführende, auskommentierter Code (löschen!), Tagebuch-/Mandats-Kommentare, Rauschen.
- Regel: **Erkläre dich im Code, nicht in Kommentaren.**

## Kapitel 5: Formatting (Formatierung)
- **Vertikale Formatierung:** Datei wie ein Zeitungsartikel (oben Überschrift/Abstraktes, unten Details). Zusammengehöriges nah beieinander; Konzepte durch Leerzeilen trennen.
- **Vertical Distance:** abhängige Funktionen nah; Aufrufer über Aufgerufenem.
- **Horizontale Formatierung:** kurze Zeilen. **Teamregeln** schlagen persönliche Vorlieben.

## Kapitel 6: Objects and Data Structures
- **Datenabstraktion:** Implementierung verbergen, nicht nur Getter/Setter draufsetzen.
- **Data/Object Anti-Symmetry:** Objekte verbergen Daten, exponieren Verhalten; Datenstrukturen exponieren Daten, kein Verhalten.
- **Law of Demeter:** "Sprich nur mit Freunden" - keine Ketten `a.getB().getC().doSomething()` (Train Wrecks).
- **DTOs** und **Active Records** sind reine Datenstrukturen - keine Geschäftslogik hineinmischen.

## Kapitel 7: Error Handling
- **Exceptions statt Rückgabecodes.** Erst `try-catch-finally` schreiben.
- **Keine `null` zurückgeben** und **kein `null` übergeben** - stattdessen Sonderfall-Objekte / Exceptions. Aussagekräftige Fehlermeldungen mit Kontext.
- Fehlerbehandlung ist **eine Sache** - in eigene Funktionen.

## Kapitel 8: Boundaries (Grenzen)
- Fremde Bibliotheken/APIs **kapseln** (z.B. nicht `Map` durchreichen). **Learning Tests** schreiben, um Drittanbieter-Verhalten zu lernen.
- Code gegen **eigene** Schnittstellen schreiben, die man kontrolliert (Adapter).

## Kapitel 9: Unit Tests
- **TDD-Gesetze:** (1) Kein Produktivcode ohne fehlschlagenden Test, (2) nur so viel Test, dass er fehlschlägt, (3) nur so viel Code, dass der Test grün wird.
- Testcode ist **so wichtig wie Produktivcode** - muss sauber gehalten werden.
- **F.I.R.S.T.:** Fast, Independent, Repeatable, Self-Validating, Timely.
- Ein **Concept pro Test**, möglichst eine Assertion. Tests halten den Code flexibel.

## Kapitel 10: Classes
- Klassen **klein** - gemessen an **Verantwortlichkeiten**, nicht Zeilen. **SRP**: ein Grund zur Änderung.
- Hohe **Kohäsion** (Methoden nutzen die Instanzvariablen). Für Wandel organisieren (OCP, DIP) -> testbar & isoliert.

## Kapitel 11: Systems
- Konstruktion von Verwendung trennen (**Dependency Injection**, Main-Setup). Skalierbarkeit durch saubere Abstraktionsschichten. "Frameworks erst dann, wenn nötig."

## Kapitel 12: Emergence (Einfaches Design)
Kent Becks vier Regeln einfachen Designs, nach Priorität:
1. **Tests bestehen** (Runs all the tests).
2. **Keine Duplikation** (DRY).
3. **Absicht ausdrücken** (Expressive).
4. **Minimale Anzahl Klassen/Methoden.**

## Kapitel 13: Concurrency
- Nebenläufigkeit entkoppelt Was von Wann, ist aber schwer. Geteilte Daten minimieren, Daten kopieren, kritische Bereiche klein. Concurrency-Code getrennt halten und gezielt testen.

## Kapitel 14-16: Fallstudien
- Schrittweises Refactoring realer Beispiele (Args-Parser, etc.): zeigt, wie man iterativ von "funktioniert" zu "sauber" kommt.

## Kapitel 17: Smells and Heuristics
- Umfangreiche Liste von **Code Smells** (Kommentare, Funktionen, allgemein, Java, Namen, Tests) - eine Referenz-Checkliste.

---

## Die wichtigsten Lehren fürs tägliche Coden

1. **Aussagekräftige Namen** überall - der billigste Hebel für Lesbarkeit.
2. **Kleine Funktionen, eine Aufgabe, eine Abstraktionsebene**, wenige Argumente, keine Seiteneffekte.
3. **Kommentare vermeiden** - lieber selbsterklärenden Code; auskommentierten Code löschen.
4. **DRY** - Duplikation ist der Erzfeind.
5. **Exceptions statt Fehlercodes; kein null** rein/raus.
6. **Tests sauber halten** (F.I.R.S.T.), TDD bevorzugen.
7. **Boy-Scout-Regel:** bei jeder Berührung etwas verbessern.
