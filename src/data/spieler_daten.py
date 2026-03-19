from src.models.spieler import Spieler
from src.models.match import DoppelMatch, EinzelMatch
from src.scraper.web_scraper import get_bax


spielerListe = [
    Spieler(
        "Till", 
        "Reichardt",
        "BC Düsseldorf",
        gegner_daten_einzel=[
            # Hinrunde
            EinzelMatch(get_bax("Rainer", "Gehring", "Ohligser TV", "einzel"), [2,0]),
            EinzelMatch(get_bax("Leif", "Kaiser", "BC Heiligenhaus", "einzel"), [2,0]),
            EinzelMatch(get_bax("Vincent", "Bergman", "OSC Düsseldorf", "einzel"), [2,1]),
            EinzelMatch(get_bax("Felix", "Köster", "PTSV Wuppertal", "einzel"), [2,0]),
            EinzelMatch(get_bax("Thomas", "Müller", "SFD 75 Düsseldorf", "einzel"), [0,2]),
            EinzelMatch(get_bax("Daniel", "Springob", "BSC Hilden", "einzel"), [0,2]),
          
            # Rückrunde
            EinzelMatch(get_bax("Leif", "Kaiser", "BC Heiligenhaus", "einzel"), [2,0]),
            EinzelMatch(get_bax("Robert", "Klöckers", "SFD 75 Düsseldorf", "einzel"), [2,0]),
            EinzelMatch(get_bax("Vincent", "Bergman", "OSC Düsseldorf", "einzel"), [2,1]),
            EinzelMatch(get_bax("Rainer", "Gehring", "Ohligser TV", "einzel"), [2,0]),
            EinzelMatch(get_bax("Marc", "Abratis", "TSV Meerbusch", "einzel"), [2,0]),

            # Düsseldorfer Stadtmeisterschaften 2025
            EinzelMatch(get_bax("Fabian", "Fischer", "OSC Düsseldorf", "einzel"), [0,2]),
            EinzelMatch(get_bax("Constantin", "Wermann", "OSC Düsseldorf", "einzel"), [0,2]),
            EinzelMatch(get_bax("Leon", "Mainusch", "SSV WBG Bochum", "einzel"), [0,2]),
            
            # 2. RLT Bezirk Langenfeld 2025
            EinzelMatch(get_bax("Andreas", "Kläs", "BC Burg", "einzel"), [2,0]),
            EinzelMatch(get_bax("Bogdan", "Cravcenco", "OSC Düsseldorf", "einzel"), [2,0]),
            EinzelMatch(get_bax("Maximilian", "Schaerlaekens", "Krefelder BC", "einzel"), [2,0]),
            EinzelMatch(get_bax("Jan", "Hammer", "FC Langenfeld", "einzel"), [2,0]),

            # Neujahrsturnier OSC Düsseldorf 2026
            EinzelMatch(get_bax("Jonas", "Klose", "BG 62 Dormagen", "einzel"), [0,2]),
            EinzelMatch(get_bax("Vincent", "Bergman", "OSC Düsseldorf", "einzel"), [1,2]),
            EinzelMatch(get_bax("Veit", "Kriegel", "OSC Düsseldorf", "einzel"), [2,1]),

            # Offene Duisburger Stadtmeisterschaften
            EinzelMatch(get_bax("Jan", "Kaufmann", "TVE Heinsberg", "einzel"), [0,2]),
            EinzelMatch(get_bax("Dominik", "Pehle", "VfB GW Mülheim", "einzel"), [1,2]),
            EinzelMatch(get_bax("Daniele", "Bertoldo", "BC Matchpoint Berlin", "einzel"), [2,0]),
            EinzelMatch(get_bax("Arttapon", "Setchampa", "OSC Düsseldorf", "einzel"), [2,0]),

            # Westdeutsche Meisterschaften U22 2026
            EinzelMatch(get_bax("Johann", "Sufryd", "1. BV Mülheim", "einzel"), [0,2]),

            # Test
            # EinzelMatch(get_bax("Andreas", "Kläs", "BC Burg", "einzel"), [2,0]),
            # EinzelMatch(get_bax("Bogdan", "Cravcenco", "OSC Düsseldorf", "einzel"), [2,0]),
            # EinzelMatch(get_bax("Maximilian", "Schaerlaekens", "Krefelder BC", "einzel"), [2,0]),
            # EinzelMatch(get_bax("Jan", "Hammer", "FC Langenfeld", "einzel"), [2,0]),
            # EinzelMatch(get_bax("Andreas", "Kläs", "BC Burg", "einzel"), [2,0]),
            # EinzelMatch(get_bax("Bogdan", "Cravcenco", "OSC Düsseldorf", "einzel"), [2,0]),
            # EinzelMatch(get_bax("Maximilian", "Schaerlaekens", "Krefelder BC", "einzel"), [2,0]),
            # EinzelMatch(get_bax("Jan", "Hammer", "FC Langenfeld", "einzel"), [2,0]),
            # EinzelMatch(get_bax("Andreas", "Kläs", "BC Burg", "einzel"), [2,0]),
            # EinzelMatch(get_bax("Bogdan", "Cravcenco", "OSC Düsseldorf", "einzel"), [2,0]),
            # EinzelMatch(get_bax("Maximilian", "Schaerlaekens", "Krefelder BC", "einzel"), [2,0]),
            # EinzelMatch(get_bax("Jan", "Hammer", "FC Langenfeld", "einzel"), [2,0]),
        ]
    )
]