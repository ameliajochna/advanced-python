import numpy


def F(n):
    if n == 1:
        return []

    if n % 2 == 0:
        return [int(n / 2)] + F(n / 2)
    else:
        return [int(3 * n + 1)] + F(3 * n + 1)


def energia(a, b, output_file):
    with open(output_file, "w") as f:
        for i in range(a, b + 1):
            sequence_length = len(F(i))
            f.write(f"{i}: {sequence_length}\n")

        arr = [len(F(i)) for i in range(a, b + 1)]
        f.write(f"\nAVG: {numpy.average(arr)}\n")
        f.write(f"MEDIAN: {numpy.median(arr)}\n")
        f.write(f"MIN: {numpy.min(arr)}\n")
        f.write(f"MAX: {numpy.max(arr)}\n")


def main():
    energia(1, 10, "output.txt")


if __name__ == "__main__":
    main()
