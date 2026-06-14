def is_valid(isbn):
    sum = 0
    i = 10
    isbn = isbn.replace("-","")
    if len(isbn) !=10:
        return False
    for digit in isbn:
            
        if digit == 'X' and i == 1:
            sum += (10*i)
            
        elif digit.isdigit():
            sum += int(digit) * i
        else:
            return False
        i -= 1

    return sum % 11 == 0
