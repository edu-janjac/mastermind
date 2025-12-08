#funktion som visar layouten med gissningar och markeringar
def display_layout(guesses, marks_list):
    #antal rundor från 12 till 1
    antal_rundor = range(12,0,-1)
    
    #gör om antal_rundor till en lista för att kunna iterera igenom den
    rundor = list(antal_rundor)
    
    #printar ut layouten
    print("\n" + "="*60)
    print("Drag #           Drag            Feedback")
    print("-"*60 + "\n")
    
    #loop för att printa ut varje runda med gissning och markeringar
    for n, round_num in enumerate(rundor):
        if n < len(guesses):
            #gör om gissningen och markeringarna till strängar för att kunna printa ut dem 
            #på ett snyggt sätt (inte ['1','2','3','4'] utan 1 2 3 4)
            guess_str = " ".join(map(str, guesses[n]))
            marks_str = " ".join(marks_list[n])
            
            #printar ut rundan med gissning och markeringar
            print(f"{round_num:2d}               {guess_str}         {marks_str}")
        else:
            #om har loopat igenom längden av gissningen, printas bara rundan ut utan 
            #gissning och markeringar
            print(f"{round_num:2d}")
    
    print("="*60 + "\n")
