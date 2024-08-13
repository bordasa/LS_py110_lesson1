#Problem
    #Input: list of positive integers
    #Output: the value of the multiplicative average as a string with 3 decimals
    #Rules: Output must be a string. Must have 3 decimals

#Examples:


#Data Structures:

#Algorithm
    #1. Multiply all of the numbers in the list
    #2. Divide the result by the length of the list
    #3. Round the result to 3 decimals
    #4. return the result as a string

#Code

def add_extra_zeros(num_string):
    decimal_idx = num_string.find('.')

    while len(num_string[decimal_idx + 1:]) < 3:
        num_string += '0'
    
    return num_string

def multiplicative_average(list):
    if not list:
        return "List is empty."

    product = 1

    for num in list:
        product *= num
    
    result = round((product / len(list)), 3)
    result = str(result)

    return add_extra_zeros(result)

# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")