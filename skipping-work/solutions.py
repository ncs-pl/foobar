def solution(x,  y):
    # x and y are two list of integers
    for el in x:
        if not el in y:
            return el
    for el in y:
        if not el in x:
            return el
