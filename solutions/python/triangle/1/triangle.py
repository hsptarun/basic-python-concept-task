def equilateral(sides):
    if 0 in sides:
        return False
    elif (sides[0] == sides[1] == sides[2]):
        return True
    else:
        return False
    pass


def isosceles(sides):
    a, b, c = sides

    if 0 in sides:
        return False
    elif a==b==c:
            return True
    if a + b >= c and a + c >= b and b + c >= a:
        return (a==b!=c) or (a!=b==c) or (b!=c==a)
    else:
        return False
    
    pass


def scalene(sides):
    a, b, c = sides
    if 0 in sides:
        return False
    elif a + b >= c and a + c >= b and b + c >= a:
        if (a != b) and (b != c) and (a != c):
            return True
        else:
            return False
    else:
        return False
    pass
