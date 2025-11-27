from text import rules
from guessing.checkGuess import check_guess

def main():
    rules()
    i = 0
    while i < 11:
        marks = check_guess()
        print(marks)
        i += 1
    print("du har slut på gissningar!")

main()