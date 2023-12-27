def divisors(n):
    return [i for i in range(1, n // 2 + 1) if n % i == 0]

def primes(n):
    return [i for i in range(1, n) if len(divisors(i)) == 1]

def composites(n):
    return [i for i in range(1, n) if len(divisors(i)) > 1]

def sum_of_divisors(n):
    return sum(divisors(n))

def is_perfect(n):
    return sum_of_divisors(n) == n

def is_deficient(n):
    return sum_of_divisors(n) < n

def is_abundant(n):
    return sum_of_divisors(n) > n

def generate_list(n, predicate):
    return [i for i in range(1, n) if predicate(i)]

def pythagorean_triplets(n):
    return [
        (i, j, k)
        for k in range(1, n)
        for i in range(1, n)
        for j in range(1, n)
        if i < j and i * i + j * j == k * k
    ]

def main():
    print("divisors of 60: ", divisors(60))
    print("primes less than 25: ", primes(25))
    print("composites less than 20", composites(20))
    print("perfect numbers up to 15:", generate_list(15, is_perfect))
    print("deficient numbers up to 15:", generate_list(15, is_deficient))
    print("abundant numbers up to 15:", generate_list(15, is_abundant))
    print("pythagorean triplets up to 30: ", pythagorean_triplets(30))

if __name__ == "__main__":
    main()