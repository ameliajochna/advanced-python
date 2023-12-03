import random


def randperm(n):
    perm = list(range(0, n))

    for i in range(n):
        pos = random.randint(i, n - 1)
        perm[pos], perm[i] = perm[i], perm[pos]

    return perm


# for i in range(0, 9):
#     print(randperm(i))

print(randperm(10**6))
