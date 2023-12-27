def remove_duplicates(input_list):
    indexed_list = [(value, index) for index, value in enumerate(input_list)]
    indexed_list.sort()

    unique_list = []

    for item in indexed_list:
        if not unique_list or unique_list[-1][1] != item[0]:
            unique_list.append((item[1], item[0]))

    unique_list.sort()

    result = [item[1] for item in unique_list]
    return result


def main():
    input_list = [1, 2, 3, 1, 2, 3, 8, 2, 2, 2, 9, 9, 4]
    print(remove_duplicates(input_list))


if __name__ == "__main__":
    main()
