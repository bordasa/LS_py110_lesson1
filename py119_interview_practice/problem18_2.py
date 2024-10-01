#Problem Overview:
    #Input: list of integers
    #Output: index N for which sum(list[:N]) == sum(list[N:])
    #Rules:
        # -if can't happen, return -1
        # -if multiples answer work, return smallest answer
        # -sum to the left of index 0 or right of index -1 = 0

#Examples:

#Data Structure: list slicing

#Algorithm:
    #1. Start at index 0. Iterate through each index. range(len(list))
    #2. For each index, check sum left == sum right
    #3. if yes, return N
    #4. return -1 if get through the list without returning

#Code
def equal_sum_index(lst):
    for N in range(len(lst)):
        if sum(lst[ :N]) == sum(lst[N + 1 :]):
            return N
    
    return -1

print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)