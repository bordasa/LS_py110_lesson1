#Input: integer (always positive)
#Output: a list containing all integers between 1 and the argument (inclusive)
#Rules: List in ascending order

#Examples

#Data Structures: List

#Algorithm:
    #1. add 1 to the input
    #2. Find the range to the new number
    #3. Convert it to a list

#Code

def sequence(number):
    return list(range(1, number + 1))


print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True