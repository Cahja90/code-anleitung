# Domain-Driven Design - Eric Evans (2003)

welche zeilen im code stehen: [im_code.md](im_code.md).

> Vollständige Zusammenfassung. Untertitel: *Tackling Complexity in the Heart of Software*. Oft "the Blue Book" genannt.

## Kernbotschaft

Bei komplexer Software liegt die größte Herausforderung nicht in der Technik, sondern in der **Domäne** (dem Fachbereich) selbst. Der Schlüssel ist ein **Domänenmodell**, das eng mit dem Code verbunden ist und in einer **gemeinsamen Sprache** (Ubiquitous Language) zwischen Entwicklern und Fachexperten ausgedrückt wird. Das Modell ist nicht ein Diagramm, sondern die **Idee, die das Diagramm kommunizieren soll** - und es lebt im Code.

---

## Teil I - Modell und Sprache in Einklang bringen

### Crunching Knowledge (Wissen verdichten)
- Modellbildung ist ein **kollaborativer Lernprozess** mit Domänenexperten. Das Modell entsteht durch Iteration und ständige Verfeinerung der Begriffe.
- **Knowledge Crunching:** rohe Information in ein nützliches, abstraktes Modell verwandeln.

### Ubiquitous Language (Allgegenwärtige Sprache)
- **Eine gemeinsame, rigorose Sprache** für Team und Code. Dieselben Begriffe in Gesprächen, Dokumenten und im Code (Klassen, Methoden).
- Übersetzungslücken zwischen "Fach-Sprech" und "Entwickler-Sprech" erzeugen Fehler. Änderungen an der Sprache = Änderungen am Modell.

### Modell und Implementierung verbinden (Model-Driven Design)
- Das Modell muss sich **direkt im Code widerspiegeln**. **Hands-on Modelers:** wer modelliert, muss auch Code anfassen.

---

## Teil II - Bausteine eines modellgetriebenen Designs

### Layered Architecture
- Domänenlogik in eine eigene **Domain Layer** isolieren, getrennt von UI, Application und Infrastructure. Die Domänenschicht ist das Herz der Software.

### Die Building Blocks (das taktische DDD)
- **Entities:** Objekte mit durchgehender **Identität** über die Zeit (nicht durch Attribute definiert), z.B. Kunde, Bestellung.
- **Value Objects:** durch ihre **Attribute** definiert, keine Identität, idealerweise **unveränderlich** (z.B. Geldbetrag, Adresse). Frei austauschbar/kopierbar.
- **Services:** Operationen, die konzeptuell zu keinem Objekt gehören; zustandslos, in der Sprache der Domäne benannt.
- **Modules (Packages):** schneiden das Modell in kohäsive, lose gekoppelte Teile mit niedriger Kopplung, hoher Kohäsion.

### Aggregates (eines der wichtigsten Muster)
- Ein **Aggregate** ist ein Cluster zusammengehöriger Objekte mit einer **Aggregate Root** als einzigem Zugriffspunkt. Es definiert eine **Konsistenzgrenze** (Invarianten gelten innerhalb).
- Externe Objekte dürfen nur die Root referenzieren. Transaktionen/Invarianten respektieren Aggregat-Grenzen.

### Factories und Repositories
- **Factories:** kapseln komplexe Erzeugung von Objekten/Aggregaten, sodass Invarianten von Anfang an gelten.
- **Repositories:** liefern den Eindruck einer **In-Memory-Sammlung** für Aggregat-Roots; verbergen Persistenz. Nur Aggregat-Roots haben Repositories.

---

## Teil III - Refactoring toward Deeper Insight (Tieferes Verständnis)

- Modelle entwickeln sich durch **kontinuierliches Refactoring** und Durchbrüche ("Breakthroughs").
- **Implicit Concepts explizit machen:** verborgene Begriffe (oft Constraints, Prozesse, Spezifikationen) als eigene Modellelemente herausarbeiten.
- **Supple Design (geschmeidiges Design):** Design, das leicht zu ändern ist. Bausteine:
  - **Intention-Revealing Interfaces**, **Side-Effect-Free Functions**, **Assertions**, **Conceptual Contours**, **Standalone Classes**, **Closure of Operations**.
- **Specification Pattern:** Geschäftsregeln/Prädikate als Objekte kapseln.

---

## Teil IV - Strategic Design (Strategisches Design - bei großen Systemen)

### Bounded Context (das wichtigste strategische Muster)
- Jedes Modell gilt nur innerhalb eines **Bounded Context** - einer expliziten Grenze, in der die Ubiquitous Language konsistent ist. Derselbe Begriff kann in verschiedenen Kontexten Unterschiedliches bedeuten.
- **Context Map:** die Beziehungen zwischen den Bounded Contexts sichtbar machen.

### Context-Beziehungsmuster
- **Shared Kernel**, **Customer/Supplier**, **Conformist**, **Anticorruption Layer** (Schutzschicht gegen fremde Modelle), **Separate Ways**, **Open Host Service**, **Published Language**.

### Distillation (Destillation)
- **Core Domain:** das wertvollste, differenzierende Herzstück - die besten Kräfte dorthin.
- **Generic Subdomains**, **Domain Vision Statement**, **Highlighted Core**. Den Kern von unterstützenden Teilen trennen.

### Large-Scale Structure
- **Evolving Order**, **Responsibility Layers**, **Knowledge Level**, **Pluggable Component Framework**, um auch große Systeme verständlich zu halten.

---

## Die wichtigsten Lehren fürs tägliche Coden

1. **Ubiquitous Language:** Code-Bezeichner spiegeln die Fachbegriffe der Domäne wider (keine technischen Tarnnamen).
2. **Domänenlogik isolieren** in einer eigenen Schicht, frei von Infrastruktur.
3. **Entities vs. Value Objects** bewusst unterscheiden; Value Objects unveränderlich halten.
4. **Aggregates mit klaren Grenzen** und einer Root als Konsistenz-/Zugriffsgrenze; nur Roots über Repositories laden.
5. **Factories/Repositories** für Erzeugung und Persistenz - Geschäftslogik kennt keine DB-Details.
6. **Bounded Contexts** explizit machen; an Grenzen mit Anticorruption Layer schützen.
7. **Kern-Domäne fokussieren**, kontinuierlich Richtung tieferer Einsicht refaktorieren.
