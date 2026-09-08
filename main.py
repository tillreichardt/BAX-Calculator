import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Berechnet den neuen BAX-Wert aus den erfassten Spielen.")
    parser.add_argument(
        "saison",
        nargs="?",
        default="2026/27",
        help='Saison, die berechnet werden soll, z.B. "2026/27" (Standard: 2026/27)',
    )
    parser.add_argument(
        "--training",
        action="store_true",
        help="Trainingsspiele mit in die Berechnung einbeziehen (Standard: nur offizielle Spiele)",
    )
    return parser.parse_args()


args = parse_args()

# Import erst nach dem Parsen der Argumente, damit `--help` nicht erst alle Spieler
# scrapen muss, bevor die Hilfe angezeigt wird.
from src.data.spieler_daten import spielerListe

for spieler in spielerListe:
    if spieler.saison != args.saison:
        continue
    print(f"\nName: {spieler.vorname} {spieler.nachname}")
    spieler.baxBerechnungEinzel(training_einschliessen=args.training)
    print("-" * 20 + "\n\n")