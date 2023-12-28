import numpy


def F(n: float) -> list:
    if n == 1:
        return []

    if n % 2 == 0:
        return [int(n / 2)] + F(n / 2)
    else:
        return [int(3 * n + 1)] + F(3 * n + 1)


def energy(a: int, b: int, output_file: str) -> None:
    with open(output_file, "w") as f:
        for i in range(a, b + 1):
            sequence_length = len(F(i))
            f.write(f"{i}: {sequence_length}\n")

        arr = [len(F(i)) for i in range(a, b + 1)]
        f.write(f"\nAVG: {numpy.average(arr)}\n")
        f.write(f"MEDIAN: {numpy.median(arr)}\n")
        f.write(f"MIN: {numpy.min(arr)}\n")
        f.write(f"MAX: {numpy.max(arr)}\n")


def main() -> None:
    energy(1, 10, "output.txt")


if __name__ == "__main__":
    main()
