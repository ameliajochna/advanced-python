def chessboard(n: int, k: int):
    type1 = " " * k + "#" * k
    type2 = "#" * k + " " * k
    print(((type1 * n + "\n") * k + (type2 * n + "\n") * k) * n)


def main():
    chessboard(5, 3)


if __name__ == "__main__":
    main()
