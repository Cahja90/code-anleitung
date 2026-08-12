# The Mythical Man-Month - Frederick P. Brooks Jr. (1975 / Anniversary Ed. 1995)

> Vollständige Zusammenfassung. Untertitel: *Essays on Software Engineering*. Der wohl einflussreichste Essayband über das Management von Softwareprojekten.

## Kernbotschaft

Die großen Probleme großer Softwareprojekte sind **menschlich und kommunikativ**, nicht primär technisch. Das berühmteste Ergebnis ist **Brooks's Law**: *"Adding manpower to a late software project makes it later."* Und das wichtigste Qualitätsmerkmal eines Systems ist seine **conceptual integrity** (konzeptionelle Integrität).

---

## Die zentralen Essays

### Kap. 1: The Tar Pit
- Große Systemprogrammierung ist ein "Teergrube" - viele kleine Verstrickungen. Ein **Programming Systems Product** kostet ~9x mehr als ein einfaches Programm (Produkt + System = je ~3x).

### Kap. 2: The Mythical Man-Month (Brooks's Law)
- **Mensch-Monate sind kein austauschbares Maß** für Aufwand und Zeit. Aufgaben mit Kommunikations-/Sequenzabhängigkeiten lassen sich nicht beliebig parallelisieren.
- Hinzufügen von Leuten zu einem verspäteten Projekt verspätet es weiter (Einarbeitung + Kommunikations-Overhead, der quadratisch wächst).
- Schätzungen sind oft von Optimismus getrieben; Systemtest wird unterschätzt.

### Kap. 3: The Surgical Team
- **Kleine, scharfe Teams** sind produktiver. Mills' Vorschlag: ein "Chefchirurg" entwirft/schreibt das Wesentliche, das Team unterstützt spezialisiert. Verbindet Effizienz kleiner Teams mit Kraft größerer.

### Kap. 4: Aristocracy, Democracy, and System Design - **Conceptual Integrity**
- **"Conceptual integrity is the most important consideration in system design."**
- Besser ein System, das **eine** kohärente Idee von einem (oder wenigen) Köpfen widerspiegelt, als ein Sammelsurium vieler guter, aber unkoordinierter Ideen.
- Architektur (das "Was" für den Nutzer) von Implementierung trennen. Architektur darf "aristokratisch" von wenigen bestimmt werden.

### Kap. 5: The Second-System Effect
- Das **zweite System** ist das gefährlichste: Designer neigen dazu, es mit all den Ideen zu überladen, die beim ersten keinen Platz hatten -> Overengineering. Bewusst dagegen disziplinieren.

### Kap. 6-7: Passing the Word / Tower of Babel
- Die Architektur über präzise **schriftliche Spezifikationen (das Manual)** kommunizieren. Babel scheiterte an **Kommunikation und Organisation** - daher Projekt-Workbook, klare Kommunikationswege.

### Kap. 9: Ten Pounds in a Five-Pound Sack
- Ressourcen (damals Speicher) bewusst budgetieren. **"Representation is the essence of programming"** - die richtige Datenrepräsentation ist der Kern; gute Datenstrukturen machen Algorithmen einfach.

### Kap. 11: Plan to Throw One Away
- **"Plan to throw one away; you will, anyhow."** Der erste Wurf eines Systems ist selten der richtige - also für den Wegwurf/Prototyp planen. (Brooks relativiert das später Richtung iterativ/inkrementell statt großem Wegwurf.)
- **"The only constancy is change itself."** Für Wandel planen - System und Organisation.

### Kap. 13: The Whole and the Parts
- **"Designing the bugs out":** Fehler durch sauberes Design vermeiden, nicht nur später jagen. Komponenten- vor System-Debugging.

### Kap. 14: Hatching a Catastrophe
- **"How does a project get to be a year late? ... One day at a time."** Zeitpläne rutschen schleichend. Klare **Meilensteine** (scharf definiert, "messbar"), kein Vertuschen.

### Kap. 15: The Other Face
- Programme brauchen **Dokumentation**; Ideal: **selbst-dokumentierende Programme** (Struktur und Namen erklären sich selbst).

### Kap. 16-17: No Silver Bullet
- **Essence vs. Accident:** Die **essentielle** Komplexität von Software (Komplexität, Konformität, Wandelbarkeit, Unsichtbarkeit) lässt sich nicht durch ein einzelnes Werkzeug wegzaubern.
- **"There is no single development, in either technology or management technique, which by itself promises even one order-of-magnitude improvement in productivity."**
- Vielversprechende Ansätze: Kaufen statt Bauen, Rapid Prototyping, inkrementelles Wachstum ("grow, not build"), großartige Designer fördern.

---

## Die wichtigsten Lehren fürs tägliche Coden

1. **Conceptual Integrity über alles:** ein kohärentes, einheitliches Konzept schlägt eine Ansammlung unkoordinierter Features.
2. **Plan to throw one away:** erste Version als Prototyp behandeln; iterativ/inkrementell wachsen lassen.
3. **Second-System-Effekt vermeiden:** beim Neubau/Umbau nicht überladen - Disziplin gegen Featuritis.
4. **Repräsentation ist das Wesen:** zuerst die richtigen Datenstrukturen wählen - "show me your data".
5. **Designing the bugs out:** Qualität durch klares Design statt nur nachträgliches Debugging.
6. **Essentielle Komplexität managen** (No Silver Bullet): kein Werkzeug ersetzt durchdachtes Design.
7. **Selbst-dokumentierender Code** und klare schriftliche Spezifikation für gemeinsame Sprache.
