def error_wrong():
    print("Du har gjort fel :)")

def get_guess():
    i = 0
    final_guess = []
    while i < 1:
        guess = input("Gissning (4 siffror): ")
        if guess.isdigit() is False:
            error_wrong()
            continue
        else:
            guess = guess.split
            final_guess.append(guess)
            i += 1
    return final_guess

print(get_guess())