# coding=utf-8
from fractions import Fraction

def solution(pegs):
    # This function is based on the formulat I figured out on paper
    # using what I could find online about gears, I used the 
    # (number of gears entraining one other) / (number of gears entraned by one other)
    # Using the distances, I can express the sizes of all gears from the first one
    # and then, using the formula, I can find x

    # The developed formula shows that the signs + / - are present half of the time
    # However, the x present in the last part changes if the number is event/pair
    # (because of the signs, when n is pair, it adds up to the one present in the other branch
    # of the equation, if n is impair, it removes 2x from the single x on the other branch, resulting
    # in a negative x in the other branch

    sm = 0
    # Avoid .append by creating a sized array
    distances = [pegs[0]] + [0] * (len(pegs) - 1)

    # We calculate the points between the pegs, (except the first one)
    for i, v in enumerate(pegs):
        if i != 0:
            distances[i] = pegs[i] - pegs[i - 1]

    # Derived from the formula
    for i, v in enumerate(distances[1:]):
        sm += (-1) ** (i) * (2 * v)
    
    denom = 1

    # If the number of pegs is pair, we divide by 3
    if len(pegs) % 2 == 0:
        denom = 3

    # Avoid .append by creating a sized array
    sizes = [sm / denom] + [0] * (len(pegs) - 1)

    # calculate all the gear sizes
    for i, v in enumerate(distances):
        if v == distances[0]:
            continue
        
        size = v - sizes[i - 1]
        sizes[i] = size

        # all gears must be >=
        if size < 1:
            return [-1, -1]

    # used to simplify the fraction
    f = Fraction(sm, denom)

    # the first gear must be >= 1
    if f < 1:
        return [-1, -1]
    
    return [f.numerator, f.denominator]


assert solution([4, 17, 50]) == [-1, -1], "invalid"
assert solution([4, 30, 50]) == [12, 1], "invalid"
