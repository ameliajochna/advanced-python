from tasks2.big_numbers import give_number


def join_numbers(number: list, digit: list) -> list:
    for i in range(len(number)):
        number[i] += " " + digit[i]
    return number


def process_number(number_str: str) -> None:
    number_arr = []
    for num in number_str:
        number_arr.append(int(num))

    result = give_number(number_arr[0])
    for i in range(1, len(number_arr)):
        result = join_numbers(result, give_number(number_arr[i]))

    for r in result:
        print(r)


def main() -> None:
    process_number("12324")


if __name__ == "__main__":
    main()
