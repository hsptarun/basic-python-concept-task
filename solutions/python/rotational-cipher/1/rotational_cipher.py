def rotate(text, key):
    cipher = ""

    for ele in text:

        if ele.islower():

            ele = ord(ele) + key

            if ele > 122:
                ele = 97 + (ele - 123)

            cipher += chr(ele)

        elif ele.isupper():

            ele = ord(ele) + key

            if ele > 90:
                ele = 65 + (ele - 91)

            cipher += chr(ele)

        else:
            cipher += ele

    return cipher