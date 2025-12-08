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
            

    def baxBerechnung(self):
        n = len(self.baxGegner)
        # --- Startwerte ---
        print(f"Balt: {self.baxAlt}")
        print(f"Gegner: {self.baxGegner}")
        print(f"Ergebnisse: {self.ergebnisse}")
        print(f"n: {n}")
        print("-" * 20)
        
        # --- Zwischenberechnungen ---
        bniv = rechner.berechne_bax_niveau(self.baxGegner)
        ssoll = rechner.berechne_ssoll(self.baxAlt, self.baxGegner)
        sist = rechner.berechne_sist(self.ergebnisse)
        spielefaktor = 7
        berst = rechner.berechne_berst(bniv, spielefaktor, sist, n)
        bn = rechner.berechne_bn(self.baxAlt, spielefaktor, sist, ssoll)
        
        print(f"BNiv: {bniv:.4f}")
        print(f"SSoll: {ssoll:.4f}")
        print(f"SIst: {sist:.4f}")
        print(f"Spielefaktor: {spielefaktor:.4f}")
        print(f"Berst: {berst:.4f}")
        print(f"Bn: {bn:.4f}")
        
        print("-" * 20)

        # --- Endergebnis ---
        bneu = rechner.berechne_bneu(self.baxAlt, bniv, berst, bn, n)
        print(f"neuer BAX: {bneu:.4f}")
        
        return bneu