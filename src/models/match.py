from dataclasses import dataclass
from typing import List

@dataclass
class EinzelMatch: 
    bax_gegner: int
    ergebnis: List[int]

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