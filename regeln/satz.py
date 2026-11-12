class Regel:
    def __init__(
        self,
        regel_id: str,
        buch: str,
        stufe: str,
        text: str,
        pruefung: str,
    ) -> None:
        self.regel_id = regel_id
        self.buch = buch
        self.stufe = stufe
        self.text = text
        self.pruefung = pruefung


#muss hängt an einer prüfung. soll und kann stehen im beispiel oder nur als satz.
REGELN = (
    Regel(
        "kern_ohne_aussen",
        "1",
        "muss",
        "die rechnung importiert keine datenbank, kein web und kein framework.",
        "kern_import",
    ),
    Regel(
        "importe_ohne_kreis",
        "1",
        "muss",
        "importe zwischen den eigenen modulen bilden keinen kreis.",
        "zyklus",
    ),
    Regel(
        "name_sagt_die_sache",
        "2",
        "muss",
        "der name sagt die sache. "
        "funktion klein_mit_unterstrich, klasse gross am anfang.",
        "namen",
    ),
    Regel(
        "kommentar_kurz",
        "2",
        "muss",
        "kommentar nur wenn nötig: klein, kein leerzeichen nach #.",
        "kommentar",
    ),
    Regel(
        "fehler_nicht_schlucken",
        "2",
        "muss",
        "echte fehler werden geworfen. "
        "except ohne typ und except mit pass sind verboten.",
        "fehler",
    ),
    Regel(
        "zahl_mit_namen",
        "2",
        "muss",
        "eine zahl mit bedeutung ist eine konstante. 0 und 1 dürfen nackt stehen.",
        "konstante",
    ),
    Regel(
        "verhalten_dazustecken",
        "3",
        "soll",
        "verhalten als funktion oder feld. keine vererbungskette.",
        "flach",
    ),
    Regel(
        "muster_spaet",
        "3",
        "kann",
        "ein muster erst, wenn dieselbe verzweigung schon zweimal da ist.",
        "",
    ),
    Regel(
        "wert_eingefroren",
        "4",
        "muss",
        "ein wert ohne eigene lebenslinie ist eingefroren. "
        "die operation gibt denselben typ zurück.",
        "eingefroren",
    ),
    Regel(
        "namen_wie_die_sache",
        "4",
        "soll",
        "klassen und funktionen heissen wie die sache im auftrag.",
        "namen",
    ),
    Regel(
        "eine_art",
        "5",
        "kann",
        "dieselbe aufgabe immer auf dieselbe art. kein zweiter stil daneben.",
        "",
    ),
    Regel(
        "grenze_sichtbar",
        "5",
        "muss",
        "eine knappe grenze steht als konstante. der test wird rot, wenn sie reisst.",
        "konstante",
    ),
    Regel(
        "eine_stelle",
        "6",
        "soll",
        "ein wert, den zwei stellen gleich meinen, steht einmal.",
        "konstante",
    ),
    Regel(
        "struktur_test",
        "6",
        "muss",
        "ein test bewacht: kern ohne datenbank und web, importe ohne kreis.",
        "kern_import",
    ),
    Regel(
        "kleiner_umbau",
        "7",
        "soll",
        "umbau in kleinen schritten. neue funktion und umbau nicht im selben schritt.",
        "",
    ),
    Regel(
        "fehler_wird_test",
        "7",
        "soll",
        "ein fehler wird zuerst ein test, dann die korrektur.",
        "",
    ),
    Regel(
        "frueher_abbruch",
        "7",
        "soll",
        "früher abbruch statt verschachtelter bedingungen.",
        "",
    ),
    Regel(
        "eine_linie",
        "8",
        "soll",
        "ein entwurfsgedanke. der zweite bau stopft nichts nach.",
        "",
    ),
    Regel(
        "daten_zuerst",
        "8",
        "soll",
        "zuerst die daten, der ablauf bleibt kurz darüber.",
        "",
    ),
    Regel(
        "wissen_einmal",
        "9",
        "soll",
        "jedes wissen an einer stelle.",
        "konstante",
    ),
    Regel(
        "sofort_abbruch",
        "9",
        "muss",
        "eine falsche annahme bricht sofort ab.",
        "fehler",
    ),
    Regel(
        "schwelle_draussen",
        "9",
        "muss",
        "pfad, adresse und schwelle stehen nicht als literale in der rechnung.",
        "konstante",
    ),
)

BEKANNTE_PRUEFUNGEN = {
    "namen",
    "kommentar",
    "fehler",
    "konstante",
    "kern_import",
    "zyklus",
    "flach",
    "eingefroren",
}
