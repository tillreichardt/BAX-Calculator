import berechnung as rechner
from web_scraper import scrape_bax


class Spieler: 
    
    def __init__(self, vorname:str, nachname:str, verein: str, gegner_daten: list):
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
            

    def berechne_bax(self, bax_alt, bax_gegner_liste, ergebnis_liste, titel=""):
        n = len(bax_gegner_liste)

        print(f"------ {titel} ------")
        print(f"Balt: {bax_alt}")
        print(f"Gegner: {bax_gegner_liste}")
        print(f"Ergebnisse: {ergebnis_liste}")
        print(f"n: {n}")
        print("-" * 20)

        bniv = rechner.berechne_bax_niveau(bax_gegner_liste)
        ssoll = rechner.berechne_ssoll(bax_alt, bax_gegner_liste)
        sist = rechner.berechne_sist(ergebnis_liste)
        spielefaktor = 7
        berst = rechner.berechne_berst(bniv, spielefaktor, sist, n)
        bn = rechner.berechne_bn(bax_alt, spielefaktor, sist, ssoll)

        print(f"BNiv: {bniv:.4f}")
        print(f"SSoll: {ssoll:.4f}")
        print(f"SIst: {sist:.4f}")
        print(f"Spielefaktor: {spielefaktor}")
        print(f"Berst: {berst:.4f}")
        print(f"Bn: {bn:.4f}")
        print("-" * 20)

        bneu = rechner.berechne_bneu(bax_alt, bniv, berst, bn, n)
        print(f"Neuer BAX: {bneu:.4f}")

        return bneu
    
    def baxBerechnungEinzel(self):
        return self._berechne_bax(
            bax_alt=self.baxAltEinzel,
            bax_gegner_liste=self.baxGegnerEinzel,
            ergebnis_liste=self.ergebnisseEinzel,
            titel="Einzel"
        )
    
    def baxBerechnungDoppel(self):
        # 1. Partner-Mittel
        partner_bax_liste = [t[0] for t in self.baxGegnerDoppel]
        partner_mittel = sum(partner_bax_liste) / len(partner_bax_liste)

        # 2. Eigener BAX inkl. Partner (gleich für alle Spiele)
        bax_eigener = (self.baxAltDoppel + 0.25 * partner_mittel) / 2

        # 3. Gegner-Mittel pro Spiel
        bax_gegner = [sum(t[1]) / 2 for t in self.baxGegnerDoppel]

        # 4. Ergebnisse extrahieren
        ergebnisse = [t[2] for t in self.baxGegnerDoppel]

        return self._berechne_bax(
            bax_alt=bax_eigener,
            bax_gegner_liste=bax_gegner,
            ergebnis_liste=ergebnisse,
            titel="Doppel"
        )

