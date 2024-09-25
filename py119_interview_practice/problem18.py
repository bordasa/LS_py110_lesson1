#Problem Overview
    #Input: list of int
    #Output: the index for which all nums beefore = sum all numbers after
        #Rules: If no index works, return -1
            #If multiple answers exist, return the smallest index
            #sum left of index 0 = 0. Same after last element.

#Examples

#Data Structures: variables only. list slicing

#Algorithm:
    #1. Start at index 0 
    #2. left = 0, right = sum (remainder of list)
        #2a. If yes, return 0
    #3. Work thorugh full range of indexes up to len(list)
    #4. If none work, return -1

#Code
def equal_sum_index(lst):
    for index in range(len(lst)):
        left = sum(lst[:index])
        right = sum(lst[index + 1: ])

        if left == right:
            return index
    
    return -1

print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)