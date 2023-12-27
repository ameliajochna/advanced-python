import random


def randperm(n):
    perm = list(range(0, n))

    for i in range(n):
        pos = random.randint(i, n - 1)
        perm[pos], perm[i] = perm[i], perm[pos]

    return perm


def main():
    print(randperm(10**6))


if __name__ == "__main__":
    main()
