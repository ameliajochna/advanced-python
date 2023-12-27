def sum_calibration_values(text):
    # Extract digits from each word, sum the reversed pairs of digits, and calculate the total sum
    return sum(
        [
            sum(
                int(
                    c1 + c2,
                )
                for c1 in word
                if c1.isdigit()
                for c2 in reversed(word)
                if c2.isdigit()
            )
            for word in text
        ]
    )


def main():
    with open("calibration.txt") as file:
        # Read lines from the file and calculate the sum of calibration values
        lines = file.read().splitlines()
        result = sum_calibration_values(lines)
        print(result)


if __name__ == "__main__":
    main()
