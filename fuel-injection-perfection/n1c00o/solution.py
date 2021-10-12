def solution(str_n):
    # 3 possibles operations:
    # - Add one fuel
    # - Remove one fuel
    # - Divide fuel by 2 (allowed only if fuel is an even number)
    fuel = int(str_n)
    actions = 0

    # Execute until we get 1 fuel remaining
    while fuel != 1:
        # If fuel is not an even number, we need to add or remove one fuel
        if fuel % 2 != 0:
            # We have to check if it is more interesting to add or remove one fuel, depending on the result of (fuel + 1) % 2 and (fuel - 1)
            # i.e. 13 -> Adding 1 = 14 ; 14 // 2 = 7 ; we'd need to update 7 to get an even number
            #      13 -> Removing 1 = 12 ; 12 // 2 = 6 ; we wouldn't need to add change 6

            # If removing one is more efficient
            if ((fuel - 1) // 2) % 2 == 0:
                fuel -= 1
                actions += 1
            # Exception! If it results in 2, then it is more efficient to go from 3 to 2
            elif fuel - 1 == 2:
                fuel -= 1
                actions += 1
            # if not, we add one
            else:
                fuel += 1
                actions += 1

        # Consume fuel
        fuel //= 2
        actions += 1

    return actions


print(solution('4'), "should equal 2")
print(solution('15'), "should equal 5")
