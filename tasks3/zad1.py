import math


def is_prime(n: int) -> bool:
    for i in range(2, int(math.sqrt(n) + 2)):
        if n % i == 0:
            return False
    return True


def is_happy_number(number: int, digit: int, consecutive: int) -> bool:
    if not is_prime(number):
        return False
    count = 0
    for c in str(number):
        if int(c) == digit:
            count += 1
        else:
            count = 0
        if count == consecutive:
            return True

    return False


def check_range(range_limit: int) -> None:
    count = 0
    for i in range(range_limit + 1):
        if is_happy_number(i, 4, 2):
            print(i)
            count += 1

    print(count)


def main() -> None:
    check_range(100000)


if __name__ == "__main__":
    main()
