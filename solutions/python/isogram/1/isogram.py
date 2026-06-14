def is_isogram(string):
    string = string.lower()
    seen = []
    for char in string:
        if char == " " or char == "-":
            continue
        if char in seen:
            return False
        seen.append(char)
    return True
