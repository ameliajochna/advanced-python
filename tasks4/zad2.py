import random

# This program contains several simple functions demonstrating operations on lists.
# [!] indicates that it is necessary to add (or change) existing code at that point.
# The correct program output can be found on the KNO page.


def is_even(n: int) -> bool:
    return n % 2 == 0


#
# Functions that perform operations on a list
#


def sum1(L: list) -> int:
    # 'Summing elements of the list'
    result = 0
    for element in L:
        result += element
    return result


def sum2(L: list) -> int:  # [!]
    # 'Summing elements of the list, iteration by indices. There is a minor mistake in the function.'
    result = 0  # instead of L[0]
    for index in range(len(L)):
        result += L[index]
    return result


def sum_even(L: list) -> int:  # [!]
    # 'Sum of even elements in the list. There is also an error in this function. You should use the is_even function.'

    result = 0
    for element in L:
        result += int(is_even(element)) * element
    return result


#
# Procedures that do something for a list (but do not modify the list)
#


def with_spaces(n: int, k: int, character: str) -> str:
    # "If the number n takes up less than k characters, add the appropriate number of spaces (or '_' characters) to the end"
    s = str(n)
    if len(s) < k:
        for i in range(k - len(s)):
            s += character
    return s


def draw_histogram(L: list) -> None:
    # 'Prints a histogram for the list L. The number with asterisks should not concatenate; the asterisks should start in the fourth column'
    for number in L:
        print(str(number) + " " + "*" * number)


#
# Functions (procedures) that modify the list that is the argument
#


def increment_numbers(L: list) -> None:
    # 'function increases all elements of list L. Does not return anything significant (we call it as a procedure)'
    for i in range(len(L)):
        L[i] += 1


def normalize(L: list) -> None:
    # 'function subtracts the average value of all elements of list L from each element'
    average = sum1(L) / len(L)
    for i in range(len(L)):
        L[i] -= average


def normalized(L: list) -> list:
    # 'The function returns a normalized list. It should use the normalize function, cannot modify its argument. There is an error in the function.'
    L1 = []
    for i in L:
        L1 += [i]

    normalize(L1)
    return L1


#
# Functions that create new lists
#


def increased_even_with_zeros(L: list) -> list:  # [!] minor error
    # The function returns a list in which all even numbers are increased by 1, and odd ones are omitted.
    # Additionally, after each number, an additional element equal to 0 is added.
    result = []
    for n in L:
        if is_even(n):
            result.append(n + 1)  # If you prefer: result += [n+1]
        result.append(0)  # Again, you can: result += [0]
    return result


def smarter_version(L: list) -> list:  # [!]
    # The function returns a "smarter" version of the list L. It skips short words (length <= 3) as not smart enough,
    # additionally, after each word, it adds some smart word from the list of smart words.
    # The implementation below deviates significantly from the specification.

    smart_words = [
        "significantly",
        "fundamentally",
        "mentally",
        "rustically",
        "radically",
        "hey",
    ]

    result = []
    for word in L:
        if len(word) > 3:
            result += [word] + [random.choice(smart_words)]
    return result


###################################################################################
# Demonstration of operation
###################################################################################

L = [1, 2, 3, 4, 5]

print("For the list " + str(L) + " the sum of elements is")
print(sum1(L))
print(sum2(L))
print("If we sum only even ones, we get")
print(sum_even(L))
print("")

H = [1, 2, 3, 4, 5, 6, 7, 4, 8, 4, 8, 2, 2, 1, 10]
print("Histogram for the list " + str(H))
draw_histogram(H)
print("")

print("Starting with " + str(L) + " and incrementing 4 times")

increment_numbers(L)
print(L)  # we don't usually use semicolons, but I couldn't resist here
increment_numbers(L)
print(L)
increment_numbers(L)
print(L)
increment_numbers(L)
print(L)

L = [1, 2, 3, 4, 5]
L2 = L[:]

print("")
print("Starting with " + str(L2) + " and normalizing 3 times")

normalize(L2)
print(L2)
normalize(L2)
print(L2)
normalize(L2)
print(L2)

print("Why the same thing all the time?")

print("Oh, again:")

print(normalized(L))
print("Of course, we have " + str(L) + " == [1,2,3,4,5]")

print("")
print("Increasing even, skipping odd, and inserting 0 after")
print(increased_even_with_zeros(L))


print("Something smart at the end:")
Data = "programming in python is not that difficult at all".split(" ")
print(" ".join(smarter_version(Data)))
