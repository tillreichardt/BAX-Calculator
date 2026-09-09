import pytest

from src.berechnung import berechnung as rechner


def test_berechne_sist_wert_bekannte_ergebnisse():
    assert rechner.berechne_sist_wert(2, 0) == 1.0
    assert rechner.berechne_sist_wert(3, 0) == 1.0
    assert rechner.berechne_sist_wert(2, 1) == 0.8
    assert rechner.berechne_sist_wert(3, 1) == 0.9
    assert rechner.berechne_sist_wert(3, 2) == 0.8
    assert rechner.berechne_sist_wert(0, 2) == 0.0
    assert rechner.berechne_sist_wert(1, 2) == 0.2
    assert rechner.berechne_sist_wert(1, 3) == 0.1
    assert rechner.berechne_sist_wert(0, 3) == 0.0


def test_berechne_bax_niveau_leere_liste():
    assert rechner.berechne_bax_niveau([]) == 0


def test_berechne_bax_niveau_durchschnitt():
    assert rechner.berechne_bax_niveau([400, 420, 440]) == 420


def test_berechne_gewinnerwartung_gleiche_staerke():
    assert rechner.berechne_gewinnerwartung(450, 450) == pytest.approx(0.5)


def test_berechne_gewinnerwartung_monoton_faellt_mit_gegnerstaerke():
    schwaecherer_gegner = rechner.berechne_gewinnerwartung(450, 400)
    staerkerer_gegner = rechner.berechne_gewinnerwartung(450, 500)
    assert schwaecherer_gegner > 0.5 > staerkerer_gegner


def test_berechne_bax_ohne_spiele_gibt_balt_unveraendert_zurueck():
    ergebnis = rechner.berechne_bax(bax_alt=475, bax_gegner_liste=[], ergebnis_liste=[], titel="Einzel", saison="2026/27")
    assert ergebnis == 475


def test_berechne_bax_wert_stimmt_mit_berechne_bax_ueberein():
    bax_alt = 450
    gegner = [430, 460, 470]
    ergebnisse = [[2, 0], [1, 2], [2, 1]]

    bneu_wert, _details = rechner.berechne_bax_wert(bax_alt, gegner, ergebnisse)
    bneu_bax = rechner.berechne_bax(bax_alt, gegner, ergebnisse, titel="Test", saison="2025/26")

    assert bneu_wert == bneu_bax
