def sieve_of_eratosthenes(max_n: int, is_prime: list) -> None:
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, max_n):
        if is_prime[i]:
            for k in range(2, (max_n + 1) // i):
                is_prime[k * i] = False


def is_palindrome(n: int) -> bool:
    reversed_n = str(n)[::-1]
    return str(n) == reversed_n


def palindromes(a: int, b: int, is_prime: list, max_n: int) -> int:
    count = 0
    for i in range(a, b + 1):
        count += int(is_prime[i] and is_palindrome(i))
        if is_prime[i] and is_palindrome(i):
            print(i)

    return count


def main() -> None:
    max_n = 1001
    is_prime = [True] * max_n
    sieve_of_eratosthenes(max_n, is_prime)
    palindromes(0, 1000, is_prime, max_n)


if __name__ == "__main__":
    main()
