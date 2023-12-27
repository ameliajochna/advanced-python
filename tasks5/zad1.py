import numpy


def F(n):
    if n == 1:
        return []

    if n % 2 == 0:
        return [int(n / 2)] + F(n / 2)
    else:
        return [int(3 * n + 1)] + F(3 * n + 1)


def energia(a, b):
    arr = []
    for i in range(a, b + 1):
        arr += [len(F(i))]

    print("AVG: ", numpy.average(arr))
    print("MEDIAN: ", numpy.median(arr))
    print("MIN: ", numpy.min(arr))
    print("MAX: ", numpy.max(arr))


def main():
    energia(1, 10)


if __name__ == "__main__":
    main()
