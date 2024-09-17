def integer_to_string(num):
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    new_num, rightmost = divmod(num, 10)
    result = DIGITS[rightmost]

    while new_num > 0:
        new_num, rightmost = divmod(new_num, 10)
        result = DIGITS[rightmost] + result
    
    return result

def signed_integer_to_string(num):
    if num < 0:
        return '-' + integer_to_string(-1 * num)
    elif num > 0:
        return '+' + integer_to_string(num)
    else:
        return '0'
    

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True