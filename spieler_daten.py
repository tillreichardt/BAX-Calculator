from spieler import Spieler
from functools import lru_cache
from web_scraper import scrape_bax

@lru_cache(maxsize=None)
def get_bax(vorname, nachname, verein):
    result = scrape_bax(verein, vorname, nachname)

    if result["einzel"][0][0] == "2025/26":
        return result["einzel"][1][1]
    return result["einzel"][0][1]

spielerListe = [
    Spieler(
        "Till", 
        "Reichardt",
        "BC Düsseldorf",
        baxGegner = [
            get_bax("Rainer", "Gehring", "Ohligser TV"),
            get_bax("Leif", "Kaiser", "BC Heiligenhaus"),
            get_bax("Vincent", "Bergman", "OSC Düsseldorf"),
            get_bax("Felix", "Köster", "PTSV Wuppertal"),
            get_bax("Thomas", "Müller", "SFD 75 Düsseldorf"),
            get_bax("Daniel", "Springob", "BSC Hilden"),
        ],
        ergebnisse = [
            [2, 0],  # Rainer Gehring
            [2, 0],  # Leif Kaiser
            [2, 1],  # Vincent Berman
            [2, 0],  # Felix Köster
            [0, 2],  # Thomas Müller
            [0, 2],  # Daniel Springob
        ]
    )
]