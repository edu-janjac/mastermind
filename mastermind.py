import random

def error_wrong():
    print("Du har gjort fel :)")

def rules():
    print("Datorn kommer att slumpa fram en kod på fyra siffror mellan 1 och 6.")
    print("Du ska försöka gissa denna kods siffror på max 12 drag.")
    print("Efter respektive gissning korrekt siffra på rätt plats i koden: ")
    print("Efter respektive gissning korrekt siffra på fel plats i koden: ")
    print("För de siffror som inte finns med i koden ges ingen markering.\n")
    print("Exempel: om den slumpande koden är 2315\noch du gissar 3165\nså blir responsen: \n")


def difficulty():
    print("Du får välja mellan 2 svårighetsgrader:\nLättare: Alla siffror är olika\nSvårare: Det kan finnas flera av samma siffra\n")
    diff = int(input("Välj svårighetsgrad: Lätt(1), Svår(2) -> "))
    if diff != int:
        error_wrong()
    return diff

def random_number():
    number = random.randint(1,6)
    return number

def get_number_order():
    i = 0
    order = [ ]
    while i <= 3:
        order.append(random_number())
        i += 1
    return order

def get_guess():
    guess = int(input("Gissning (4 siffror): ")).split()
    return guess

def main():
    rules()
    difficulty()


main()