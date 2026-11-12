import unittest
from pathlib import Path

from regeln.pruefen import finde_zyklen, pruefe_ordner, pruefe_text
from regeln.rechnung import MAX_MENGE, Menge, preis
from regeln.satz import BEKANNTE_PRUEFUNGEN, REGELN


class TestRechnung(unittest.TestCase):
    def test_plus_gibt_dieselbe_art(self) -> None:
        summe = Menge(2).plus(Menge(3))
        self.assertIsInstance(summe, Menge)
        self.assertEqual(summe.stueck, 5)
        self.assertEqual(preis(summe, 4), 20)

    def test_grenze_reisst(self) -> None:
        with self.assertRaises(ValueError):
            Menge(MAX_MENGE).plus(Menge(1))

    def test_falsche_annahme_bricht(self) -> None:
        with self.assertRaises(ValueError):
            preis(Menge(1), -1)


class TestPruefung(unittest.TestCase):
    def test_eigener_code_ist_sauber(self) -> None:
        ordner = Path(__file__).resolve().parent
        dateien = {
            pfad.name: pfad.read_text(encoding="utf-8")
            for pfad in sorted(ordner.glob("*.py"))
        }
        self.assertEqual(pruefe_ordner(dateien, {"rechnung.py"}), [])

    def test_jede_muss_regel_hat_eine_pruefung(self) -> None:
        buecher = set()
        for regel in REGELN:
            buecher.add(regel.buch)
            if regel.pruefung != "":
                self.assertIn(regel.pruefung, BEKANNTE_PRUEFUNGEN)
            if regel.stufe == "muss":
                self.assertNotEqual(regel.pruefung, "")
        self.assertEqual(buecher, {str(n) for n in range(1, 10)})

    def test_im_code_nennt_die_regel(self) -> None:
        wurzel = Path(__file__).resolve().parents[1]
        for regel in REGELN:
            text = (wurzel / regel.buch / "im_code.md").read_text(encoding="utf-8")
            self.assertIn(regel.regel_id, text)
            self.assertIn(regel.text, text)

    def test_schlechter_code_faellt_auf(self) -> None:
        proben = {
            "def ladeDaten():\n    return 1\n": "ladeDaten",
            "x = 1\n# kommentar\n": "leerzeichen",
            "try:\n    x = 1\nexcept:\n    pass\n": "except",
            "def rechne():\n    return 12\n": "nackte zahl",
            "import sqlite3\n": "sqlite3",
            "class Kind(Basis):\n    pass\n": "vererbung",
            "@dataclass\nclass Geld:\n    wert: int\n": "eingefroren",
        }
        for text, nadel in proben.items():
            funde = pruefe_text("rechnung.py", text, True)
            self.assertTrue(
                any(nadel in fund for fund in funde),
                msg=f"{nadel} fehlt in {funde}",
            )

    def test_zyklus(self) -> None:
        self.assertEqual(finde_zyklen({"a": {"b"}, "b": set()}), [])
        self.assertTrue(finde_zyklen({"a": {"b"}, "b": {"a"}}))


if __name__ == "__main__":
    unittest.main()
