def remove_brackets(text):
    in_bracket = False
    result = ""
    for t in text:
        if t == "(":
            in_bracket = True
        elif t == ")":
            in_bracket = False
        elif not in_bracket:
            result += t
    return result
