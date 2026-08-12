# The Design of Design - Frederick P. Brooks Jr. (2010)

> Vollständige Zusammenfassung. Untertitel: *Essays from a Computer Scientist*. Vom Autor des "Mythical Man-Month".

## Kernbotschaft

Über viele Medien hinweg (Computerarchitektur, Software, Häuser, Bücher, Organisationen) folgt **gutes Design einem gemeinsamen, unsichtbaren Prozess**. Das wertvollste Gut eines Entwurfs ist seine **konzeptionelle Integrität** (conceptual integrity) - Einheit, Ökonomie, Klarheit. Brooks plädiert für ein **Design-Konzept** als reale, leitende Entität und gegen naive, rein rationale Prozessmodelle.

---

## Teil I - Modelle des Designens

### Das Rational Model und seine Schwächen (Kap. 1-3)
- **Das Rational Model:** Design als systematische Suche durch einen Entscheidungsbaum: Goal -> Desiderata -> Utility Function -> Constraints/Budgets -> Design Tree. Man optimiert eine Nutzenfunktion unter Nebenbedingungen.
- **Was daran falsch ist:** In der Realität sind die **Ziele beim Start unbekannt**, ändern sich; die Nutzenfunktion ist nicht im Voraus formulierbar; der Entwurfsraum ist nicht vorab bekannt. Das **Wasserfall-Modell** (Royce als Strohmann) ist deshalb fundamental fehlerhaft.
- Design ist tatsächlich **iterativ, inkrementell, explorativ** - Ziele und Lösung entwickeln sich gemeinsam.

### Requirements, Sin, and Contracts (Kap. 4)
- Anforderungen wachsen unkontrolliert ("requirements creep"). Mehr Anforderungen heißt nicht besseres Produkt; oft das Gegenteil. Der Designer muss aktiv **gegen Featuritis** arbeiten.

### Bessere Prozessmodelle (Kap. 5)
- Co-Evolution von Problem und Lösung; Boehms **Spiralmodell**, Risiko-getriebenes Vorgehen statt starrer Phasen.

## Teil II - Zusammenarbeit
- **Conceptual Integrity entsteht aus einem Geist (oder wenigen).** Teamdesign verwässert leicht die Einheit. Lösung: starke Architektenrolle, viel Kommunikation über das Design-Konzept. Telekollaboration ist möglich, aber spontane Begegnung ("water cooler") bleibt wertvoll.

## Teil III - Design-Perspektiven (die praktischsten Essays)

- **Rationalism vs. Empiricism (Kap. 8):** Brooks ist **Empiriker** - "Ich werde Fehler machen, also muss ich testen." Man kann Korrektheit nicht allein durch Nachdenken garantieren; prototypen und testen.
- **User Models - Better Wrong than Vague (Kap. 9):** Mach **explizite Annahmen** über Nutzer/Nutzung. Eine explizite (auch falsche) Annahme ist besser als eine vage, weil sie **kritisierbar und korrigierbar** ist.
- **The Budgeted Resource (Kap. 10):** Jeder Entwurf rationiert eine knappe Ressource (Geld, Bits, Gewicht, Zeit). Die **kritische Ressource explizit budgetieren** und überwachen.
- **Constraints Are Friends (Kap. 11):** Beschränkungen verkleinern den Suchraum und fördern Kreativität. Künstliche Grenzen können helfen, wenn echte fehlen.
- **Esthetics and Style (Kap. 12):** Eleganz und konsistenter Stil sind keine Dekoration - sie verbessern Verständlichkeit und Qualität.
- **Exemplars (Kap. 13):** Lernen an herausragenden Vorbildern/Referenzdesigns.
- **How Expert Designers Go Wrong (Kap. 14):** Erfahrung verleitet, alte Lösungen auf neue Probleme zu zwingen; Annahmen veralten.

## Teil IV-VI - Traumsystem, Große Designer, Fallstudien

- **Great Designs Come from Great Designers (Kap. 19):** Herausragende Designs stammen von **einzelnen großartigen Designern oder kleinen Teams**, nicht von Komitees/Prozessen. Daraus folgt: gute Designer fördern, ihnen Verantwortung geben.
- **Where Do Great Designers Come From? (Kap. 20):** Sie werden aktiv gefördert: früh fordern, mentoren, Karrierewege für Designer (nicht nur für Manager).
- **Fallstudien:** Strandhaus, IBM System/360 (geglückte konzeptionelle Integrität), OS/360 (Warnbeispiel), Buchdesign - zeigen, dass **mutige Entwurfsentscheidungen** einen Großteil der Qualität ausmachen.

## Durchgängiges Leitmotiv
> "Die mutigsten Designentscheidungen haben für einen hohen Anteil der Güte des Ergebnisses gesorgt." Große, bewusste Entscheidungen am Anfang prägen das Resultat mehr als viele kleine.

---

## Die wichtigsten Lehren fürs tägliche Coden

1. **Konzeptionelle Integrität zuerst:** Konsistenz und ein klares Leitkonzept schlagen Feature-Fülle und Cleverness.
2. **Iterativ statt Wasserfall:** früh eine einfache lauffähige Version, dann verfeinern; Ziele und Lösung gemeinsam entwickeln.
3. **Empirisch arbeiten:** Annahmen durch Prototypen/Tests prüfen, nicht auf Korrektheit "durch Nachdenken" vertrauen.
4. **Annahmen explizit machen** ("better wrong than vague") - so werden sie überprüfbar.
5. **Constraints aktiv nutzen** zur Eingrenzung des Lösungsraums; knappe Ressourcen bewusst budgetieren.
6. **Requirements-Disziplin:** Scope-Creep benennen und begrenzen.
7. **Wenige mutige Kernentscheidungen** sorgfältig treffen - sie bestimmen den Großteil der Qualität.
