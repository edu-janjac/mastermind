#funktion som kollar gissningen mot koden och returnerar markeringar
def check_guess(da_code, guess):
    marks = []
    
    #gör en kopia av koden för att kunna ändra på den utan att ändra originalet
    code_change = da_code.copy()
    guess_change = guess.copy()
    
    for n in range(len(guess)):
        if guess[n] == code_change[n]:
                marks.append("✓")
                code_change[n] = None   
                guess_change[n] = None
    
    for n in range(len(guess_change)):
        if guess_change[n] is not None and guess_change[n] in code_change:
            marks.append("—")
            index = code_change.index(guess_change[n])
            code_change[index] = None

    marks.sort(reverse=True)
    return marks

