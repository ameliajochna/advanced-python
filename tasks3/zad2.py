import math


def is_prime(n: int) -> bool:
    for i in range(2, int(math.sqrt(n) + 2)):
        if n % i == 0:
            return False
    return True


def check_primes(numbers: list) -> int:
    count = 0
    all_primes = []
    for num in numbers:
        if is_prime(num):
            all_primes.append(num)
        count += int(is_prime(num))
    print(all_primes)
    return count


def generate_numbers(length: int, digit: int, consecutive: int) -> list:
    base = str(digit) * consecutive
    numbers = []
    remaining = length - consecutive + 1
    for number in range(0, 10**remaining):
        str_number = str(number)
        if len(str(number)) != remaining:
            str_number = "0" * (remaining - len(str_number)) + str_number

        for pt in range(len(str_number) + 1):
            l1 = str_number[0:pt]
            l2 = str_number[pt:]
            new_number = int(l1 + base + l2)
            if len(str(new_number)) == length + 1:
                numbers.append(new_number)

    numbers = list(dict.fromkeys(numbers))
    return numbers


def main() -> None:
    print(check_primes(generate_numbers(9, 7, 7)))


if __name__ == "__main__":
    main()
