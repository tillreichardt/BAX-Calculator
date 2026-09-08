import src.berechnung.berechnung as rechner
from src.scraper.web_scraper import get_bax, vorsaison
from math import floor

class Spieler:

    def __init__(self, vorname:str, nachname:str, verein: str, gegner_daten_einzel: list, gegner_daten_doppel: list = None, gegner_daten_mixed: list = None, saison: str = None):
        """saison: die Saison, in der die übergebenen Spiele stattgefunden haben (z.B. "2026/27").
        Für die Berechnung wird intern immer der BAX der Vorsaison herangezogen."""
        self.verein = verein
        self.vorname: str = vorname
        self.nachname: str = nachname
        self.saison = saison

        self.baxGegnerEinzel = gegner_daten_einzel
        self.baxGegnerDoppel = gegner_daten_doppel
        self.baxGegnerMixed = gegner_daten_mixed

        basis_saison = vorsaison(saison)
        self.baxAltEinzel = get_bax(vorname, nachname, verein, "einzel", basis_saison)
        self.baxAltDoppel = get_bax(vorname, nachname, verein, "doppel", basis_saison)
        self.baxAltMixed = get_bax(vorname, nachname, verein, "mixed", basis_saison)




    def baxBerechnungEinzel(self, training_einschliessen: bool = False):
        matches = [m for m in self.baxGegnerEinzel if training_einschliessen or not m.ist_training]
        titel = "Einzel" + (" inkl. Training" if training_einschliessen else "")
        return rechner.berechne_bax(
            bax_alt=get_bax(self.vorname, self.nachname, self.verein, "einzel", vorsaison(self.saison)),
            bax_gegner_liste=[t.gegner_bax for t in matches],
            ergebnis_liste=[t.ergebnis for t in matches],
            titel=titel,
            saison=self.saison
        )

    def baxBerechnungDoppel(self):
        partner_bax_liste = [d.partner_bax for d in self.baxGegnerDoppel]
        partner_mittel = floor(sum(partner_bax_liste) / len(partner_bax_liste))
        print(f"Durchschnittlicher BAX des Partners: {partner_mittel}")


        bax_eigener = floor(get_bax(self.vorname, self.nachname, self.verein, "doppel", vorsaison(self.saison)) * 0.75 + 0.25 * partner_mittel)
        bax_gegner = [floor(sum([t.gegner_bax_1, t.gegner_bax_2]) / 2) for t in self.baxGegnerDoppel]
        ergebnisse = [t.ergebnis for t in self.baxGegnerDoppel]

        return rechner.berechne_bax(
            bax_alt=bax_eigener,
            bax_gegner_liste=bax_gegner,
            ergebnis_liste=ergebnisse,
            titel="Doppel",
            saison=self.saison
        )

