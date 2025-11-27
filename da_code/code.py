from da_code.difficulty import difficulty
from da_code.difficulty import easy
from da_code.difficulty import hard

def code():
    diff = difficulty()
    if diff == 1:
        code = easy()
    else:
        code = hard()
    return code