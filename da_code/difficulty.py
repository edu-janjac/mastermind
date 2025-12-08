import random
from text.error import error_wrong

def difficulty():
    print("Du får välja mellan 2 svårighetsgrader:\nLättare: Alla siffror är olika\nSvårare: Det kan finnas flera av samma siffra\n")
    
    #frågar användaren om svårighetsgrad tills ett giltigt svar ges
    while True:
        diff = input("Välj svårighetsgrad: Lätt(1), Svår(2) -> ")
        #kollar om det är en siffra
        if diff.isdigit() is True:
            if diff != '1' and diff != '2':
                error_wrong()
            else:
                break
        else:
            error_wrong()
            continue
        break 
    return diff

#gör en slumpad siffra mellan 1 och 6
def random_number():
    number = random.randint(1,6)
    return number

def easy():
    #gör en lista för att kolla så att inga siffror upprepas
    seen = set()
    
    order = []
    i = 0
    while i <= 3:
        #genererar en slumpad siffra
        num = random_number()
        
        #kollar om siffran har setts förut
        if num not in seen:
            #lägger till siffran i seen
            seen.add(num)
            
            #lägger till siffran i koden (som ska gisssas)
            order.append(num)
            i += 1
    return order

def hard():
    #genererar en slumpad siffra 4 gånger och lägger till den i koden (som ska gisssas)
    i = 0
    order = []
    while i <= 3:
        order.append(random_number())
        i += 1
    return order