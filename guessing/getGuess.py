from text import error_wrong

def get_guess():
    i = 0
    valid_guess = ['1','2','3','4','5','6']
    final_guess = []
    while i < 1:
        guess = list(input("Gissning (4 siffror): "))
        if len(guess) > 4 or len(guess) < 4:
            error_wrong()
            continue
        else:
            for char in guess:
                if char.isdecimal() and char in valid_guess:
                    guess_num = int(char)
                    final_guess.append(guess_num)
                else:
                    error_wrong()
                    break
            if len(final_guess) == 4:
                i += 1
            else:
                final_guess.clear()
                continue
    return final_guess

