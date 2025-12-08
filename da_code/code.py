from da_code.difficulty import difficulty, easy, hard

#gör koden beroende på vald svårighetsgrad
def code():
    diff = difficulty()
    if diff == 1:
        code = easy()
    else:
        code = hard()
    return code