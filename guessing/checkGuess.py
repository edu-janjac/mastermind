from guessing.getGuess import get_guess
from da_code.code import code

def check_guess():
    i = 0
    marks = []
    da_code = code()
    code_change = da_code.copy()
    guess = get_guess()
    while i < 3:
        for n in guess:
            if n in code_change:
                place_code = code_change.index(n)
                place_guess = guess.index(n)
                if  place_guess == place_code:
                    marks.append("✅")
                    i += 1
                else:
                    marks.append("🌫️")
                    i += 1
                code_change[place_code] = 0
            else:
                i +=1
                continue 
    return marks

