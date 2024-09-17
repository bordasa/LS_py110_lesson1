#Problem Overview
    #Input: string of digits
    #output: the appropriate number as an integer
    #Rules: No standard conversion functions available in Python
        #Must use each character as a string
        #For now, do not worry about + or -
        #Assume all characters are numeric

#Examples

#Data Structures: dictionary to look up numbers?

#Algorithm:
    # Create dictionary to look up each string and its corresponding int
    # Get input String
    # start at 1st index.
    # Convert to integer and save as result
    # At next index, multiply previous result x 10 then add new char/int
    # Repeat until no more characters remain
    # Return Result

#Code

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

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True
