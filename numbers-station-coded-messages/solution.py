def solution(l, t):
    for start_i in range(len(l)):
        sum = l[start_i]

        for curr_i in range(start_i + 1, len(l), 1):
            sum += l[curr_i]

            if sum == t:
                return [start_i, curr_i]
            elif sum > t:
                break

    return [-1, -1]


# tests
assert solution([1, 2, 3, 4], 15) == [-1, -1], "Test 1 failed"
assert solution([4, 3, 10, 2, 8], 12) == [2, 3], "Test 2 failed"
