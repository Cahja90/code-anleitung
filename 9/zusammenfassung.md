# The Pragmatic Programmer - David Thomas & Andrew Hunt (20th Anniversary Edition, 2019)

> Vollständige Zusammenfassung. Untertitel: *Your Journey to Mastery*. Sammlung von ~100 Tipps für pragmatische, verantwortungsvolle Softwareentwicklung.

## Kernbotschaft

Ein pragmatischer Programmierer denkt **kritisch, verantwortungsvoll und anpassungsfähig**. Übergeordnete Maximen: **DRY** (keine Wissens-Duplikation), **Orthogonalität** (Entkopplung), **ETC** ("Easier To Change" - das Leitprinzip für gutes Design) und ständige Verbesserung des eigenen "Wissensportfolios".

---

## Kapitel 1: A Pragmatic Philosophy
- **It's Your Life / Take Responsibility:** Verantwortung übernehmen, Lösungen statt Ausreden ("provide options, don't make lame excuses").
- **Software Entropy - Don't Live with Broken Windows:** kaputte Stellen sofort reparieren, sonst verfällt das ganze System. Keine "Broken Windows" stehen lassen.
- **Stone Soup / Be a Catalyst for Change.**
- **Good-Enough Software:** Qualität bewusst als Anforderung handhaben; Nutzer einbeziehen, wann "gut genug" ist - nicht endlos vergolden.
- **Your Knowledge Portfolio:** regelmäßig in Lernen investieren, diversifizieren.
- **Communicate!** Wissen ist wertlos, wenn man es nicht vermitteln kann.

## Kapitel 2: A Pragmatic Approach
- **The Essence of Good Design - ETC:** *"Good design is easier to change than bad design."* Alle Designregeln sind Spezialfälle von ETC.
- **DRY - Don't Repeat Yourself:** *"Every piece of knowledge must have a single, unambiguous, authoritative representation within a system."* DRY betrifft **Wissen**, nicht nur Code.
- **Orthogonality:** unabhängige Komponenten; eine Änderung an einer Stelle soll andere nicht beeinflussen. Eliminiert Effekte zwischen unzusammenhängenden Dingen.
- **Reversibility:** keine Entscheidung in Stein meißeln; flexibel gegenüber Änderungen (es gibt keine endgültigen Entscheidungen).
- **Tracer Bullets:** früh ein dünnes, durchgängiges Ende-zu-Ende-Skelett bauen, das funktioniert, und dann ausbauen (im Gegensatz zum Wegwerf-Prototyp).
- **Prototypes and Post-it Notes:** Prototypen sind zum **Lernen** (wegwerfbar), nicht zum Behalten.
- **Domain Languages:** nahe an der Sprache der Domäne programmieren.
- **Estimating:** schätzen lernen, Einheiten bewusst wählen.

## Kapitel 3: The Basic Tools
- **Power of Plain Text**, **Shell Games**, **Power Editing** (Werkzeuge meistern).
- **Version Control - Always Use It.** Alles unter Versionskontrolle.
- **Debugging:** *"Fix the Problem, Not the Blame"*; nicht in Panik geraten; "select isn't broken" (das Problem liegt fast immer im eigenen Code, nicht im Tool/OS).
- **Text Manipulation**, **Engineering Daybooks** (Notizbuch führen).

## Kapitel 4: Pragmatic Paranoia
- *"You Can't Write Perfect Software."* - defensiv arbeiten.
- **Design by Contract (DbC):** Vor-/Nachbedingungen und Invarianten explizit machen.
- **Dead Programs Tell No Lies:** früh und laut abstürzen statt mit korruptem Zustand weiterlaufen ("crash early").
- **Assertive Programming:** Assertions für "das kann nie passieren".
- **How to Balance Resources:** wer Ressourcen allokiert, gibt sie frei; Ressourcen entkoppeln.
- **Don't Outrun Your Headlights:** in kleinen Schritten vorausschauen, nur so weit wie man sehen kann.

## Kapitel 5: Bend, or Break (Kopplung)
- **Decoupling:** lose Kopplung; **Tell, Don't Ask**; **Law of Demeter** (nicht durch Objektketten greifen).
- **Juggling the Real World:** ereignisgesteuert (Finite State Machines, Observer/Pub-Sub, Streams).
- **Transforming Programming:** Programme als Folge von Daten-**Transformationen** (Pipelines) denken.
- **Inheritance Tax:** Vererbung sparsam einsetzen; stattdessen Interfaces/Protocols, Delegation, Mixins/Traits.
- **Configuration:** externe Konfiguration für veränderliche Werte.

## Kapitel 6: Concurrency
- **Breaking Temporal Coupling:** Analyse von Workflow/Parallelität.
- **Shared State Is Incorrect State**; Aktoren/Prozesse statt geteiltem Zustand; **Blackboards**.

## Kapitel 7: While You Are Coding
- **Listen to Your Lizard Brain** (Intuition ernst nehmen).
- **Don't Program by Coincidence:** nur Code schreiben, den man **versteht** - nicht zufällig funktionierenden Code.
- **Algorithm Speed (Big-O)** abschätzen.
- **Refactor Early, Refactor Often** - Refactoring ist wie Gärtnern, nicht Big-Bang.
- **Test to Code:** Tests treiben Design; **Testing Is Not About Finding Bugs** sondern Feedback über Design; *"A Test Is the First User of Your Code."* Property-Based Tests; **Stay Safe Out There** (Security-Basics); **Name Things Well** (gute Namen, und umbenennen, wenn sie nicht mehr passen).

## Kapitel 8: Before the Project / Kapitel 9: Pragmatic Projects
- **The Requirements Pit:** Anforderungen werden mit Nutzern **entdeckt**, nicht gesammelt; "Programmers Help People Understand What They Want".
- **Don't Think Outside the Box - Find the Box** (Constraints klären).
- **Pragmatic Teams**, **Coconuts Don't Cut It** (kein Cargo-Kult), **Pragmatic Starter Kit:** Versionskontrolle, rücksichtslose & kontinuierliche Tests, **vollständige Automatisierung**.
- **Delight Your Users**; **Pride and Prejudice** - Sign Your Work (Verantwortung/Stolz auf die eigene Arbeit).

---

## Die wichtigsten Lehren fürs tägliche Coden

1. **ETC - Easier To Change:** im Zweifel die Option wählen, die spätere Änderungen erleichtert.
2. **DRY:** jedes Stück Wissen hat genau eine autoritative Quelle - keine Duplikation.
3. **Orthogonalität/Entkopplung:** unabhängige Module; Tell-Don't-Ask; Law of Demeter.
4. **Don't program by coincidence:** nur Code schreiben, den man wirklich versteht.
5. **Crash early & Design by Contract:** Annahmen mit Assertions/Verträgen absichern, bei Verletzung sofort abbrechen.
6. **Keine Broken Windows:** kleine Mängel sofort beheben.
7. **Tracer Bullets statt Big-Bang:** früh ein lauffähiges Ende-zu-Ende-Skelett; Prototypen wegwerfen.
8. **Refactor early/often, Tests als erster Nutzer, gute Namen, alles automatisieren & versionieren.**
