import itertools


def solution(l):
    res = 0

    # Get all the permutations of the list, without duplicates
    for r in range(0, len(l) + 1, 1):

        for i in itertools.permutations(l, r):

            # ignore the empty set
            if i == ():
                continue

            # now we need to convert tuples into an int
            # such as (1, 2, 3) become 123
            num = int("".join(str(x) for x in i))

            # now we check if the number is divisible by 3
            # and greater than the latest divisible
            if num % 3 == 0 and num > res:
                res = num
    return res


print(solution([3, 1, 4, 1]))  # == 4311
print(solution([3, 1, 4, 1, 5, 9]))  # == 94311
