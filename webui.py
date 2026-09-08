import json
import webbrowser
from pathlib import Path

from src.data.spieler_daten import spielerListe

PROJECT_ROOT = Path(__file__).resolve().parent
TEMPLATE_PATH = PROJECT_ROOT / "webui" / "template.html"
OUTPUT_PATH = PROJECT_ROOT / "bax_report.html"


def build_season_data(spieler):
    return {
        "verein": spieler.verein,
        "balt": spieler.baxAltEinzel,
        "official": {"milestones": spieler.baxVerlaufEinzel(training_einschliessen=False)},
        "mit_training": {"milestones": spieler.baxVerlaufEinzel(training_einschliessen=True)},
    }


def main():
    spieler_by_saison = {sp.saison: sp for sp in spielerListe}
    season_order = sorted(spieler_by_saison.keys(), reverse=True)

    data = {
        "season_order": season_order,
        "seasons": {s: build_season_data(spieler_by_saison[s]) for s in season_order},
    }

    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    html = template.replace("__BAX_DATA__", json.dumps(data, ensure_ascii=False))
    OUTPUT_PATH.write_text(html, encoding="utf-8")

    print(f"Bericht geschrieben nach {OUTPUT_PATH}")
    webbrowser.open(OUTPUT_PATH.as_uri())


if __name__ == "__main__":
    main()
