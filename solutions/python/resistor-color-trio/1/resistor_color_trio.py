def label(colors):
    num = ""
    result = ''
    for i in colors:
        num += str(ind().index(i))
    last = num[2]
    main = num[:2]
    value = int(main) * (10 **(int(last)))
    if value >= 1000000000:
        result = str(value//1000000000) + " gigaohms"
    elif value >= 1000000:
        result = str(value//1000000) + " megaohms"
    elif value >= 1000:
        result = str(value//1000) + " kiloohms"
    else:
        result = str(value) + " ohms"
    return result
def ind():
    return [
       "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white"
    ]