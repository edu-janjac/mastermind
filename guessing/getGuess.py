from text.error import error_wrong

def get_guess():
    #lista med giltiga siffror för gissning
    valid_guess = ['1','2','3','4','5','6']
    
    #lista för den slutgiltiga gissningen som ska returneras
    final_guess = []
    
    #loop för att få en giltig gissning
    while True:
        #hämtar spelarens gissning och gör om den till en lista för att kunna iterera igenom den
        guess = list(input("Gissning (4 siffror): "))
        
        #kollar om gissningen är rätt längd
        if len(guess) > 4 or len(guess) < 4:
            error_wrong()
            continue
        else:
            #kollar om varje tecken i gissningen är giltig
            for char in guess:
                #om tecknet är siffra och är en giltig siffra läggs den till i final_guess
                if char.isdecimal() and char in valid_guess:
                    guess_num = int(char)
                    final_guess.append(guess_num)
                
                #error om tecknet inte är giltigt
                else:
                    error_wrong()
                    break
            
            #kollar om final_guess har rätt längd (4 siffror), annars rensas den och loopen börjar om
            #finns för att undvika att returnera en ofullständig gissning (t.ex om en ogiltig siffra matas in)
            if len(final_guess) == 4:
                break
            else:
                final_guess.clear()
                continue
    
    #returnerar den slutgiltiga gissningen som en lista med 4 siffror
    return final_guess

