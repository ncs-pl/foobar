def solution(l, t):
    for start_i in range(len(l)):
        sum = 0

        for curr_i in range(start_i, len(l)):
            sum += l[curr_i]

            if sum == t:
                return [start_i, curr_i]

    return [-1, -1]
