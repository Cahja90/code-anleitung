# Clean Architecture - Robert C. Martin (2018)

> Vollständige Zusammenfassung. Untertitel: *A Craftsman's Guide to Software Structure and Design*.

## Kernbotschaft

Gute Architektur minimiert die **Lebenszeit-Kosten** eines Systems und maximiert die **Produktivität der Entwickler**. Das Ziel von Architektur ist nicht, das System zum Laufen zu bringen, sondern **Optionen offen zu halten** und Entscheidungen so lange wie möglich zu verzögern. Die wichtigste Regel des ganzen Buches ist die **Dependency Rule**: Quellcode-Abhängigkeiten zeigen immer nach innen, Richtung höherer Policy (Geschäftsregeln) - niemals nach außen Richtung Details.

---

## Teil I - Einführung

### Kapitel 1: Was ist Design und Architektur?
- Es gibt **keinen Unterschied** zwischen "Design" und "Architektur". Architektur = die hochrangigen Strukturen, Design = die Details. Beide sind dasselbe Kontinuum.
- **Das Ziel:** "Die Struktur einer Software-Architektur dient dazu, die menschlichen Ressourcen zu minimieren, die nötig sind, um das System zu bauen und zu warten."
- Messgröße: Wenn die Produktivität pro Release sinkt, während die Mitarbeiterzahl steigt, ist die Architektur kaputt.

### Kapitel 2: A Tale of Two Values (Verhalten vs. Struktur)
- Jedes Softwaresystem liefert zwei Werte: **Behavior** (Verhalten/Features) und **Structure** (Architektur, die "weich" bleiben muss).
- **Wichtig:** Die Struktur ist langfristig der größere Wert. Ein Programm, das funktioniert, aber unmöglich zu ändern ist, wird wertlos. Ein Programm, das nicht funktioniert, aber leicht änderbar ist, kann zum Laufen gebracht werden.
- **Eisenhower-Matrix:** "Dringend" ist selten "wichtig". Features sind dringend, Architektur ist wichtig. Entwickler müssen für die Architektur kämpfen.

---

## Teil II - Programmierparadigmen (Die Bausteine)

### Kapitel 3-6: Die drei Paradigmen
Jedes Paradigma **nimmt dem Programmierer etwas weg**, es gibt nichts dazu:
- **Structured Programming** (Dijkstra): entzieht den ungezügelten `goto`-Sprung -> ermöglicht Zerlegung in beweisbare Einheiten. Basis für Testbarkeit (Falsifizierbarkeit statt Beweis).
- **Object-Oriented Programming**: entzieht den direkten Funktionszeiger (Transfer of Control) -> diszipliniert durch Polymorphismus. Der eigentliche Gewinn: **Dependency Inversion** - die Abhängigkeitsrichtung kann gegen den Kontrollfluss gedreht werden.
- **Functional Programming**: entzieht die Zuweisung (veränderlichen Zustand) -> Unveränderlichkeit. Wichtig für Nebenläufigkeit; Strategie: Mutability segregieren, Event Sourcing.

---

## Teil III - Design-Prinzipien (SOLID)

Die SOLID-Prinzipien sagen, wie Funktionen und Datenstrukturen zu Klassen gruppiert und wie diese Klassen verbunden werden.

- **SRP - Single Responsibility Principle:** Ein Modul sollte genau **einen Grund zur Änderung** haben = genau einem Akteur/Stakeholder gegenüber verantwortlich. (Nicht "eine Funktion tut eine Sache", das ist eine andere Ebene.)
- **OCP - Open-Closed Principle:** Software-Entitäten sollen **offen für Erweiterung, geschlossen für Modifikation** sein. Neues Verhalten durch Hinzufügen von Code, nicht durch Ändern bestehenden Codes. Erreicht durch Trennung in Komponenten und gerichtete Abhängigkeiten.
- **LSP - Liskov Substitution Principle:** Subtypen müssen für ihre Basistypen **substituierbar** sein. Verletzungen (z.B. Quadrat/Rechteck) erzwingen hässliche Sonderfälle.
- **ISP - Interface Segregation Principle:** Hänge nicht von Dingen ab, die du nicht benutzt. Schmale, klientenspezifische Interfaces statt fetter.
- **DIP - Dependency Inversion Principle:** Abhänge von **Abstraktionen**, nicht von Konkretem. Stabile Architektur referenziert keine volatilen konkreten Klassen. Die wichtigste Mechanik der Clean Architecture.

---

## Teil IV - Komponenten-Prinzipien

### Kohäsion (welche Klassen gehören in eine Komponente?)
- **REP - Reuse/Release Equivalence Principle:** Die Einheit der Wiederverwendung ist die Einheit des Release (versioniert, mit Release-Notes).
- **CCP - Common Closure Principle:** Klassen, die sich aus denselben Gründen und zu denselben Zeiten ändern, gehören zusammen (SRP auf Komponenten-Ebene).
- **CRP - Common Reuse Principle:** Klassen, die nicht gemeinsam genutzt werden, gehören nicht zusammen (ISP auf Komponenten-Ebene).
- Diese drei stehen in **Spannung** (Tension Diagram) - früh CCP-orientiert, mit Reife Richtung REP/CRP.

