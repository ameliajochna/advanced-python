def cross(n: int):
    print((' ' * n + '*' * n + ' ' * n + '\n') * n, end='')
    print(('*' * (3 * n) + '\n') * n, end='')
    print((' ' * n + '*' * n + ' ' * n + '\n') * n, end='')


def main():
    cross(4)


if __name__ == '__main__':
    main()
