#Problem:
    #Input: a positive integer
    #Output: sum of its digits

#Algorithm:
    #1. stringify the number
    #2. split the string into a list
    #3. Turn each item back into an int
    #4. Sum the values

#Code
# def sum_digits(num):
#     string_num = str(num)
#     string_list = list(string_num)
#     total = 0

#     for strnum in string_list:
#         total += int(strnum)
    
#     return total

# def sum_digits(num):
#     total = 0

#     for digit in str(num):
#         total += int(digit)
    
#     return total

def sum_digits(num):
    return sum([int(digit) for digit in str(num)])

#Examples
print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True