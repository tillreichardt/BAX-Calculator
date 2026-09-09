import json
import webbrowser
from datetime import datetime
from pathlib import Path

from src.data.spieler_daten import spielerListe
from src.scraper.web_scraper import vorsaison

PROJECT_ROOT = Path(__file__).resolve().parent
TEMPLATE_PATH = PROJECT_ROOT / "webui" / "template.html"
OUTPUT_PATH = PROJECT_ROOT / "bax_report.html"


def match_list(spieler, training_einschliessen):
    return [[m.gegner_bax, m.ergebnis] for m in spieler.alleSpieleEinzel(training_einschliessen)]


def satzverteilung(spieler):
    """Anteil der Siege/Niederlagen dieser Saison, die über 3 Sätze gingen -- als
    empirische Grundlage für eine realistischere Ziel-BAX-Simulation (statt immer
    von 2:0-Siegen/0:2-Niederlagen auszugehen)."""
    matches = spieler.alleSpieleEinzel(training_einschliessen=False)
    siege = [m.ergebnis for m in matches if m.ergebnis[0] > m.ergebnis[1]]
    niederlagen = [m.ergebnis for m in matches if m.ergebnis[0] < m.ergebnis[1]]

    if not siege or not niederlagen:
        return None

    return {
        "saison": spieler.saison,
        "anzahl_spiele": len(matches),
        "anteil_3satz_sieg": round(sum(1 for e in siege if e == [2, 1]) / len(siege), 4),
        "anteil_3satz_niederlage": round(sum(1 for e in niederlagen if e == [1, 2]) / len(niederlagen), 4),
    }


def build_season_data(spieler, spieler_by_saison):
    vorsaison_spieler = spieler_by_saison.get(vorsaison(spieler.saison))

    return {
        "verein": spieler.verein,
        "balt": spieler.baxAltEinzel,
        "satzverteilung": satzverteilung(vorsaison_spieler) if vorsaison_spieler else None,
        "official": {
            "milestones": spieler.baxVerlaufEinzel(training_einschliessen=False),
            "matches": match_list(spieler, False),
            "matches_detail": spieler.alleSpieleEinzelDetailliert(training_einschliessen=False),
        },
        "mit_training": {
            "milestones": spieler.baxVerlaufEinzel(training_einschliessen=True),
            "matches": match_list(spieler, True),
            "matches_detail": spieler.alleSpieleEinzelDetailliert(training_einschliessen=True),
        },
    }


def main():
    spieler_by_saison = {sp.saison: sp for sp in spielerListe}
    season_order = sorted(spieler_by_saison.keys(), reverse=True)

    data = {
        "generated_at": datetime.now().strftime("%d.%m.%Y %H:%M"),
        "season_order": season_order,
        "seasons": {s: build_season_data(spieler_by_saison[s], spieler_by_saison) for s in season_order},
    }

    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    html = template.replace("__BAX_DATA__", json.dumps(data, ensure_ascii=False))
    OUTPUT_PATH.write_text(html, encoding="utf-8")

    print(f"Bericht geschrieben nach {OUTPUT_PATH}")
    webbrowser.open(OUTPUT_PATH.as_uri())


if __name__ == "__main__":
    main()
