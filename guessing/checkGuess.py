#funktion som kollar gissningen mot koden och returnerar markeringar
def check_guess(da_code, guess):
    marks = []
    
    #gör en kopia av koden för att kunna ändra på den utan att ändra originalet
    code_change = da_code.copy()
    
    #räknare för att hålla koll på hur många markeringar som har lagts till
    i = 0
    while i < 3:
        #loopar igenom varje siffra i gissningen
        for n in guess:
            #kollar om siffran finns i koden
            if n in code_change:
                #hittar indexen för siffran i koden och gissningen
                place_code = code_change.index(n)
                place_guess = guess.index(n)
                
                #kollar index är lika/är siffra på rätt plats
                if  place_guess == place_code:
                    marks.append("✓")
                    i += 1
                
                #annars är det en rätt siffra på fel plats
                else:
                    marks.append("—")
                    i += 1
                code_change[place_code] = 0
            else:
                #finns inte med i koden, gå vidare
                i +=1
                continue 
    
    #sorterar markeringarna så att rätt markeringar kommer först 
    #(är "✓" först, för snyggare utskrift)
    marks.sort(reverse=True)
    return marks

