#Problem Overview:
    #Input: list of nums
    #Output: the number in the list that differs from the rest
    #Rules: There will always be at least 3 numbers and exactly 1 answer

#Examples:

#Data Structures: Use a set

#Algorithm:
    #1. take input list and make a set
    #2. check each element (2 guaranteed)
        #2a. If element 0 has count 1 in list, return element 0
        #2b. else, return element 1

#Code
def what_is_different(input_list):
    input_set = set(input_list)
    input_set_list = list(input_set)

    if input_list.count(input_set_list[0]) == 1:
        return input_set_list[0]
    else:
        return input_set_list[1]
    
print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)