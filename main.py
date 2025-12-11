from src.data.spieler_daten import spielerListe

for spieler in spielerListe:
    print(f"Name: {spieler.vorname} {spieler.nachname}")
    spieler.baxBerechnungEinzel()
    print("-" * 20 + "\n\n")
    # spieler.baxBerechnungDoppel()
    print("-" * 20 + "\n\n")
    