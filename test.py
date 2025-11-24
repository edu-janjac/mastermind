def error_wrong():
    print("Du har gjort fel :)")

def get_guess():
    i = 0
    valid_guess = ['1','2','3','4','5','6']
    final_guess = []
    while i < 1:
        guess = list(input("Gissning (4 siffror): "))
        for char in guess:
            if char.isdecimal():
                guess_num = int(char)
                final_guess.append(guess_num)
            else:
                error_wrong()
        if final_guess.len() == 4:
            i += 1
        else:
            continue
    return final_guess

print(get_guess())