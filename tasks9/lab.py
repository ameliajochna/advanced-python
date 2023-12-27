def sum_calibration_values(text):
    return sum(
        [
            [
                int(c1 + c2)
                for c1 in word
                if c1 >= '0' and c1 <= '9'
                for c2 in reversed(word)
                if c2 >= '0' and c2 <= '9'
            ][0]
            for word in text
        ]
    )


def main():
    f = open('calibration.txt')
    print(sum_calibration_values(f.read().splitlines()))


if __name__ == '__main__':
    main()
