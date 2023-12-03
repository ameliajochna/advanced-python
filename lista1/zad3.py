def krzyzyk(n: int):
    print((' ' * n + '*' * n + ' ' * n + '\n') * n, end='')
    print(('*' * (3 * n) + '\n') * n, end='')
    print((' ' * n + '*' * n + ' ' * n + '\n') * n, end='')


krzyzyk(4)
