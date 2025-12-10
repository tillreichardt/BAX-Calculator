from bs4 import BeautifulSoup
import requests

def scrape_bax(gewünschter_verein: str, vorname: str, nachname: str):
    url = f"https://www.badminton-bax.de/index.php/bax-portal/spieler-entwicklung?name={nachname}&vorname={vorname}&vom_start="
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Fall 1: Kein Spieler gefunden
    if soup.find("h3") and "Spieler existiert nicht" in soup.find("h3").text:
        return None
    
    # Fall 2: Spieler mehrfach
    elif soup.find("h2") and "Bitte auswählen!" in soup.find("h2").text:
        labels = soup.find_all("label", id="f14")
        
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

    tabelle = soup.find("table", id="tabelle3")
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
        if tr.find("td", id="f14cb"):
            text_raw = tr.get_text(strip=True).lower()
            if "einzel" in text_raw:
                aktuelle_kategorie = "einzel"
            elif "doppel" in text_raw:
                aktuelle_kategorie = "doppel"
            elif "mixed" in text_raw:
                aktuelle_kategorie = "mixed"
            continue

        if tr.get("id") == "liste":
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



from functools import lru_cache


@lru_cache(maxsize=None)
def get_bax(vorname, nachname, verein, disziplin):
    result = scrape_bax(verein, vorname, nachname)

    if not result:
        raise ValueError(f"{vorname} {nachname} is not in the database")
    if result[disziplin][0][0] == "2025/26":
        return result[disziplin][1][1]
    return result[disziplin][0][1]

def get_bax_einzel(vorname, nachname, verein):
    return get_bax(vorname, nachname, verein, "einzel")

def get_bax_doppel(vorname, nachname, verein):
    return get_bax(vorname, nachname, verein, "doppel")

def get_bax_mixed(vorname, nachname, verein):
    return get_bax(vorname, nachname, verein, "mixed")
# print(scrape_bax("BC Düsseldorf", "Till", "Reichardt"))
# print(scrape_bax("BG 62 Dormagen", "Jonas", "Klose"))