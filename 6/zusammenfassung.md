# Fundamentals of Software Architecture - Mark Richards & Neal Ford (2020)

welche zeilen im code stehen: [im_code.md](im_code.md).

> Vollständige Zusammenfassung. Untertitel: *An Engineering Approach*.

## Kernbotschaft

Softwarearchitektur = **Struktur + Architektur-Eigenschaften ("-ilities") + Architektur-Entscheidungen + Designprinzipien**. Es gibt keine "richtige" Architektur, nur die am wenigsten schlechte Menge von **Trade-offs**. Zwei Gesetze prägen das Buch:

- **Erstes Gesetz der Softwarearchitektur:** *"Everything in software architecture is a trade-off."* Alles ist ein Kompromiss.
- **Zweites Gesetz:** *"Why is more important than how."* Das **Warum** einer Entscheidung ist wichtiger als das Wie.

---

## Teil I - Grundlagen

- **Definition:** Architektur besteht aus Struktur (Stil), den geforderten **Architektur-Eigenschaften**, den **Entscheidungen** (Regeln/Constraints) und **Designprinzipien** (Leitlinien).
- **Erwartungen an Architekten:** Entscheidungen treffen, kontinuierlich analysieren, aktuell bleiben, Compliance sicherstellen, breite (nicht nur tiefe) technische Kenntnis, Geschäftsverständnis, zwischenmenschliche Fähigkeiten, Politik navigieren.
- **Architectural Thinking:** breites Wissen statt nur Tiefe; Trade-offs analysieren; Balance zwischen Architektur und (Hands-on) Coding.

## Teil II - Architektur-Eigenschaften (das Zentrum)

- **Architecture Characteristics ("-ilities"):** nicht-funktionale Anforderungen, die der Erfolg des Systems verlangt (z.B. Verfügbarkeit, Skalierbarkeit, Performance, Sicherheit, Wartbarkeit, Testbarkeit, Deployability, Elastizität).
- Sie sind: **nicht-domänenspezifisch**, beeinflussen die Struktur, sind **explizit oder implizit** verlangt.
- **Wichtigste Regel:** **Nie alle gleichzeitig maximieren** - sie konkurrieren. Wenige (idealerweise <7) **treibende** Eigenschaften priorisieren ("never shoot for the best, settle for the least worst").
- Charakteristika **identifizieren** (aus Domänen-Anliegen + Anforderungen), **messen** und **steuern** (Fitness Functions - automatisierte Tests für Architektur-Eigenschaften).

## Teil III - Komponenten

- **Component-Based Thinking:** Komponenten sind die Bausteine; identifizieren, Verantwortlichkeiten zuweisen.
- **Coupling:** Afferent (eingehend) und Efferent (ausgehend).
- **Connascence** (Meilir Page-Jones): Maß für Kopplung. **Static** (Name, Type, Meaning, Position, Algorithm) und **Dynamic** (Execution, Timing, Value, Identity) Connascence. Ziel: starke Connascence lokal halten, über Grenzen hinweg schwächen/verringern.
- Partitionierung: **technisch** (nach Schichten) vs. **domänenbasiert** (nach Fachbereichen) - das Buch tendiert zu domänenbasiert.

## Teil IV - Architektur-Stile

- **Architectural Quantum:** unabhängig deploybare Einheit mit hoher funktionaler Kohäsion und (bei Bedarf) eigenem Datenspeicher - misst, wie monolithisch/verteilt ein System ist.
- **Monolithische Stile:** Layered (geschichtet), Pipeline (Pipes & Filters), Microkernel (Plugin-Architektur).
- **Verteilte Stile:** Service-Based, Event-Driven (Broker/Mediator), Space-Based (für extreme Skalierung), Service-Oriented, **Microservices** (stark entkoppelt, eigener Bounded Context + Datenspeicher pro Service).
- Jeder Stil wird über **Star-Ratings** der Eigenschaften (Kosten, Skalierbarkeit, Performance, Testbarkeit, ...) verglichen - **Trade-off-Analyse** statt "Lieblingsstil".
- **Fallacies of Distributed Computing** beachten (Netz ist nicht zuverlässig/latenzfrei/unendlich, etc.).

## Teil V - Techniken & Soft Skills

- **Architecture Decisions:** als **ADR (Architecture Decision Records)** dokumentieren - Kontext, Entscheidung, Konsequenzen. Anti-Patterns: "Covering Your Assets", "Groundhog Day" (immer wieder dieselbe Diskussion), "E-mail-driven Architecture".
- **Analyzing Trade-offs:** modellieren, qualitative/quantitative Analyse, iterativ.
- **Architecture Risk:** Risiko-Matrix, Risk Storming (kollaborativ).
- **Diagramming & Presenting:** C4-Modell, UML-Maßhalten; gute Visualisierung; Storytelling.
- **Effective Teams:** Architekt setzt **Grenzen/Leitplanken** (zu viel = Kontrollfreak, zu wenig = "armchair architect"). Teamtypen, Pluralismus, Checklisten.
- **Developing a Career Path:** "20-minute rule", die "Technologie-Radar"-Idee, lebenslanges Lernen.

---

## Die wichtigsten Lehren fürs tägliche Coden

1. **Trade-offs explizit machen:** Es gibt keine perfekte Lösung; jede Wahl hat Vor- und Nachteile - benenne sie.
2. **Das Warum dokumentieren:** Entscheidungen mit Begründung festhalten (ADR-Stil).
3. **Wenige treibende Qualitätsziele** priorisieren statt alles zu maximieren.
4. **Kopplung bewusst steuern** (Connascence): starke Kopplung lokal, schwache über Modulgrenzen.
5. **Komponenten/Module um Domänen schneiden**, mit klaren Verantwortlichkeiten.
6. **Fitness Functions:** wichtige Architektur-Eigenschaften automatisiert prüfen.
7. **Kontext zählt:** Architekturentscheidungen sind immer ein Produkt ihres Umfelds - keine Cargo-Cult-Übernahme.
