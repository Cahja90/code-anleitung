from dataclasses import dataclass

#grenze der rechnung
MAX_MENGE = 99


@dataclass(frozen=True)
class Menge:
    stueck: int

    def plus(self, andere: "Menge") -> "Menge":
        summe = self.stueck + andere.stueck
        if summe > MAX_MENGE:
            raise ValueError("menge über dem limit")
        return Menge(summe)


def preis(menge: Menge, stueckpreis: int) -> int:
    if menge.stueck < 0:
        raise ValueError("menge fehlt")
    if stueckpreis < 0:
        raise ValueError("preis fehlt")
    return menge.stueck * stueckpreis
