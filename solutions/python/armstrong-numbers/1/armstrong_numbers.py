def is_armstrong_number(number):
    sum = 0
    count = 0;
    num = number
    num2 = number
    while num > 0:
        digit = num % 10
        count += 1
        num //= 10

    while num2 > 0:
        digit = num2 % 10
        sum += (digit**count)
        num2 //= 10

    if sum == number:
        return True
    else :
        return False
    pass
