import math


def prime_divisors(n):
    divisors = set()

    for divisor in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % divisor == 0:
            divisors.add(divisor)
            while n % divisor == 0:
                n //= divisor

    if n > 1:
        divisors.add(int(n))

    return divisors
