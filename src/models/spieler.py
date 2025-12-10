import src.berechnung.berechnung as rechner
from src.scraper.web_scraper import get_bax_einzel, get_bax_doppel, get_bax_mixed
from math import floor

class Spieler: 
    
    def __init__(self, vorname:str, nachname:str, verein: str, gegner_daten_einzel: list, gegner_daten_doppel: list = None, gegner_daten_mixed: list = None):
        self.verein = verein
        self.vorname: str = vorname
        self.nachname: str = nachname

        self.baxGegnerEinzel = gegner_daten_einzel
        self.baxGegnerDoppel = gegner_daten_doppel
        self.baxGegnerMixed = gegner_daten_mixed

        self.baxAltEinzel = get_bax_einzel(vorname, nachname, verein)
        self.baxAltDoppel = get_bax_doppel(vorname, nachname, verein)
        self.baxAltMixed = get_bax_mixed(vorname, nachname, verein) 

        
            

    def baxBerechnungEinzel(self):
        return rechner.berechne_bax(
            bax_alt=get_bax_einzel(self.vorname, self.nachname, self.verein),
            bax_gegner_liste=[t.gegner_bax for t in self.baxGegnerEinzel],
            ergebnis_liste=[t.ergebnis for t in self.baxGegnerEinzel],
            titel="Einzel"
        )
    
    def baxBerechnungDoppel(self):  
        partner_bax_liste = [d.partner_bax for d in self.baxGegnerDoppel]
        partner_mittel = floor(sum(partner_bax_liste) / len(partner_bax_liste))

        bax_eigener = floor((get_bax_doppel(self.vorname, self.nachname, self.verein) + 0.25 * partner_mittel) / 2)
        bax_gegner = [floor(sum([t.gegner_bax_1, t.gegner_bax_2]) / 2) for t in self.baxGegnerDoppel]
        ergebnisse = [t.ergebnis for t in self.baxGegnerDoppel]

        return rechner.berechne_bax(
            bax_alt=bax_eigener,
            bax_gegner_liste=bax_gegner,
            ergebnis_liste=ergebnisse,
            titel="Doppel"
        )