### Kopplung (Beziehungen zwischen Komponenten)
- **ADP - Acyclic Dependencies Principle:** **Keine Zyklen** im Komponenten-Abhängigkeitsgraphen. Zyklen mit DIP oder neuer Komponente brechen.
- **SDP - Stable Dependencies Principle:** In Richtung **Stabilität** abhängen. Stabilität = wie schwer eine Komponente zu ändern ist (viele eingehende Abhängigkeiten = stabil).
- **SAP - Stable Abstractions Principle:** Eine Komponente sollte so **abstrakt** wie sie **stabil** ist. Stabile Komponenten = abstrakt (Policy); instabile = konkret (Details).

---

## Teil V - Architektur (das Herzstück)

### Kapitel 15-16: Was ist Architektur? / Unabhängigkeit
- Architektur unterstützt: **Development, Deployment, Operation, Maintenance** - und hält **Optionen offen**.
- Eine gute Architektur erlaubt, dass die wichtigen Entscheidungen (Datenbank, Web-Framework, UI) **so spät wie möglich** und leicht reversibel getroffen werden.

### Kapitel 17-18: Boundaries (Grenzen ziehen)
- Architektur = die Kunst, **Grenzen** zu ziehen und das Überqueren teurer Grenzen zu kontrollieren. Grenzen trennen Dinge, die sich aus unterschiedlichen Gründen/Geschwindigkeiten ändern.
- **Plugin-Architektur:** Details (UI, DB) sind Plugins zur Geschäftslogik.

### Kapitel 19-20: Policy & Level / Business Rules
- **Policy** (Geschäftsregeln) ist der Kern. **Level** = Entfernung von Ein-/Ausgabe. Höhere Level = stabiler.
- **Entities** (unternehmensweite kritische Geschäftsregeln) und **Use Cases** (anwendungsspezifische Regeln) bilden den Kern. Use Cases kennen Entities, nicht umgekehrt.

### Kapitel 21-22: Screaming Architecture & The Clean Architecture
- **Screaming Architecture:** Die Verzeichnisstruktur soll den **Anwendungszweck** schreien (z.B. "Gesundheitssystem"), nicht das Framework ("Rails-App").
- **Das Kreis-Diagramm (die berühmte Grafik):** konzentrische Ringe von innen nach außen:
  1. **Entities** (Enterprise Business Rules)
  2. **Use Cases** (Application Business Rules)
  3. **Interface Adapters** (Controllers, Presenters, Gateways)
  4. **Frameworks & Drivers** (DB, Web, UI, Devices)
- **The Dependency Rule:** Abhängigkeiten zeigen **nur nach innen**. Innere Ringe wissen nichts von äußeren. Datenformate äußerer Ringe lecken nicht nach innen.

### Kapitel 23-29: Mechanik
- **Humble Object Pattern:** Schwer testbares (View) von testbarem (Presenter) trennen.
- **Partial Boundaries / Facades:** Grenzen können teil-implementiert werden, wenn volle Trennung (noch) zu teuer ist.
- **Main Component:** das schmutzigste Detail, der Einstiegspunkt, der alles verdrahtet (Dependency Injection).
- **Test Boundary:** Tests sind Teil des Systems; nicht über volatile Details (GUI) testen (Fragile Tests Problem).

---

## Teil VI - Details

- **Kapitel 30-32:** Die **Datenbank ist ein Detail.** Das **Web ist ein Detail.** **Frameworks sind Details.** Keines gehört in den Architektur-Kern. Heirate kein Framework (asymmetrische Beziehung).

## Teil VII / Kapitel 34: The Missing Chapter (Simon Brown)
- Paketstrukturierung: **Package by Layer** (schlecht), **Package by Feature**, **Ports and Adapters**, **Package by Component** (empfohlen). Architektur-Absicht muss durch Sichtbarkeitsmodifizierer **erzwungen** werden, nicht nur dokumentiert.

---

## Die wichtigsten Lehren fürs tägliche Coden

1. **Dependency Rule befolgen:** Geschäftslogik kennt keine Frameworks, DB oder UI.
2. **SOLID anwenden**, besonders DIP (gegen Abstraktionen programmieren) und SRP (ein Akteur pro Modul).
3. **Details verzögern:** DB/Web/Framework so spät und so isoliert wie möglich.
4. **Grenzen ziehen** zwischen Policy und Detail; Abhängigkeiten über Interfaces invertieren.
5. **Keine zyklischen Abhängigkeiten** zwischen Komponenten.
6. **Testbarkeit als Architekturziel:** nicht durch volatile Details testen.
7. **Architektur soll den Zweck schreien**, nicht das Framework.
