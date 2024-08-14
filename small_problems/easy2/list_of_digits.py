#Problem
    #Input: a positive integer
    #Output: a list of the digits in the number
    #Rules: output is in the order of the input

#Examples:


#Data Structures: list

#Algorithm:
    #1. Turn the input into a string
    #2. Iterate through the string
    #3. Add to a list and convert to integer again
    #4. Return list

#Code

def digit_list(number):
    return [int(num) for num in str(number)]


print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True