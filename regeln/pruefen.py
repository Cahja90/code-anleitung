import ast
import re
from pathlib import Path

VERBOTENE_IMPORTE = {
    "aiohttp",
    "django",
    "fastapi",
    "flask",
    "http",
    "requests",
    "sqlalchemy",
    "sqlite3",
    "urllib",
}
_SNAKE = re.compile(r"^[a-z_][a-z0-9_]*$")
_PASCAL = re.compile(r"^[A-Z][A-Za-z0-9]*$")
_KONSTANT = re.compile(r"^_?[A-Z][A-Z0-9_]*$")
_ADRESSE = re.compile(r"https?://|[A-Za-z]:\\|\\\\")
_ERLAUBTE_ZAHL = {-1, 0, 1}


def pruefe_ordner(dateien: dict[str, str], kern: set[str]) -> list[str]:
    funde: list[str] = []
    module = {name[:-3] for name in dateien if name.endswith(".py")}
    kanten: dict[str, set[str]] = {}
    for name in sorted(dateien):
        if not name.endswith(".py"):
            continue
        text = dateien[name]
        funde.extend(pruefe_text(name, text, name in kern))
        kanten[name[:-3]] = lokale_importe(text, module)
    for zyklus in finde_zyklen(kanten):
        funde.append(f"zyklus: {zyklus}")
    return funde


def pruefe_text(name: str, text: str, kern: bool) -> list[str]:
    funde = [f"{name}: {fund}" for fund in _kommentare(text)]
    try:
        baum = ast.parse(text)
    except SyntaxError as fehler:
        funde.append(f"{name}: syntax zeile {fehler.lineno}")
        return funde
    eltern = _eltern(baum)
    funde.extend(f"{name}: {fund}" for fund in _namen(baum))
    funde.extend(f"{name}: {fund}" for fund in _fehler(baum))
    if not kern:
        return funde
    funde.extend(f"{name}: {fund}" for fund in _konstante(baum, eltern))
    funde.extend(f"{name}: {fund}" for fund in _kern_import(baum))
    funde.extend(f"{name}: {fund}" for fund in _flach(baum))
    funde.extend(f"{name}: {fund}" for fund in _eingefroren(baum))
    return funde


def lokale_importe(text: str, bekannte: set[str]) -> set[str]:
    try:
        baum = ast.parse(text)
    except SyntaxError:
        return set()
    gefunden: set[str] = set()
    for knoten in ast.walk(baum):
        if isinstance(knoten, ast.Import):
            for alias in knoten.names:
                gefunden.update(_bekannte_teile(alias.name, bekannte))
        elif isinstance(knoten, ast.ImportFrom):
            if knoten.module:
                gefunden.update(_bekannte_teile(knoten.module, bekannte))
            if knoten.level and knoten.level > 0:
                for alias in knoten.names:
                    if alias.name in bekannte:
                        gefunden.add(alias.name)
    return gefunden


def finde_zyklen(kanten: dict[str, set[str]]) -> list[str]:
    farbe: dict[str, int] = {}
    funde: list[str] = []

    def lauf(knoten: str, stapel: list[str]) -> None:
        farbe[knoten] = 1
        stapel.append(knoten)
        for nach in sorted(kanten.get(knoten, ())):
            stand = farbe.get(nach, 0)
            if stand == 0:
                lauf(nach, stapel)
            elif stand == 1 and not funde:
                start = stapel.index(nach)
                funde.append(" -> ".join(stapel[start:] + [nach]))
        stapel.pop()
        farbe[knoten] = 2

    for start in sorted(kanten):
        if farbe.get(start, 0) == 0:
            lauf(start, [])
        if funde:
            break
    return funde


def main() -> int:
    ordner = Path(__file__).resolve().parent
    dateien = {
        pfad.name: pfad.read_text(encoding="utf-8")
        for pfad in sorted(ordner.glob("*.py"))
    }
    funde = pruefe_ordner(dateien, {"rechnung.py"})
    for fund in funde:
        print(fund)
    return 1 if funde else 0


def _bekannte_teile(modul: str, bekannte: set[str]) -> set[str]:
    return {teil for teil in modul.split(".") if teil in bekannte}


def _eltern(baum: ast.AST) -> dict[ast.AST, ast.AST]:
    eltern: dict[ast.AST, ast.AST] = {}
    for knoten in ast.walk(baum):
        for kind in ast.iter_child_nodes(knoten):
            eltern[kind] = knoten
    return eltern


def _kommentare(text: str) -> list[str]:
    funde: list[str] = []
    for nummer, zeile in enumerate(text.splitlines(), start=1):
        inhalt = _kommentar_von(zeile)
        if inhalt is None or inhalt.strip() == "":
            continue
        if inhalt.startswith("!") or inhalt.startswith("-*-") or "coding" in inhalt:
            continue
        if inhalt.startswith(" "):
            funde.append(f"zeile {nummer}: kommentar mit leerzeichen nach #")
            continue
        erstes = inhalt[:1]
        if erstes.isalpha() and erstes != erstes.lower():
            funde.append(f"zeile {nummer}: kommentar beginnt gross")
    return funde


def _kommentar_von(zeile: str) -> str | None:
    in_string = False
    zeichen = ""
    flucht = False
    i = 0
    while i < len(zeile):
        c = zeile[i]
        if in_string:
            if flucht:
                flucht = False
            elif c == "\\":
                flucht = True
            elif c == zeichen:
                in_string = False
            i += 1
            continue
        if c in ("'", '"'):
            in_string = True
            zeichen = c
            i += 1
            continue
        if c == "#":
            return zeile[i + 1 :]
        i += 1
    return None


