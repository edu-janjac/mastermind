from text import error_wrong
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

guess = get_guess()
    i = 0
    while i <= 11:

        if guess == :