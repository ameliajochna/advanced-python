def square(n):
    for i in range(n):
        for j in range(n):
            print('* ', end='')
        print()


def square2(n):
    for i in range(n):
        print(n * '#')


def main():
    for i in range(10):
        print('Przebieg:', i)
        print(20 * '-')
        if i < 5:
            square(3 + 2 * i)
        else:
            square2(i - 2)
        print()


if __name__ == '__main__':
    main()
