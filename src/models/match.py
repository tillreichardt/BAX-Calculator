from dataclasses import dataclass
from typing import List

@dataclass
class EinzelMatch:
    gegner_bax: int
    ergebnis: List[int]
    ist_training: bool = False

@dataclass
class Turnier:
    """Eine benannte Gruppe von Spielen (Turnier, Hin-/Rückrunde, ...), in der
    Reihenfolge, in der sie gespielt wurden. Dient als Meilenstein für den
    BAX-Verlauf über die Saison."""
    name: str
    spiele: List[EinzelMatch]

@dataclass
class DoppelMatch:
    partner_bax: int
    gegner_bax_1: int
    gegner_bax_2: int
    ergebnis: List[int]

@dataclass
class MixedMatch:
    partner_bax: int
    gegner_bax_1: int
    gegner_bax_2: int
    ergebnis: List[int]