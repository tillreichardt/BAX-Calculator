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
            EinzelMatch(get_bax("Marc", "Abratis", "TSV Meerbusch", "einzel"), [0,2]),

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

            # Westdeutsche Meisterschaften U22 2026 -- Zählt nicht zur Bax-Berechnung, warum auch immer
            # EinzelMatch(get_bax("Johann", "Sufryd", "1. BV Mülheim", "einzel"), [0,2]),

            # Ostwestfalenpokal 2026
            EinzelMatch(get_bax("Stephan", "Weber", "SC Melle 03", "einzel"), [2,0]),
            EinzelMatch(get_bax("Andre", "Bäumer", "SC GW Steinbeck", "einzel"), [2,0]),
            EinzelMatch(get_bax("Julius", "Hüne", "TV Werther 04", "einzel"), [2,0]),
            EinzelMatch(get_bax("Joel", "Walkenhorst", "BSC Westerenger", "einzel"), [1,2]),

            # Blau-Weißer Alpen Cup 2026
            EinzelMatch(get_bax("Dominik", "Pehle", "VfB GW Mülheim", "einzel"), [2,1]),
            EinzelMatch(get_bax("Oliver", "Krause", "VfB GW Mülheim", "einzel"), [0,2]),
            EinzelMatch(get_bax("Mirko", "Fischer", "TuS Saxonia Münster", "einzel"), [2,1]),
            EinzelMatch(get_bax("Takayuki", "Nagakura", "TV Datteln", "einzel"), [0,2]),

            # 13. BTB Open 2026
            EinzelMatch(get_bax("Simon", "Michalowski", "SG Bad Bears BSC", "einzel"), [2,0]),
            EinzelMatch(get_bax("Sebastian", "Harms", "DJK Stolberg", "einzel"), [2,1]),
            EinzelMatch(get_bax("Lukas", "Riege", "FC Rheinland Übach", "einzel"), [2,0]),
            EinzelMatch(get_bax("Rene", "Wagner", "FC Rheinland Übach", "einzel"), [2,0]),
            EinzelMatch(get_bax("Stefan", "Reupert", "SC St. Tönis", "einzel"), [2,0]),
            # EinzelMatch(get_bax("Cedric", "Conrad", "BSC Herzogenrath", "einzel"), [2,0]),
            EinzelMatch(431, [2,0]),
            EinzelMatch(get_bax("Joshua", "Heinzmann", "1. BV Troisdorf", "einzel"), [1,2]),

            # 4. Schwebebahn Cup 2026
            # Walkover -- EinzelMatch(get_bax("Jonas", "Klose", "BG 62 Dormagen", "einzel"), [2,0]),
            EinzelMatch(get_bax("Fabian", "Fischer", "OSC Düsseldorf", "einzel"), [0,2]),
            EinzelMatch(get_bax("Matthias", "Hampel", "BC Heiligenhaus", "einzel"), [2,0]),
            EinzelMatch(get_bax("Julian", "Klehr", "OSC Düsseldorf", "einzel"), [1,2]),

        ]
    )
]