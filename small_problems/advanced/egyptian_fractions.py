#Problem 1 Overview
    #Input: 1 number (Rational)
    #Output: A list of the denominators that make an Egyptian Fraction
    #Rules:
        #Use the Fraction class from fractions module
        #Results may differ
        #Assume the input is a correct rational number

#Examples

#Data Structures: Lists and Vars

#Algorithm
    #1. Get input number
    #2. If the number is less than 1, start with the denominator of the input
    #3. If the number is greater than 1, start with 1
    #4. Subtract Fraction(1, denom) from the current num, append D to list
        #4a. If the 1/new_num % 1 == 0 (whole number), list.append(whole num)
        #4b. Else: denom + 1 and repeat
    #5. return list

#Code
from fractions import Fraction

# def egyptian(rat_num):
#     denom = 1
#     denom_list = [denom]
#     new_num = rat_num - Fraction(1, denom)

#     while True:
#         denom += 1
#         if Fraction(1, denom) < new_num:
#             new_num -= Fraction(1, denom)
#             denom_list.append(denom)
        

#         if Fraction(new_num).numerator == 1 and Fraction(new_num).denominator not in denom_list:
#             denom = Fraction(new_num).denominator
#             denom_list.append(denom)
#             # print(denom_list)
#             # print(new_num)
#             break

#     return denom_list

def egyptian(target_value):
    denominators = []
    unit_denominator = 1

    while target_value != 0:
        unit_fraction = Fraction(1, unit_denominator)

        if unit_fraction <= target_value:
            target_value -= unit_fraction
            denominators.append(unit_denominator)

        unit_denominator += 1

    return denominators

def unegyptian(list):
    return sum([Fraction(1, d) for d in list])

print(egyptian(Fraction(2, 1)))
print(egyptian(Fraction(137, 60)))
print(egyptian(Fraction(3, 1)))
print(egyptian(Fraction(1, 2)))

# Using the unegyptian function
# All of these examples should print True
print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))