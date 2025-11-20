import random

def error_wrong():
    print("Du har gjort fel :)")

def rules():
    print("Datorn kommer att slumpa fram en kod på fyra siffror mellan 1 och 6.")
    print("Du ska försöka gissa denna kods siffror på max 12 drag.")
    print("Efter respektive gissning korrekt siffra på rätt plats i koden: ✅")
    print("Efter respektive gissning korrekt siffra på fel plats i koden: 🌫️")
    print("För de siffror som inte finns med i koden ges ingen markering.\n")
    print("Exempel: om den slumpande koden är 2315\noch du gissar 3165\nså blir responsen: \n")

def difficulty():
    print("Du får välja mellan 2 svårighetsgrader:\nLättare: Alla siffror är olika\nSvårare: Det kan finnas flera av samma siffra\n")
    i = 0
    while i < 1:
        diff = int(input("Välj svårighetsgrad: Lätt(1), Svår(2) -> "))
        if diff != 1 and diff != 2:
            error_wrong()
        else:
            i += 1
    return diff

def random_number():
    number = random.randint(1,6)
    return number

def easy():
    seen = set()
    order = []
    i = 0
    while i <= 3:
        num = random_number()
        if num not in seen:
            seen.add(num)
            order.append(num)
            i += 1
    return order

def hard():
    i = 0
    order = []
    while i <= 3:
        order.append(random_number())
        i += 1
    return order

def get_guess():
    i = 0
    while i < 1:
        guess = input("Gissning (4 siffror): ").split()
        if guess.isdigit() is True:
            guess(int(guess))
            return guess
            i += 1
        else:
            error_wrong()

def layout():
    print("Drag #       Drag        Feedback")
    print("--------------------------------------------\n")

def layout_round():
    i = 0
    runda = 12
    while i <= 11:
        print(runda - 1"\n")
        

def main():
    rules()
    if  difficulty() == 1:
        order = easy()
    else:
        order = hard()
    guess = get_guess()
    i = 0
    while i <= 11:

        if guess == :

main()