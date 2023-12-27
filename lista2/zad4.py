from lista2.big_numbers import give_number


def scal_cyfry(liczba, cyfra):
    for i in range(len(liczba)):
        liczba[i] += ' ' + cyfra[i]
    return liczba


def process_number(number_str):
    number_arr = []
    for l in number_str:
        number_arr.append(int(l))

    wynik = give_number(number_arr[0])
    for i in range(1, len(number_arr)):
        wynik = scal_cyfry(wynik, give_number(number_arr[i]))

    for w in wynik:
        print(w)


def main():
    process_number('12324')


if __name__ == '__main__':
    main()
