import math

def berechne_bax_niveau(bax_gegner):
    n = len(bax_gegner)
    if n == 0:
        return 0
    return sum(bax_gegner) / n

def berechne_gewinnerwartung(balt, b_gegner):
    D = b_gegner - balt
    WD = 1 / (1 + math.pow(10, D / 50))
    return WD

def berechne_ssoll(balt, bax_gegner):
    SSoll = 0
    for b_gegner in bax_gegner:
        WD = berechne_gewinnerwartung(balt, b_gegner)
        # print(f"Gewinnerwartung gegen {b_gegner} ist: {round(WD * 100)}%")
        SSoll += WD
    return SSoll

def berechne_sist_wert(siege, niederlagen):
    if (siege == 2 and niederlagen == 0) or (siege == 3 and niederlagen == 0): return 1.0
    if (siege == 2 and niederlagen == 1) or (siege == 3 and niederlagen == 2): return 0.8
    if siege == 3 and niederlagen == 1: return 0.9
    
    if (siege == 0 and niederlagen == 2) or (siege == 0 and niederlagen == 3): return 0.0
    if (siege == 1 and niederlagen == 2) or (siege == 2 and niederlagen == 3): return 0.2
    if siege == 1 and niederlagen == 3: return 0.1
    return 0.0

def berechne_sist(ergebnisse):
    SIst = 0
    for siege, niederlagen in ergebnisse:
        SIst += berechne_sist_wert(siege, niederlagen)
    return SIst

def berechne_berst(bniv, spielefaktor, sist, n):
    return bniv + spielefaktor * (sist - n / 2)

def berechne_bn(balt, spielefaktor, sist, ssoll):
    return balt + spielefaktor * (sist - ssoll)

def berechne_bneu(balt, bniv, berst, bn, n):
    if balt <= bniv:
        if bn < berst:
            Bneu = bn
        else:
            Bneu = berst
    else:
        if bn > berst:
            Bneu = (berst + (n + 2) * bn) / (n + 3)
        else:
            Bneu = berst
    return round(Bneu)


def berechne_bax_wert(bax_alt, bax_gegner_liste, ergebnis_liste):
        """Reine BAX-Berechnung ohne Konsolenausgabe. Gibt (bneu, details) zurück,
        details enthält alle Zwischenwerte für Anzeige/Auswertung."""
        n = len(bax_gegner_liste)

        anzahl_gewonnene_matches = sum(1 for siege, niederlagen in ergebnis_liste if siege > niederlagen)
        anzahl_verlorene_matches = sum(1 for siege, niederlagen in ergebnis_liste if siege < niederlagen)

        if n == 0:
            details = {
                "n": 0,
                "gewonnen": 0,
                "verloren": 0,
                "win_rate": 0.0,
            }
            return bax_alt, details

        bniv = berechne_bax_niveau(bax_gegner_liste)
        ssoll = berechne_ssoll(bax_alt, bax_gegner_liste)
        sist = berechne_sist(ergebnis_liste)
        spielefaktor = 500 / (n+50)
        berst = berechne_berst(bniv, spielefaktor, sist, n)
        bn = berechne_bn(bax_alt, spielefaktor, sist, ssoll)
        bneu = berechne_bneu(bax_alt, bniv, berst, bn, n)

        details = {
            "n": n,
            "gewonnen": anzahl_gewonnene_matches,
            "verloren": anzahl_verlorene_matches,
            "win_rate": anzahl_gewonnene_matches / (anzahl_gewonnene_matches + anzahl_verlorene_matches) * 100 if (anzahl_gewonnene_matches + anzahl_verlorene_matches) > 0 else 0,
            "bniv": bniv,
            "ssoll": ssoll,
            "sist": sist,
            "spielefaktor": spielefaktor,
            "berst": berst,
            "bn": bn,
        }
        return bneu, details


def berechne_bax(bax_alt, bax_gegner_liste, ergebnis_liste, titel="", saison=None):
        bneu, details = berechne_bax_wert(bax_alt, bax_gegner_liste, ergebnis_liste)

        print(f"------ {titel} (Saison {saison}) ------")

        if details["n"] == 0:
            print(f"Noch keine Spiele erfasst, BAX unverändert: {bax_alt}")
            print("-" * 20)
            return bneu

        print(f"Balt: {bax_alt}")
        print(f"Gewonnene Matches: {details['gewonnen']}")
        print(f"Verlorene Matches: {details['verloren']}")
        print(f"win rate: {details['win_rate']:.0f}%")
        print(f"n: {details['n']}")
        print("-" * 20)

        print(f"BNiv: {details['bniv']:.2f}")
        print(f"SSoll: {details['ssoll']:.2f}")
        print(f"SIst: {details['sist']:.2f}")
        print(f"Spielefaktor: {details['spielefaktor']:.2f}")
        print(f"Berst: {details['berst']:.2f}")
        print(f"Bn: {details['bn']:.2f}")
        print("-" * 20)

        print(f"Neuer BAX: {bneu}")
        return bneu

