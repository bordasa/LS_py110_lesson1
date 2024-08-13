#Problem
    #Input: 2 lists
    #Output: new list that contains all elements from both list arguments
    # Rules: each element taken in alternation.
    # both lists are non-empty
    # both lists have the same number of elements

#Examples


#Data Structure
# - lists

#Algorithm
    #create 1 pointer that works on both lists
    #create an empty list
    #iterate through the list, adding each element 1 by 1 to the new list
    #return the new list

#Code

def interleave(list1, list2):
    # list_length = len(list1)
    # new_list = []

    # idx = 0

    # while idx < list_length:
    #     new_list.append(list1[idx])
    #     new_list.append(list2[idx])
    #     idx += 1
    
    # return new_list
#--------------------------------
    # result = []

    # for idx in range(len(list1)):
    #     result.extend([list1[idx], list2[idx]])
    
    # return result
#---------------------------------

    zipped_lists = zip(list1, list2)
    new_list = []

    for pair in zipped_lists:
        for item in pair:
            new_list.append(item)

    return new_list

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True