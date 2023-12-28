def square(n: int) -> None:
    for i in range(n):
        for j in range(n):
            print("* ", end="")
        print()


def square2(n: int) -> None:
    for ind in range(n):
        print(n * "#")


def main() -> None:
    for i in range(10):
        print("Iteration:", i)
        print(20 * "-")
        if i < 5:
            square(3 + 2 * i)
        else:
            square2(i - 2)
        print()


if __name__ == "__main__":
    main()
