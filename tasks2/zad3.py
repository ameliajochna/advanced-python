def is_inside(x: int, y: int, n: int) -> bool:
    return bool((x - n // 2) ** 2 + (y - n // 2) ** 2 <= (n // 2) ** 2)


def draw_circle(shift: int, n: int, removal: int) -> None:
    for i in range(removal, n - removal):
        for j in range(shift):
            print(" ", end="")
        for j in range(0, n):
            if is_inside(i, j, n):
                print("#", end="")
            else:
                print(" ", end="")
        print("")


def draw_snowman(sizes: list) -> None:
    for num in sizes:
        draw_circle(int((sizes[-1:][0] - num) / 2), num, 0)


def main() -> None:
    draw_snowman([15, 17, 23])


if __name__ == "__main__":
    main()
