import berechnung as rechner
from bax_tool.src.scraper.web_scraper import scrape_bax


class Spieler: 
    
    def __init__(self, vorname:str, nachname:str, verein: str, gegner_daten_einzel: list, gegner_daten_doppel: list = None, gegner_daten_mixed: list = None):
        self.verein = verein
        self.vorname: str = vorname
        self.nachname: str = nachname

        self.baxGegner = [bax for bax, _ in gegner_daten]
        self.ergebnisse = [ergebnis for _, ergebnis in gegner_daten] 

        result = scrape_bax(self.verein, self.vorname, self.nachname)
        if not result: 
            raise ValueError(f"{self.vorname} {self.nachname} is not in the database")
        if result["einzel"][0][0] in "2025/26":
            self.baxAlt: int = result["einzel"][1][1]
        else: 
            self.baxAlt: int = result["einzel"][0][1]
            

    def baxBerechnungEinzel(self):
        return rechner.berechne_bax(
            bax_alt=self.baxAltEinzel,
            bax_gegner_liste=self.baxGegnerEinzel,
            ergebnis_liste=self.ergebnisseEinzel,
            titel="Einzel"
        )
    
    def baxBerechnungDoppel(self):  
        partner_bax_liste = [t[0] for t in self.baxGegnerDoppel]
        partner_mittel = sum(partner_bax_liste) / len(partner_bax_liste)

        bax_eigener = (self.baxAltDoppel + 0.25 * partner_mittel) / 2
        bax_gegner = [sum(t[1]) / 2 for t in self.baxGegnerDoppel]
        ergebnisse = [t[2] for t in self.baxGegnerDoppel]

        return rechner.berechne_bax(
            bax_alt=bax_eigener,
            bax_gegner_liste=bax_gegner,
            ergebnis_liste=ergebnisse,
            titel="Doppel"
        )

