import math


def prime_divisors(n):
    arr = []
    for d in range(2, math.ceil(math.sqrt(n)) + 2):
        if n % d == 0:
            arr.append(d)
            while n % d == 0:
                n /= d
    return set(arr)


print(prime_divisors(12))
