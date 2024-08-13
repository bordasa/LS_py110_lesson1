#Input:
    #string of digits
#Output:
    # integer
#Rules:
    #cannot use int()
    #calc result using the chars in string
    #do not worry about + - in front
    #do not worry about invalid characters
    #assume all characters are numeric

# #Examples:


# Data Structures:

# Algorithm
    #create a dictionary that translates each string digit as key to integer as value
    #set value to zero
    #iterate through string
    #multiply 10 by the previous value and add it to the current digit. Set this to new value
    # return value

def string_to_integer(string):
    integer_dict = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }

    value = 0

    for number in string:
        value = (10 * value) + integer_dict[number]

    return value


print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True