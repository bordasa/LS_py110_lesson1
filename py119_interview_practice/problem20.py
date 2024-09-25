#Problem Overview:
    #Input: list of nums all of which are the same except 1
    #Output: the number in the list that differs from the rest
    #Rules: There will always be at least 3 numbers and exactly 1 diff

#Examples:

#Data Structure: set

#Algorithm:
    #make a set out of the list. This will definitely have 2 elements
    #check count of element[0] in original list
    #if count == 1, return element[0]
    #else, return element[1]

#Code

def what_is_different(lst):
    unique_elements = tuple(set(lst))

    if lst.count(unique_elements[0]) == 1:
        return unique_elements[0]
    else:
        return unique_elements[1]

print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)