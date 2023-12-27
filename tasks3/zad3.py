def remove_brackets(tekst):
    bracket = False
    wynik = ""
    for t in tekst:
        if t == "(":
            bracket = True
        elif t == ")":
            bracket = False
        elif not bracket:
            wynik += t
    return wynik
