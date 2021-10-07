def is_prime(n):
    assert n > 1, "the number must be > 1"
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            return False
    return True

prime_string = []
i = 1

while len(prime_string) < 10000 + 5:
    i += 1
    if is_prime(i):
        prime_string.append(str(i))

print(''.join(prime_string))
