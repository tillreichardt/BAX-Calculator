import sys

from src.data.spieler_daten import spielerListe

saison_filter = "2026/27"
training_einschliessen = "y" == "ys" 

for spieler in spielerListe:
    if saison_filter and spieler.saison != saison_filter:
        continue
    print(f"\nName: {spieler.vorname} {spieler.nachname}")
    spieler.baxBerechnungEinzel(training_einschliessen=training_einschliessen)
    print("-" * 20 + "\n\n")