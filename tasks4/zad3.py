import random

def random_permutation(n):
    # Initialize a list with numbers from 0 to n-1
    permutation = list(range(0, n))

    # Perform a Fisher-Yates shuffle to generate a random permutation
    for i in range(n):
        pos = random.randint(i, n - 1)
        # Swap elements at positions i and pos
        permutation[pos], permutation[i] = permutation[i], permutation[pos]

    return permutation

def main():
    # Generate and print a random permutation of numbers from 0 to 10^6 - 1
    print(random_permutation(10**6))

if __name__ == "__main__":
    main()
