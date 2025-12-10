from src.models.spieler import Spieler
from src.models.match import DoppelMatch, EinzelMatch
from src.scraper.web_scraper import get_bax_einzel, get_bax_doppel, get_bax_mixed


spielerListe = [
    Spieler(
        "Till", 
        "Reichardt",
        "BC Düsseldorf",
        gegner_daten_einzel=[
            EinzelMatch(get_bax_einzel("Rainer", "Gehring", "Ohligser TV"), [2,0]),
            EinzelMatch(get_bax_einzel("Leif", "Kaiser", "BC Heiligenhaus"), [2,0]),
            EinzelMatch(get_bax_einzel("Vincent", "Bergman", "OSC Düsseldorf"), [2,1]),
            EinzelMatch(get_bax_einzel("Felix", "Köster", "PTSV Wuppertal"), [2,0]),
            EinzelMatch(get_bax_einzel("Thomas", "Müller", "SFD 75 Düsseldorf"), [2,0]),
            EinzelMatch(get_bax_einzel("Daniel", "Springob", "BSC Hilden"), [2,0]),
        ]
    )
]