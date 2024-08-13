# Problem
    #Input: 1 list
    #Output 1 list of 2 lists
    #Rules: if odd number, the first list has an extra value
        # if empty, returns 2 empty strings
        # values are in the same order

#Examples



#Data Structures: Lists

#Algorithm:
    #Find the middle index of the input list
    #Output a list of 2 lists that are slices of the input list

#code:

def halvsies(list):

    list_length = len(list)

    middle_index = list_length // 2

    if list_length % 2 == 1:
        middle_index += 1

    return [list[: middle_index], list[middle_index: ]]

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
# print(halvsies([5]) == [[5], []])
# print(halvsies([]) == [[], []])