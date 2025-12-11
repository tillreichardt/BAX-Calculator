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
    ),
    Spieler(
        "Jonas",
        "Klose",
        "BG 62 Dormagen",
        gegner_daten_einzel=[
            EinzelMatch(
                gegner_bax= get_bax("Atif", "Javed", "Osterather TV", "einzel"),
                ergebnis=[2,1]
            ),
            EinzelMatch(
                gegner_bax= get_bax("Stephan", "Vallata", "SC Bad Bears BSC", "einzel"),
                ergebnis=[2,0]
            ),
            EinzelMatch(
                gegner_bax= get_bax("Manuel", "Günster", "SV DJK Holzbüttgen", "einzel"),
                ergebnis=[2,0]
            ),
            EinzelMatch(
                gegner_bax= get_bax("Alexander", "Reinhardt", "TSV Norf", "einzel"),
                ergebnis=[2,0]
            )
        ],
        gegner_daten_doppel=[
            DoppelMatch(
                partner_bax= get_bax("Lukas", "Bartsch", "BG 62 Dormagen", "doppel"),
                gegner_bax_1= get_bax("Atif", "Javed", "Osterather TV", "doppel"),
                gegner_bax_2= get_bax("Muhammad", "Ahmad", "Osterather TV", "doppel"),
                ergebnis=[0,2]
            ),
            DoppelMatch(
                partner_bax= get_bax("Lukas", "Bartsch", "BG 62 Dormagen", "doppel"),
                gegner_bax_1= get_bax("Heinz-Josef", "Rösch", "SC Bad Bears BSC", "doppel"),
                gegner_bax_2= get_bax("Stephan", "Vallata", "SC Bad Bears BSC", "doppel"),
                ergebnis=[2,0]
            ),
            DoppelMatch(
                partner_bax= get_bax("Lukas", "Bartsch", "BG 62 Dormagen", "doppel"),
                gegner_bax_1= get_bax("Renaldi", "Bernard", "SV DJK Holzbüttgen", "doppel"),
                gegner_bax_2= get_bax("Manuel", "Günster", "DV DJK Holzbüttgen", "doppel"),
                ergebnis=[2,1]
            ),
            DoppelMatch(
                partner_bax= get_bax("Lukas", "Bartsch", "BG 62 Dormagen", "doppel"),
                gegner_bax_1= get_bax("Alexander", "Reinhardt", "TSV Norf", "doppel"),
                gegner_bax_2= get_bax("Florian", "Klein", "TSV Norf", "doppel"),
                ergebnis=[2,0]
            )
        ]
    )
]