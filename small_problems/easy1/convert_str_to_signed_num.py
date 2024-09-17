def string_to_integer(num_string):
    dict_str_to_num = {
        '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9, '0': 0
    }

    if not num_string:
        return None
    
    result = 0

    for char in num_string:
        result *= 10
        result += dict_str_to_num[char]
    
    return result

def string_to_signed_integer(num_string):

    if not num_string:
        return None
    elif num_string[0] == "-":
        return -1 * string_to_integer(num_string[1:])
    elif num_string[0] == '+':
        return string_to_integer(num_string[1:])
    else:
        return string_to_integer(num_string)
    

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True