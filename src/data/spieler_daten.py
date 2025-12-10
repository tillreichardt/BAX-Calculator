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
        ],
        gegner_daten_doppel=[   
            DoppelMatch(
                partner_bax=get_bax_doppel("Nikhil", "Sundar", "BC Düsseldorf"),
                gegner_bax_1=get_bax_doppel("Rainer", "Gehring", "Ohligser TV"),
                gegner_bax_2=get_bax_doppel("Antonio", "Argibay da Silva", "Ohligser TV"),
                ergebnis=[2,0]
            ),
            DoppelMatch(
                partner_bax=get_bax_doppel("Till", "Schirrmacher", "BC Düsseldorf"),
                gegner_bax_1=get_bax_doppel("Niklas", "Ketschau", "BC Heiligenhaus"),
                gegner_bax_2=get_bax_doppel("Finn Luca", "Schulz", "BC Heiligenhaus"),
                ergebnis=[2,0]
            ),
            DoppelMatch(
                partner_bax=get_bax_doppel("Daniel", "Rickert", "BC Düsseldorf"),
                gegner_bax_1=get_bax_doppel("Tobias", "Haarmann", "TSV Meerbusch"),
                gegner_bax_2=get_bax_doppel("Marc", "Abratis", "TSV Meerbusch"),
                ergebnis=[0,2]
            ),
            DoppelMatch(
                partner_bax=get_bax_doppel("Kirill", "Kuznezow", "BC Düsseldorf"),
                gegner_bax_1=get_bax_doppel("Vincent", "Bergman", "OSC Düsseldorf"),
                gegner_bax_2=get_bax_doppel("Tobias", "Vanik", "OSC Düsseldorf"),
                ergebnis=[0,2]
            ),
            DoppelMatch(
                partner_bax=get_bax_doppel("Gerrit", "Bittmann", "BC Düsseldorf"),
                gegner_bax_1=get_bax_doppel("Felix", "Köster", "PTSV Wuppertal"),
                gegner_bax_2=get_bax_doppel("Thorben", "Knippschild", "PTSV Wuppertal"),
                ergebnis=[2,0]
            ),
            DoppelMatch(
                partner_bax=get_bax_doppel("Kirill", "Kuznezow", "BC Düsseldorf"),
                gegner_bax_1=get_bax_doppel("Robert", "Klöckers", "SFD 75 Düsseldorf"),
                gegner_bax_2=get_bax_doppel("Anowar", "Mowry", "SFD 75 Düsseldorf"),
                ergebnis=[2,0]
            ),
            DoppelMatch(
                partner_bax=get_bax_doppel("Kirill", "Kuznezow", "BC Düsseldorf"),
                gegner_bax_1=get_bax_doppel("Daniel", "Springob", "BSC Hilden"),
                gegner_bax_2=get_bax_doppel("Felix", "Haltaufderheide", "BSC Hilden"),
                ergebnis=[1,2]
            )
        ]
    )
]