from src.models.spieler import Spieler
from src.models.match import DoppelMatch, EinzelMatch
from src.scraper.web_scraper import get_bax


spielerListe = [
    Spieler(
        "Till", 
        "Reichardt",
        "BC Düsseldorf",
        gegner_daten_einzel=[
            EinzelMatch(get_bax("Rainer", "Gehring", "Ohligser TV", "einzel"), [2,0]),
            EinzelMatch(get_bax("Leif", "Kaiser", "BC Heiligenhaus", "einzel"), [2,0]),
            EinzelMatch(get_bax("Vincent", "Bergman", "OSC Düsseldorf", "einzel"), [2,1]),
            EinzelMatch(get_bax("Felix", "Köster", "PTSV Wuppertal", "einzel"), [2,0]),
            EinzelMatch(get_bax("Thomas", "Müller", "SFD 75 Düsseldorf", "einzel"), [0,2]),
            #EinzelMatch(get_bax("Daniel", "Springob", "BSC Hilden", "einzel"), [0,2]),
        ],
        gegner_daten_doppel=[   
            DoppelMatch(    
                partner_bax=get_bax("Nikhil", "Sundar", "BC Düsseldorf", "doppel"),
                gegner_bax_1=get_bax("Rainer", "Gehring", "Ohligser TV", "doppel"),
                gegner_bax_2=get_bax("Antonio", "Argibay da Silva", "Ohligser TV", "doppel"),
                ergebnis=[2,0]
            ),
            DoppelMatch(
                partner_bax=get_bax("Till", "Schirrmacher", "BC Düsseldorf", "doppel"),
                gegner_bax_1=get_bax("Niklas", "Ketschau", "BC Heiligenhaus", "doppel"),
                gegner_bax_2=get_bax("Finn Luca", "Schulz", "BC Heiligenhaus", "doppel"),
                ergebnis=[2,0]
            ),
            DoppelMatch(
                partner_bax=get_bax("Daniel", "Rickert", "BC Düsseldorf", "doppel"),
                gegner_bax_1=get_bax("Tobias", "Haarmann", "TSV Meerbusch", "doppel"),
                gegner_bax_2=get_bax("Marc", "Abratis", "TSV Meerbusch", "doppel"),
                ergebnis=[0,2]
            ),
            DoppelMatch(
                partner_bax=get_bax("Kirill", "Kuznezow", "BC Düsseldorf", "doppel"),
                gegner_bax_1=get_bax("Vincent", "Bergman", "OSC Düsseldorf", "doppel"),
                gegner_bax_2=get_bax("Tobias", "Vanik", "OSC Düsseldorf", "doppel"),
                ergebnis=[0,2]
            ),
            DoppelMatch(
                partner_bax=get_bax("Gerrit", "Bittmann", "BC Düsseldorf", "doppel"),
                gegner_bax_1=get_bax("Felix", "Köster", "PTSV Wuppertal", "doppel"),
                gegner_bax_2=get_bax("Thorben", "Knippschild", "PTSV Wuppertal", "doppel"),
                ergebnis=[2,0]
            ),
            DoppelMatch(
                partner_bax=get_bax("Kirill", "Kuznezow", "BC Düsseldorf", "doppel"),
                gegner_bax_1=get_bax("Robert", "Klöckers", "SFD 75 Düsseldorf", "doppel"),
                gegner_bax_2=get_bax("Anowar", "Mowry", "SFD 75 Düsseldorf", "doppel"),
                ergebnis=[2,0]
            ),
            # DoppelMatch(
            #     partner_bax=get_bax("Kirill", "Kuznezow", "BC Düsseldorf", "doppel"),
            #     gegner_bax_1=get_bax("Daniel", "Springob", "BSC Hilden", "doppel"),
            #     gegner_bax_2=get_bax("Felix", "Haltaufderheide", "BSC Hilden", "doppel"),
            #     ergebnis=[1,2]
            # )
        ]
    )
]