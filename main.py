import sys

from src.data.spieler_daten import spielerListe

# Optional: Saison als Kommandozeilenargument übergeben, um nur diese zu berechnen,
# z.B. `python main.py 2026/27`. Ohne Argument werden alle Saisons berechnet.
saison_filter = sys.argv[1] if len(sys.argv) > 1 else None

for spieler in spielerListe:
    if saison_filter and spieler.saison != saison_filter:
        continue
    print(f"\nName: {spieler.vorname} {spieler.nachname}")
    spieler.baxBerechnungEinzel()
    print("-" * 20 + "\n\n")