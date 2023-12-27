from lista2.big_numbers import give_number


def join_numbers(liczba, cyfra):
    for i in range(len(liczba)):
        liczba[i] += " " + cyfra[i]
    return liczba


def process_number(number_str):
    number_arr = []
    for num in number_str:
        number_arr.append(int(num))

    wynik = give_number(number_arr[0])
    for i in range(1, len(number_arr)):
        wynik = join_numbers(wynik, give_number(number_arr[i]))

    for w in wynik:
        print(w)


def main():
    process_number("12324")


if __name__ == "__main__":
    main()
