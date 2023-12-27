import numpy as np


def F(n):
    if n == 1:
        return []

    if n % 2 == 0:
        return [int(n / 2)] + F(n / 2)
    else:
        return [int(3 * n + 1)] + F(3 * n + 1)


def energia(a, b, output_file):
    with open(output_file, 'w') as f:
        for i in range(a, b + 1):
            sequence_length = len(F(i))
            f.write(f"{i}: {sequence_length}\n")

        arr = [len(F(i)) for i in range(a, b + 1)]
        f.write("\nAVG: {}\n".format(np.average(arr)))
        f.write("MEDIAN: {}\n".format(np.median(arr)))
        f.write("MIN: {}\n".format(np.min(arr)))
        f.write("MAX: {}\n".format(np.max(arr)))


def main():
    energia(1, 10, "output.txt")


if __name__ == "__main__":
    main()
