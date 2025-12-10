from spieler import Spieler
from functools import lru_cache
from web_scraper import scrape_bax

@lru_cache(maxsize=None)
def get_bax(vorname, nachname, verein, disziplin):
    result = scrape_bax(verein, vorname, nachname)

    if not result:
        raise ValueError(f"{vorname} {nachname} is not in the database")
    if result[disziplin][0][0] == "2025/26":
        return result[disziplin][1][1]
    return result[disziplin][0][1]



spielerListe = [
    Spieler(
        "Till", 
        "Reichardt",
        "BC Düsseldorf",
        gegner_daten = [
            (get_bax("Rainer", "Gehring", "Ohligser TV"), [2,0]),
            (get_bax("Leif", "Kaiser", "BC Heiligenhaus"), [2,0]),
            (get_bax("Vincent", "Bergman", "OSC Düsseldorf"), [2,1]),
            (get_bax("Felix", "Köster", "PTSV Wuppertal"), [2,0]),
            (get_bax("Thomas", "Müller", "SFD 75 Düsseldorf"), [2,0]),
            (get_bax("Daniel", "Springob", "BSC Hilden"), [2,0]),
        ]
    )
]