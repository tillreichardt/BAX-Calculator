from src.data.spieler_daten import spielerListe

for spieler in spielerListe:
    print(f"\nName: {spieler.vorname} {spieler.nachname}")
    spieler.baxBerechnungEinzel()
    print("-" * 20 + "\n\n")