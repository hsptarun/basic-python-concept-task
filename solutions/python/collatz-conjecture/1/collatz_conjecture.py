def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    step = 0
    
    while(number != 1):
        if number % 2 == 0:
            step += 1
            number = number//2
            
        elif number % 2 != 0:
            number = number*3 +1
            step += 1
    return step
    pass
