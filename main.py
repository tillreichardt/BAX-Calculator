from src.data.spieler_daten import spielerListe

spieler = spielerListe[0]
print(f"Name: {spieler.vorname} {spieler.nachname}")
# spieler.baxBerechnungEinzel()
spieler.baxBerechnungDoppel()
print("-" * 20 + "\n\n")
