from code import easy
from code import hard
from text import error_wrong
from text import rules

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

def main():
    rules()
    if  difficulty() == 1:
        order = easy()
    else:
        order = hard()

main()