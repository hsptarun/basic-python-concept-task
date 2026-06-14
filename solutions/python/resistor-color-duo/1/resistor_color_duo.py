def value(colors):
    num = ""
    for i in colors[:2]:
        num += str(ind().index(i))
    return int(num)
    pass
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