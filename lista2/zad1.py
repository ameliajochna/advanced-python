def szachownica(n: int, k: int):
    para1 = ' ' * k + '#' * k
    para2 = '#' * k + ' ' * k
    print(((para1 * n + '\n') * k + (para2 * n + '\n') * k) * n)


szachownica(5, 3)
