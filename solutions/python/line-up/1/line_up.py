def line_up(name, number):
    if number % 100 in (11, 12, 13):
        suffix = "th"
    elif number % 10 == 1:
        suffix = "st"
    elif number % 10 == 2:
        suffix = "nd"
    elif number % 10 == 3:
        suffix = "rd"
    else:
        suffix = "th"

    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"