def envelope(n: int) -> None:
    print("*" * (2 * n + 1))

    for i in range(0, n - 1):
        print("*" + " " * i + "*" + " " * (2 * n - 3 - 2 * i) + "*" + " " * i + "*")

    print("*" + " " * (n - 1) + "*" + " " * (n - 1) + "*")

    for i in reversed(range(0, n - 1)):
        print("*" + " " * i + "*" + " " * (2 * n - 3 - 2 * i) + "*" + " " * i + "*")
    print("*" * (2 * n + 1))


def main() -> None:
    envelope(10)


if __name__ == "__main__":
    main()
