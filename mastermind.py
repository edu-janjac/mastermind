from text.rules import rules
from text.error import error_wrong
from guessing.checkGuess import check_guess
from guessing.getGuess import get_guess
from da_code.code import code
from text.layout import display_layout

def main():
    #visar spelregler
    rules()
    
    #rätt markeringar för vinst
    right_marks = ['✓','✓','✓','✓']
    
    #loop för att kunna spela flera gånger
    while True:
        #kallar funktionen code som skapar kod som spelaren ska gissa
        da_code = code()
        
        #gissningar som spelaren har gjort
        guesses = []
        
        #markeringar för varje gissning
        marks_list = []
        
        #räknare för antal rundor
        i = 0
        while i < 12:
            #hämtar spelarens gissning
            current_guess = get_guess()
            #lägger gissningen i listan med alla gissningar (som spelaren har gjort)
            guesses.append(current_guess)
            
            #kollar gissningen mot koden och får tillbaka markeringar
            marks = check_guess(da_code, current_guess)
            #lägger markeringarna i listan med alla markeringar (som spelaren har fått)
            marks_list.append(marks)
            
            #printar ut layouten med alla gissningar och markeringar
            display_layout(guesses, marks_list)
            
            #kollar om spelaren har vunnit
            if marks == right_marks:
                print(f"grattis du har vunnit! (på {i + 1} rundor)\n")
                i = 12
            
            #ökar i och går vidare till nästa runda
            i += 1
        
        #om spelaren har förlorat
        if i == 12 or i > 12 and marks != right_marks:
            #gör om koden som är en lista till en sträng för att kunna printa ut den
            code_str = " ".join(map(str, da_code))
            #printar ut att spelaren har förlorat och visar koden
            print(f"du har fått slut på omgångar :(\n\nkoden var {code_str}\n")
        
        #loop för att fråga om spelaren vill köra igen, så att spelaren måste skriva in j eller n
        while True:
            svar = input("vill du köra igen? (j/n)")
            #kollar om svaret är j eller n och behöver inte fortsätta fråga
            if svar == 'j' or svar == 'n':
                break
            #visar error om input inte är j eller n
            else:
                error_wrong()
                continue
        if svar == 'j':
            #radbryte
            print("")
            #sätter om räknaren för antal rundor till 0
            i = 0
            #kör om loopen för att spela igen (gör så att den frågar om svårighetsgrad igen)
            continue
        else:
            #avslutar spelet
            print("\ntack för att du körde!\n")
            break

#har sett detta innan, och fick reda på att det används för att kunna kalla 
#på en funktion i andra filer utan att programet körs direkt
#ska vara bra vana :)
if __name__ == "__main__":
    main()