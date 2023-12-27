def is_inside(x, y, n):
    return bool((x - n // 2) ** 2 + (y - n // 2) ** 2 <= (n // 2) ** 2)


def circle(przesuniecie, n, usuniecie):
    for i in range(usuniecie, n - usuniecie):
        for j in range(przesuniecie):
            print(' ', end='')
        for j in range(0, n):
            if is_inside(i, j, n):
                print('#', end='')
            else:
                print(' ', end='')
        print('')


def snowman(lista):
    for l in lista:
        circle(int((lista[-1:][0] - l) / 2), l, 0)


def main():
    snowman([15, 17, 23])


if __name__ == '__main__':
    main()
