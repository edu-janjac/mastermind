import random
from text import error_wrong

def difficulty():
    print("Du får välja mellan 2 svårighetsgrader:\nLättare: Alla siffror är olika\nSvårare: Det kan finnas flera av samma siffra\n")
    i = 0
    while i < 1:
        diff = input("Välj svårighetsgrad: Lätt(1), Svår(2) -> ")
        if diff.isdigit() is True:
            diff = int(diff)
            if diff != 1 and diff != 2:
                error_wrong()
            else:
                i += 1
                break
        else:
            error_wrong()
            continue 
    return diff

def random_number():
    number = random.randint(1,6)
    return number

def easy():
    seen = set()
    order = []
    i = 0
    while i <= 3:
        num = random_number()
        if num not in seen:
            seen.add(num)
            order.append(num)
            i += 1
    return order

def hard():
    i = 0
    order = []
    while i <= 3:
        order.append(random_number())
        i += 1
    return order