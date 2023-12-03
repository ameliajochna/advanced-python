def czy_w_kolku(x, y, n):
    return bool((x - n // 2) ** 2 + (y - n // 2) ** 2 <= (n // 2) ** 2)


def kolko(przesuniecie, n, usuniecie):
    for i in range(usuniecie, n - usuniecie):
        for j in range(przesuniecie):
            print(' ', end='')
        for j in range(0, n):
            if czy_w_kolku(i, j, n):
                print('#', end='')
            else:
                print(' ', end='')
        print('')


def balwan(lista):
    for l in lista:
        kolko(int((lista[-1:][0] - l) / 2), l, 0)


balwan([15, 17, 23])
