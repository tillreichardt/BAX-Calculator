"""Kumulative BAX-Simulation wie in der Turnierplan-Referenz (SF=7, gleiche Formeln)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


SF = 7


def gew(balt: float, bopp: float) -> float:
    return 1.0 / (1.0 + 10 ** ((bopp - balt) / 50.0))


def calc_bneu(
    balt: float, bniv_all: float, n_all: float, sist_all: float, ssoll_all: float
) -> Tuple[float, float, float]:
    berst = bniv_all + SF * (sist_all - n_all / 2.0)
    bn = balt + SF * (sist_all - ssoll_all)
    if balt <= bniv_all:
        bneu = min(bn, berst)
    else:
        bneu = (berst + (n_all + 2) * bn) / (n_all + 3) if bn > berst else berst
    return round(bneu), berst, bn


@dataclass
class TournamentStepResult:
    name: str
    n: int
    avg_bax: float
    wins: int
    losses: int
    bneu: float
    berst: float
    bn: float
    bniv_now: float
    cum_n: float
    cum_sist: float
    cum_ssoll: float


@dataclass
class SimulationResult:
    b_start: float
    steps: List[TournamentStepResult]
    history_labels: List[str]
    history_bax: List[float]
    initial_cum_n: float
    initial_cum_sist: float
    initial_cum_ssoll: float


def simulate_from_base(
    balt: float,
    n0: int,
    bniv0: float,
    sist0: float,
    tournaments: List[Tuple[str, int, float, int]],
) -> SimulationResult:
    """
    tournaments: Liste von (Name, Anzahl Spiele, Ø Gegner-BAX, Siege).
    Niederlagen = Spiele - Siege. SIst-Zuwachs pro Turnier = Siege (wie Referenz-JS).
    """
    cum_n = float(n0)
    cum_bniv_sum = bniv0 * n0
    cum_sist = float(sist0)
    cum_ssoll = n0 * gew(balt, bniv0)
    initial_cum_n = cum_n
    initial_cum_sist = cum_sist
    initial_cum_ssoll = cum_ssoll

    b_start, _, _ = calc_bneu(balt, bniv0, cum_n, cum_sist, cum_ssoll)

    history_labels: List[str] = ["Start"]
    history_bax: List[float] = [b_start]

    steps: List[TournamentStepResult] = []

    for name, n_matches, avg_bax, wins in tournaments:
        n = max(0, int(n_matches))
        w = max(0, min(int(wins), n))
        losses = n - w

        sist_t = float(w)
        ssoll_t = n * gew(balt, avg_bax)

        cum_n += n
        cum_bniv_sum += avg_bax * n
        cum_sist += sist_t
        cum_ssoll += ssoll_t

        bniv_now = cum_bniv_sum / cum_n
        bneu, berst, bn = calc_bneu(balt, bniv_now, cum_n, cum_sist, cum_ssoll)

        steps.append(
            TournamentStepResult(
                name=name,
                n=n,
                avg_bax=avg_bax,
                wins=w,
                losses=losses,
                bneu=bneu,
                berst=berst,
                bn=bn,
                bniv_now=bniv_now,
                cum_n=cum_n,
                cum_sist=cum_sist,
                cum_ssoll=cum_ssoll,
            )
        )
        short = name[:12] + "…" if len(name) > 12 else name
        history_labels.append(short)
        history_bax.append(bneu)

    return SimulationResult(
        b_start=b_start,
        steps=steps,
        history_labels=history_labels,
        history_bax=history_bax,
        initial_cum_n=initial_cum_n,
        initial_cum_sist=initial_cum_sist,
        initial_cum_ssoll=initial_cum_ssoll,
    )


def recommendation_text(final_bax: float) -> str:
    if final_bax >= 490:
        return (
            "Ziel erreicht: BAX liegt sicher im Bereich der zweiten Mannschaft. "
            "Subjektiv stärkt du das Bild durch B- und A-Feld-Teilnahmen."
        )
    if final_bax >= 480:
        return (
            "Ziel knapp erreicht: BAX liegt im Zielkorridor. "
            "Ein gutes Zusatzturnier im B-Feld sichert den Puffer."
        )
    return (
        f"Ziel noch nicht erreicht ({final_bax:.0f}). Wechsle Turniere von A auf B, "
        "oder erhöhe Siege in den B-Feldern. Mehr C-Felder mit 5:0 bringen garantierten Zuwachs."
    )
