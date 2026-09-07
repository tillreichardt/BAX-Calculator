from bs4 import BeautifulSoup
import requests
from src.scraper.local_cache import get_from_cache, save_to_cache

def scrape_bax(gewünschter_verein: str, vorname: str, nachname: str):
    url = f"https://www.badminton-bax.de/index.php/bax-portal/spieler-entwicklung?name={nachname}&vorname={vorname}&vom_start="
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Fall 1: Kein Spieler gefunden
    if soup.find("h3") and "Spieler existiert nicht" in soup.find("h3").text:
        return None
    
    # Fall 2: Spieler mehrfach
    elif soup.find("h2") and "Bitte auswählen!" in soup.find("h2").text:
        labels = soup.find_all("label", class_="fs-14")
        
        for label in labels:
            verein = label.get_text(strip=True)

            # prüfen, ob Verein übereinstimmt
            if gewünschter_verein in verein:
                sp_code = label.find("input")["value"]
                neue_url = f"https://www.badminton-bax.de/index.php/bax-portal/spieler-entwicklung?sp_code={sp_code}&zeig_historie=&name={nachname}&vorname={vorname}"
                break

    # Fall 3: Spieler eindeutig
    else:
        # URL schon korrekt
        neue_url = url

    response = requests.get(neue_url)
    soup = BeautifulSoup(response.text, "html.parser")

    tabelle = soup.find("table", class_="tabelle3")
    result = {
        "einzel": [],
        "doppel": [],
        "mixed": []
    }

    aktuelle_kategorie = None


    for tr in tabelle.find_all("tr"):
        tds = tr.find_all("td")
        if not tds:
            continue

        # Kategorie-Wechsel erkennen (Einzel / Doppel / Mixed)
        if tr.find("td", class_="col-b"):
            text_raw = tr.get_text(strip=True).lower()
            if "einzel" in text_raw:
                aktuelle_kategorie = "einzel"
            elif "doppel" in text_raw:
                aktuelle_kategorie = "doppel"
            elif "mixed" in text_raw:
                aktuelle_kategorie = "mixed"
            continue

        if "liste" in (tr.get("class") or []):
            saison = None
            bax = None

            for td in tds:
                text = td.get_text(strip=True)
                if not text:
                    continue

                # Prüfen auf Integer (BAX)
                try:
                    bax = int(text)
                    continue
                except ValueError:
                    pass

                # Prüfen auf Saison (Format XXXX/XX)
                if "/" in text and len(text.split("/")[0]) == 4:
                    saison = text

            if saison and bax is not None and aktuelle_kategorie:
                    result[aktuelle_kategorie].append((saison, bax))
    return result
        

def get_bax_alle(vorname, nachname, verein):
    cache_key = f"{vorname}_{nachname}_{verein}".replace(" ", "_")
    
    # 1. Versuch: Aus lokalem Cache laden
    cached_data = get_from_cache(cache_key)
    if cached_data:
        # print(f"Lade {vorname} {nachname} aus lokalem Cache...")
        return cached_data

    # 2. Versuch: Wenn nicht im Cache, dann scrapen
    print(f"Scrape Daten für {vorname} {nachname} neu...")
    result = scrape_bax(verein, vorname, nachname)
    
    if not result:
        raise ValueError(f"{vorname} {nachname} is not in the database")
    
    # 3. Ergebnis für die Zukunft speichern
    save_to_cache(cache_key, result)
    
    return result

def get_bax(vorname, nachname, verein, disziplin, saison):
    """Zugriff auf den BAX-Wert der angegebenen Saison aus dem Cache.

    Hat der Spieler in dieser Saison nicht gespielt (kein Eintrag, z.B. wegen Pause),
    bleibt sein BAX unverändert -- es wird dann der letzte bekannte Wert einer früheren
    Saison verwendet.
    """
    result = get_bax_alle(vorname, nachname, verein)
    eintraege = result[disziplin]

    for eintrag_saison, bax in eintraege:
        if eintrag_saison == saison:
            return bax

    frühere_eintraege = [(s, b) for s, b in eintraege if s < saison]
    if frühere_eintraege:
        letzte_saison, bax = max(frühere_eintraege, key=lambda eintrag: eintrag[0])
        print(f"Hinweis: {vorname} {nachname} hat keinen BAX für {saison} ({disziplin}), verwende letzten bekannten Wert aus {letzte_saison}: {bax}")
        return bax

    raise ValueError(f"Keine BAX-Daten für Saison {saison} oder früher gefunden ({vorname} {nachname}, {disziplin})")

def vorsaison(saison: str) -> str:
    """Gibt die der übergebenen Saison vorausgehende Saison zurück, z.B. '2026/27' -> '2025/26'.

    Für die Berechnung des BAX einer Saison werden immer die BAX-Werte der Vorsaison
    herangezogen (sowohl für den Spieler selbst als auch für alle Gegner).
    """
    start, ende = saison.split("/")
    return f"{int(start) - 1}/{int(ende) - 1:02d}"

# scrape_score("BC Düsseldorf", "Till", "Reichardt"   )
# print(scrape_bax("BC Düsseldorf", "Till", "Reichardt"))
# print(scrape_bax("BG 62 Dormagen", "Jonas", "Klose"))