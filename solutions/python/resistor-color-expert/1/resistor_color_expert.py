values = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}
tolerance = {
    "grey": "±0.05%",
    "violet": "±0.1%",
    "blue": "±0.25%",
    "green": "±0.5%",
    "brown": "±1%",
    "red": "±2%",
    "gold": "±5%",
    "silver": "±10%"
}
def resistor_label(colors):
    if len(colors) == 1:
        return "0 ohms"
    if len(colors) == 4:
        digit = colors[:2]
        multiplier = colors[2]
        tol = tolerance[colors[3]]
    elif len(colors) == 5:
        digit = colors[:3]
        multiplier = colors[3]
        tol = tolerance[colors[4]]
    num = ""
    for i in digit:
        num += str(values[i])
    value = int(num)
    ohms = int(num) * (10 ** values[multiplier])
    if ohms >= 1000000000:
        unit = "gigaohms"
        value = ohms/100000000
    elif ohms >=1000000:
        unit = "megaohms"
        value = ohms/1000000
    elif ohms >= 1000:
        unit = "kiloohms"
        value = ohms/1000
    else:
        unit = "ohms"
        value = ohms
    if value == int(value):
        value = int(value)
    return f"{value} {unit} {tol}"
    pass
