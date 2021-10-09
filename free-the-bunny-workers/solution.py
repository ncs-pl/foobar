from itertools import combinations


def solution(num_buns, num_required):
    c = list(combinations(range(num_buns), num_buns - (num_required - 1)))
    res = []

    for bunny in range(num_buns):
        res.append([k for k, b in enumerate(c) if bunny in b])

    return res


print(solution(5, 3))
