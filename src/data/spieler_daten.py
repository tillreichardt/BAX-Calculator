from src.models.spieler import Spieler
from src.models.match import DoppelMatch, EinzelMatch
from src.scraper.web_scraper import get_bax, vorsaison

# Saison, in der die jeweiligen Spiele stattgefunden haben. Für die BAX-Berechnung
# wird daraus immer automatisch die Vorsaison abgeleitet (vorsaison()), da sowohl der
# eigene als auch der gegnerische BAX aus der Vorsaison in die Berechnung eingehen.
SAISON_2025_26 = "2025/26"
SAISON_2026_27 = "2026/27"

spielerListe = [
    Spieler(
        "Till",
        "Reichardt",
        "BC Düsseldorf",
        saison=SAISON_2025_26,
        gegner_daten_einzel=[
            # Hinrunde
            EinzelMatch(get_bax("Rainer", "Gehring", "Ohligser TV", "einzel", vorsaison(SAISON_2025_26)), [2,0]),
            EinzelMatch(get_bax("Leif", "Kaiser", "BC Heiligenhaus", "einzel", vorsaison(SAISON_2025_26)), [2,0]),
            EinzelMatch(get_bax("Vincent", "Bergman", "OSC Düsseldorf", "einzel", vorsaison(SAISON_2025_26)), [2,1]),
            EinzelMatch(get_bax("Felix", "Köster", "PTSV Wuppertal", "einzel", vorsaison(SAISON_2025_26)), [2,0]),
            EinzelMatch(get_bax("Thomas", "Müller", "SFD 75 Düsseldorf", "einzel", vorsaison(SAISON_2025_26)), [0,2]),
            EinzelMatch(get_bax("Daniel", "Springob", "BSC Hilden", "einzel", vorsaison(SAISON_2025_26)), [0,2]),
          
            # Rückrunde
            EinzelMatch(get_bax("Leif", "Kaiser", "BC Heiligenhaus", "einzel", vorsaison(SAISON_2025_26)), [2,0]),
            EinzelMatch(get_bax("Robert", "Klöckers", "SFD 75 Düsseldorf", "einzel", vorsaison(SAISON_2025_26)), [2,0]),
            EinzelMatch(get_bax("Vincent", "Bergman", "OSC Düsseldorf", "einzel", vorsaison(SAISON_2025_26)), [2,1]),
            EinzelMatch(get_bax("Rainer", "Gehring", "Ohligser TV", "einzel", vorsaison(SAISON_2025_26)), [2,0]),
            EinzelMatch(get_bax("Marc", "Abratis", "TSV Meerbusch", "einzel", vorsaison(SAISON_2025_26)), [0,2]),

            # Düsseldorfer Stadtmeisterschaften 2025
            EinzelMatch(get_bax("Fabian", "Fischer", "OSC Düsseldorf", "einzel", vorsaison(SAISON_2025_26)), [0,2]),
            EinzelMatch(get_bax("Constantin", "Wermann", "OSC Düsseldorf", "einzel", vorsaison(SAISON_2025_26)), [0,2]),
            EinzelMatch(get_bax("Leon", "Mainusch", "SSV WBG Bochum", "einzel", vorsaison(SAISON_2025_26)), [0,2]),
            
            # 2. RLT Bezirk B-Feld Langenfeld 2025
            EinzelMatch(get_bax("Andreas", "Kläs", "BC Burg", "einzel", vorsaison(SAISON_2025_26)), [2,0]),
            EinzelMatch(get_bax("Bogdan", "Cravcenco", "OSC Düsseldorf", "einzel", vorsaison(SAISON_2025_26)), [2,0]),
            EinzelMatch(get_bax("Maximilian", "Schaerlaekens", "Krefelder BC", "einzel", vorsaison(SAISON_2025_26)), [2,0]),
            EinzelMatch(get_bax("Jan", "Hammer", "FC Langenfeld", "einzel", vorsaison(SAISON_2025_26)), [2,0]),

            # Neujahrsturnier OSC Düsseldorf 2026
            EinzelMatch(get_bax("Jonas", "Klose", "BG 62 Dormagen", "einzel", vorsaison(SAISON_2025_26)), [0,2]),
            EinzelMatch(get_bax("Vincent", "Bergman", "OSC Düsseldorf", "einzel", vorsaison(SAISON_2025_26)), [1,2]),
            EinzelMatch(get_bax("Veit", "Kriegel", "OSC Düsseldorf", "einzel", vorsaison(SAISON_2025_26)), [2,1]),

            # Offene Duisburger Stadtmeisterschaften
            EinzelMatch(get_bax("Jan", "Kaufmann", "TVE Heinsberg", "einzel", vorsaison(SAISON_2025_26)), [0,2]),
            EinzelMatch(get_bax("Dominik", "Pehle", "VfB GW Mülheim", "einzel", vorsaison(SAISON_2025_26)), [1,2]),
            EinzelMatch(get_bax("Daniele", "Bertoldo", "BC Matchpoint Berlin", "einzel", vorsaison(SAISON_2025_26)), [2,0]),
            EinzelMatch(get_bax("Arttapon", "Setchampa", "OSC Düsseldorf", "einzel", vorsaison(SAISON_2025_26)), [2,0]),

            # Westdeutsche Meisterschaften U22 2026 -- Zählt nicht zur Bax-Berechnung, warum auch immer
            EinzelMatch(get_bax("Johann", "Sufryd", "1. BV Mülheim", "einzel", vorsaison(SAISON_2025_26)), [0,2]),

            # Ostwestfalenpokal 2026
            EinzelMatch(get_bax("Stephan", "Weber", "SC Melle 03", "einzel", vorsaison(SAISON_2025_26)), [2,0]),
            EinzelMatch(get_bax("Andre", "Bäumer", "SC GW Steinbeck", "einzel", vorsaison(SAISON_2025_26)), [2,0]),
            EinzelMatch(get_bax("Julius", "Hüne", "TV Werther 04", "einzel", vorsaison(SAISON_2025_26)), [2,0]),
            EinzelMatch(get_bax("Joel", "Walkenhorst", "BSC Westerenger", "einzel", vorsaison(SAISON_2025_26)), [1,2]),

            # Blau-Weißer Alpen Cup 2026
            EinzelMatch(get_bax("Dominik", "Pehle", "VfB GW Mülheim", "einzel", vorsaison(SAISON_2025_26)), [2,1]),
            EinzelMatch(get_bax("Oliver", "Krause", "VfB GW Mülheim", "einzel", vorsaison(SAISON_2025_26)), [0,2]),
            EinzelMatch(get_bax("Mirko", "Fischer", "TuS Saxonia Münster", "einzel", vorsaison(SAISON_2025_26)), [2,1]),
            EinzelMatch(get_bax("Takayuki", "Nagakura", "TV Datteln", "einzel", vorsaison(SAISON_2025_26)), [0,2]),

            # 13. BTB Open 2026
            EinzelMatch(get_bax("Simon", "Michalowski", "SG Bad Bears BSC", "einzel", vorsaison(SAISON_2025_26)), [2,0]),
            EinzelMatch(get_bax("Sebastian", "Harms", "DJK Stolberg", "einzel", vorsaison(SAISON_2025_26)), [2,1]),
            EinzelMatch(get_bax("Lukas", "Riege", "FC Rheinland Übach", "einzel", vorsaison(SAISON_2025_26)), [2,0]),
            EinzelMatch(get_bax("Rene", "Wagner", "FC Rheinland Übach", "einzel", vorsaison(SAISON_2025_26)), [2,0]),
            EinzelMatch(get_bax("Stefan", "Reupert", "SC St. Tönis", "einzel", vorsaison(SAISON_2025_26)), [2,0]),
            # EinzelMatch(get_bax("Cedric", "Conrad", "BSC Herzogenrath", "einzel", vorsaison(SAISON_2025_26)), [2,0]),
            EinzelMatch(431, [2,0]), # Cedric Conrad, BSC Herzogenrath -- hat noch keinen BAX vergangener Saison gehabt
            EinzelMatch(get_bax("Joshua", "Heinzmann", "1. BV Troisdorf", "einzel", vorsaison(SAISON_2025_26)), [1,2]),

            # 4. Schwebebahn Cup 2026
            # Walkover -- EinzelMatch(get_bax("Jonas", "Klose", "BG 62 Dormagen", "einzel", vorsaison(SAISON_2025_26)), [2,0]),
            EinzelMatch(get_bax("Fabian", "Fischer", "OSC Düsseldorf", "einzel", vorsaison(SAISON_2025_26)), [0,2]),
            EinzelMatch(get_bax("Matthias", "Hampel", "BC Heiligenhaus", "einzel", vorsaison(SAISON_2025_26)), [2,0]),
            EinzelMatch(get_bax("Julian", "Klehr", "OSC Düsseldorf", "einzel", vorsaison(SAISON_2025_26)), [1,2]),

            # 3. RLT Bezirk A-Feld Langenfeld 2026
            EinzelMatch(get_bax("Steffen", "Maus", "STC BW Solingen", "einzel", vorsaison(SAISON_2025_26)), [0,2]),
            EinzelMatch(get_bax("Philipp", "Bartoschek", "WMTV Solingen", "einzel", vorsaison(SAISON_2025_26)), [2,0]),
            EinzelMatch(get_bax("Stefan", "Reupert", "SC St. Tönis", "einzel", vorsaison(SAISON_2025_26)), [2,1]),
            EinzelMatch(get_bax("Robert", "Möller", "FC Langenfeld", "einzel", vorsaison(SAISON_2025_26)), [2,0]),
            EinzelMatch(get_bax("Tobias", "Röper", "FC Langenfeld", "einzel", vorsaison(SAISON_2025_26)), [0,2]),
            
            # Beuler Summer Games 2026
            EinzelMatch(get_bax("Jan", "Hammer", "FC Langenfeld", "einzel", vorsaison(SAISON_2025_26)), [2,0]),
            EinzelMatch(get_bax("Maurice", "Seefeld", "TC 1889 Kreuzau", "einzel", vorsaison(SAISON_2025_26)), [2,0]),
            EinzelMatch(get_bax("Laurin", "Verweyen", "TG Mülheim/Köln", "einzel", vorsaison(SAISON_2025_26)), [2,0]),
            # EinzelMatch(get_bax("Patrick", "Dasberg", "1. BV Troisdorf", "einzel", vorsaison(SAISON_2025_26)), [0,2]),
            EinzelMatch(435, [0,2]), # Patrick Dasberg, 1. BV Troisdorf -- hat noch keinen BAX vergangener Saison gehabt
        ]
    ),
    Spieler(
        "Till",
        "Reichardt",
        "FC Langenfeld",
        saison=SAISON_2026_27,
        gegner_daten_einzel=[
            # Saison 2026/27 -- hier neue Spiele eintragen, sobald sie stattgefunden haben.
            # Gegner-BAX wird automatisch aus der Vorsaison (2025/26) geholt.
            
            # 1. RLT Verband B-Feld
            EinzelMatch(get_bax("Jakob", "Hummelsheim", "Kölner FC BG", "einzel", vorsaison(SAISON_2026_27)), [0,2]),
            EinzelMatch(get_bax("Marco", "Böning", "SSV WBG Bochum", "einzel", vorsaison(SAISON_2026_27)), [2,0]),
            EinzelMatch(get_bax("Robin", "Langhoff", "BAT Bergisch Gladbach", "einzel", vorsaison(SAISON_2026_27)), [0,2]),
            EinzelMatch(get_bax("Fabian", "Disic", "SSV WBG Bochum", "einzel", vorsaison(SAISON_2026_27)), [1,2]),
            EinzelMatch(get_bax("Timo", "Gollan", "VfL Bochum Badminton", "einzel", vorsaison(SAISON_2026_27)), [2,1]),
        ]
    )
]