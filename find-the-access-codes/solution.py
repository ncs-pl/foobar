def solution(array):
    if len(array) < 3:
        return 0

    solutions = [0] * len(array)
    found = 0

    for i in range(len(array)):
        for j in range(i):
            if array[i] % array[j] == 0:
                solutions[i] += 1
                found += solutions[j]
    return found


print(solution([1, 2, 3, 4, 5, 6]), "should equal", 3)
print(solution([1, 1, 1]), "should equal", 1)
