def error_wrong():
    print("Du har gjort fel :)")

def difficulty():
    print("Du får välja mellan 2 svårighetsgrader:\nLättare: Alla siffror är olika\nSvårare: Det kan finnas flera av samma siffra\n")
    diff = int(input("Välj svårighetsgrad: Lätt(1), Svår(2) -> "))
    if diff == 1 or 2:
        return diff

print(difficulty())