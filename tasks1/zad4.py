from tasks1.generate_fragments import generate_fragment


def generate_password(n: int) -> str:
    if n == 0:
        return "" 

    fragment = generate_fragment()
    while len(fragment) > n or n - len(fragment) == 1:
        fragment = generate_fragment()
    return generate_password(n - len(fragment)) + fragment


def main():
    n = 17
    print(generate_password(n))


if __name__ == "__main__":
    main()
