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
        print(f"Gewinnerwartung gegen {b_gegner} ist: {round(WD * 100)}%")
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


def berechne_bax(bax_alt, bax_gegner_liste, ergebnis_liste, titel=""):
        n = len(bax_gegner_liste)

        print(f"------ {titel} ------")
        print(f"Balt: {bax_alt}")
        print(f"Gegner: {bax_gegner_liste}")
        print(f"Ergebnisse: {ergebnis_liste}")
        print(f"n: {n}")
        print("-" * 20)

        bniv = berechne_bax_niveau(bax_gegner_liste)
        ssoll = berechne_ssoll(bax_alt, bax_gegner_liste)
        sist = berechne_sist(ergebnis_liste)
        spielefaktor = 7
        berst = berechne_berst(bniv, spielefaktor, sist, n)
        bn = berechne_bn(bax_alt, spielefaktor, sist, ssoll)

        print(f"BNiv: {bniv:.2f}")
        print(f"SSoll: {ssoll:.2f}")
        print(f"SIst: {sist:.2f}")
        print(f"Spielefaktor: {spielefaktor}")
        print(f"Berst: {berst:.2f}")
        print(f"Bn: {bn:.2f}")
        print("-" * 20)

        bneu = berechne_bneu(bax_alt, bniv, berst, bn, n)
        print(f"Neuer BAX: {bneu}")
        return bneu
    
