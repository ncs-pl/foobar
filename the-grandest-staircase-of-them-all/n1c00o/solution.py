def solution(n):
    t = [1] + [0]*n
    for s in range(1, n + 1):
        for h in range(n, s - 1, -1):
            t[h] += t[h - s]

    return t[-1] - 1