def _namen(baum: ast.AST) -> list[str]:
    funde: list[str] = []
    for knoten in ast.walk(baum):
        if isinstance(knoten, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if knoten.name.startswith("__") and knoten.name.endswith("__"):
                continue
            if not _SNAKE.match(knoten.name):
                funde.append(f"funktion {knoten.name}: nicht klein_mit_unterstrich")
        elif isinstance(knoten, ast.ClassDef):
            if not _PASCAL.match(knoten.name):
                funde.append(f"klasse {knoten.name}: nicht gross am anfang")
        elif isinstance(knoten, ast.Name) and isinstance(knoten.ctx, ast.Store):
            if _SNAKE.match(knoten.id) or _KONSTANT.match(knoten.id):
                continue
            funde.append(f"name {knoten.id}: nicht klein_mit_unterstrich")
    return funde


def _fehler(baum: ast.AST) -> list[str]:
    funde: list[str] = []
    for knoten in ast.walk(baum):
        if not isinstance(knoten, ast.ExceptHandler):
            continue
        if knoten.type is None:
            funde.append("except ohne typ")
        if len(knoten.body) == 1 and isinstance(knoten.body[0], ast.Pass):
            funde.append("except schluckt den fehler")
    return funde


def _konstante(baum: ast.AST, eltern: dict[ast.AST, ast.AST]) -> list[str]:
    funde: list[str] = []
    for knoten in ast.walk(baum):
        if isinstance(knoten, ast.Constant) and isinstance(knoten.value, str):
            if _ADRESSE.search(knoten.value):
                funde.append("adresse oder pfad in der rechnung")
        zahl = _zahl(knoten)
        if zahl is None or zahl in _ERLAUBTE_ZAHL:
            continue
        if _liegt_in_konstanter(knoten, eltern):
            continue
        funde.append(f"nackte zahl {zahl}")
    return funde


def _zahl(knoten: ast.AST) -> int | None:
    if not isinstance(knoten, ast.Constant) or isinstance(knoten.value, bool):
        return None
    if isinstance(knoten.value, int):
        return knoten.value
    return None


def _liegt_in_konstanter(knoten: ast.AST, eltern: dict[ast.AST, ast.AST]) -> bool:
    aktuell = knoten
    while aktuell in eltern:
        vater = eltern[aktuell]
        if isinstance(vater, ast.Assign):
            ziele = [ziel for ziel in vater.targets if isinstance(ziel, ast.Name)]
            return bool(ziele) and all(_KONSTANT.match(ziel.id) for ziel in ziele)
        if isinstance(vater, ast.AnnAssign) and isinstance(vater.target, ast.Name):
            return _KONSTANT.match(vater.target.id) is not None
        if isinstance(
            vater,
            (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Module),
        ):
            return False
        aktuell = vater
    return False


def _kern_import(baum: ast.AST) -> list[str]:
    funde: list[str] = []
    for knoten in ast.walk(baum):
        namen: list[str] = []
        if isinstance(knoten, ast.Import):
            namen = [alias.name.split(".")[0] for alias in knoten.names]
        elif isinstance(knoten, ast.ImportFrom) and knoten.module:
            namen = [knoten.module.split(".")[0]]
        for name in namen:
            if name in VERBOTENE_IMPORTE:
                funde.append(f"import {name} in der rechnung")
    return funde


def _flach(baum: ast.AST) -> list[str]:
    funde: list[str] = []
    for knoten in ast.walk(baum):
        if isinstance(knoten, ast.ClassDef) and knoten.bases:
            funde.append(f"klasse {knoten.name}: vererbung")
    return funde


def _eingefroren(baum: ast.AST) -> list[str]:
    funde: list[str] = []
    for knoten in ast.walk(baum):
        if not isinstance(knoten, ast.ClassDef):
            continue
        ist_daten, frozen = _dataclass_frozen(knoten)
        if not ist_daten:
            continue
        if not frozen:
            funde.append(f"klasse {knoten.name}: wert nicht eingefroren")
            continue
        funde.extend(_gleicher_typ(knoten))
    return funde


def _dataclass_frozen(knoten: ast.ClassDef) -> tuple[bool, bool]:
    for dekor in knoten.decorator_list:
        aufruf: ast.Call | None
        if isinstance(dekor, ast.Call):
            funk: ast.AST = dekor.func
            aufruf = dekor
        else:
            funk = dekor
            aufruf = None
        name = ""
        if isinstance(funk, ast.Name):
            name = funk.id
        elif isinstance(funk, ast.Attribute):
            name = funk.attr
        if name != "dataclass":
            continue
        if aufruf is None:
            return True, False
        for kw in aufruf.keywords:
            if (
                kw.arg == "frozen"
                and isinstance(kw.value, ast.Constant)
                and kw.value.value is True
            ):
                return True, True
        return True, False
    return False, False


def _gleicher_typ(klasse: ast.ClassDef) -> list[str]:
    funde: list[str] = []
    for knoten in klasse.body:
        if not isinstance(knoten, ast.FunctionDef) or knoten.name.startswith("__"):
            continue
        for sub in ast.walk(knoten):
            if not isinstance(sub, ast.Return) or sub.value is None:
                continue
            wert = sub.value
            gleicher_aufruf = (
                isinstance(wert, ast.Call)
                and isinstance(wert.func, ast.Name)
                and wert.func.id == klasse.name
            )
            gleiches_self = isinstance(wert, ast.Name) and wert.id == "self"
            if gleicher_aufruf or gleiches_self:
                continue
            funde.append(
                f"{klasse.name}.{knoten.name}: gibt nicht {klasse.name} zurück"
            )
            break
    return funde


if __name__ == "__main__":
    raise SystemExit(main())
