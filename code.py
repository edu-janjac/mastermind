import random

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
