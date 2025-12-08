#funktion som skriver ut reglerna för spelet
def rules():
    print("\nDatorn kommer att slumpa fram en kod på fyra siffror mellan 1 och 6.")
    print("Du ska försöka gissa denna kods siffror på max 12 drag.")
    print("Efter respektive gissning korrekt siffra på rätt plats i koden: ✓")
    print("Efter respektive gissning korrekt siffra på fel plats i koden: —")
    print("För de siffror som inte finns med i koden ges ingen markering.\n")
    print("Exempel: om den slumpande koden är 2315\noch du gissar 3165\nså blir responsen: ✓ — — \n")