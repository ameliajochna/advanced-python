def main():
    fact_digits = [] 
    fact_value = 1
    for i in range(1, 101):
        fact_value *= i
        fact_digits.append(len(str(fact_value)))

    for i in range(1, 101):
        digits_nr = fact_digits[i - 1]
        print(f"{i}! has {digits_nr} digits", end="")

        last_digit = digits_nr % 10
        sec_last_digits = int((digits_nr % 100) / 10)

        if digits_nr == 1:
            print(" digit")
        elif sec_last_digits == 1:
            print(" digits")
        elif last_digit == 2 or last_digit == 3 or last_digit == 4:
            print(" digits")
        else:
            print(" digits")


if __name__ == "__main__":
    main()
