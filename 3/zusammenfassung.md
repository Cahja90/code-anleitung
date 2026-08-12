# Design Patterns - Gang of Four (1994)

> Vollständige Zusammenfassung. Autoren: Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides ("Gang of Four", GoF). Untertitel: *Elements of Reusable Object-Oriented Software*.
>
> Hinweis: Diese PDF ist ein gescanntes/bild-basiertes Dokument und ließ sich nicht als Text extrahieren. Diese Zusammenfassung basiert auf dem etablierten Inhalt des Werks.

## Kernbotschaft

Entwurfsmuster sind **bewährte, benannte Lösungen für wiederkehrende Entwurfsprobleme** im objektorientierten Design. Sie bilden ein gemeinsames Vokabular. Zwei zentrale Leitprinzipien des Buches:

1. **"Program to an interface, not an implementation."** (Gegen Schnittstellen, nicht gegen Implementierungen programmieren.)
2. **"Favor object composition over class inheritance."** (Komposition vor Vererbung bevorzugen.)

Dazu: Kapseln, was sich ändert ("encapsulate what varies").

---

## Aufbau jedes Musters
Jedes Muster wird beschrieben durch: Name, Intent (Absicht), Motivation, Applicability, Structure, Participants, Collaborations, Consequences, Implementation, Sample Code, Known Uses, Related Patterns.

Die 23 Muster gliedern sich in **Creational**, **Structural** und **Behavioral**.

---

## 1. Erzeugungsmuster (Creational) - Objekterzeugung entkoppeln

- **Abstract Factory:** Schnittstelle zum Erzeugen von Familien verwandter Objekte ohne konkrete Klassen zu nennen.
- **Builder:** Konstruktion eines komplexen Objekts von seiner Repräsentation trennen; schrittweiser Aufbau.
- **Factory Method:** Erzeugung an Unterklassen delegieren; eine Methode entscheidet, welche Klasse instanziiert wird.
- **Prototype:** Neue Objekte durch Klonen eines Prototyps erzeugen.
- **Singleton:** Genau eine Instanz mit globalem Zugriffspunkt. (Heute kritisch zu sehen - globaler Zustand, schlechte Testbarkeit.)

## 2. Strukturmuster (Structural) - Klassen/Objekte zu größeren Strukturen zusammensetzen

- **Adapter:** Schnittstelle einer Klasse in eine erwartete andere übersetzen.
- **Bridge:** Abstraktion von ihrer Implementierung entkoppeln, damit beide unabhängig variieren.
- **Composite:** Teil-Ganzes-Hierarchien als Baum; Einzelobjekt und Komposition einheitlich behandeln.
- **Decorator:** Verantwortlichkeiten dynamisch hinzufügen, flexible Alternative zur Vererbung.
- **Facade:** Eine vereinfachte, einheitliche Schnittstelle zu einem Subsystem.
- **Flyweight:** Viele feingranulare Objekte durch Teilen (geteilter Zustand) effizient handhaben.
- **Proxy:** Stellvertreter, der Zugriff auf ein Objekt kontrolliert (Lazy, Remote, Schutz, Caching).

## 3. Verhaltensmuster (Behavioral) - Zuständigkeiten und Kommunikation zwischen Objekten

- **Chain of Responsibility:** Anfrage entlang einer Handler-Kette, bis einer sie bearbeitet.
- **Command:** Anfrage als Objekt kapseln (parametrisierbar, Queue, Undo).
- **Interpreter:** Grammatik einer Sprache repräsentieren und Sätze interpretieren.
- **Iterator:** Sequenziellen Zugriff auf Elemente, ohne die innere Struktur offenzulegen.
- **Mediator:** Kommunikation zwischen Objekten bündeln, lose Kopplung.
- **Memento:** Internen Zustand erfassen und später wiederherstellen, ohne Kapselung zu brechen.
- **Observer:** 1-zu-n-Abhängigkeit; bei Zustandsänderung werden Abhängige benachrichtigt (Publish/Subscribe).
- **State:** Verhalten je nach internem Zustand ändern; Zustand als Objekt.
- **Strategy:** Familie austauschbarer Algorithmen kapseln; zentral für "encapsulate what varies".
- **Template Method:** Gerüst eines Algorithmus, Einzelschritte in Unterklassen.
- **Visitor:** Operation von der Objektstruktur trennen; neue Operationen ohne Strukturänderung.

---

## Wichtige Querschnitts-Lehren

- **Komposition > Vererbung:** Vererbung bricht Kapselung ("white-box reuse"); Komposition ("black-box reuse") ist flexibler und zur Laufzeit änderbar.
- **Gegen Schnittstellen programmieren:** reduziert Implementierungsabhängigkeiten.
- **Kapsele Variabilität:** Was sich ändern kann, hinter eine Schnittstelle isolieren (Strategy, Bridge, Factory).
- **Muster mit Bedacht einsetzen:** Patterns lösen reale Probleme - nicht überall vorab einbauen ("Overengineering"). Erst wenn die Variabilität/Komplexität es rechtfertigt.

---

## Die wichtigsten Lehren fürs tägliche Coden

1. **Gegen Abstraktionen/Interfaces programmieren**, nicht gegen Implementierungen.
2. **Komposition vor Vererbung** wählen.
3. **Variabilität kapseln** (Strategy/Factory/Bridge), statt mit `if/switch`-Typprüfungen zu verzweigen.
4. **Muster als gemeinsames Vokabular** nutzen (Name nennen, statt Mechanik zu erklären).
5. **Nicht überdesignen** - ein Muster nur einsetzen, wenn das Problem es erfordert.
