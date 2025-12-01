from text import rules
from text import error_wrong
from guessing.checkGuess import check_guess
from da_code.code import code

def main():
    rules()
    i = 0
    j = True
    right_marks = ['✅','✅','✅','✅']
    while j == True:
        da_code = code()
        while i < 12:
            marks = check_guess(da_code)
            print(f"runda {i + 1}: {marks}") #ska ändra så det blir rundor 12 till 1
            if marks == right_marks:
                print(f"grattis du har vunnit! (på {i + 1} rundor)")
                i = 12
            i += 1
        if i == 12 or i > 12 and marks != right_marks:
            print("du har fått slut på omgångar :(")
        svar = input("vill du köra igen? (j/n)")
        if svar == 'j':
            i = 0
            continue
        elif svar == 'n':
            print("tack för att du körde!")
            break
        else:
            error_wrong()


main()