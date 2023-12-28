def cross(n: int) -> None:
    print((" " * n + "*" * n + " " * n + "\n") * n, end="")
    print(("*" * (3 * n) + "\n") * n, end="")
    print((" " * n + "*" * n + " " * n + "\n") * n, end="")


def main() -> None:
    cross(4)


if __name__ == "__main__":
    main()
