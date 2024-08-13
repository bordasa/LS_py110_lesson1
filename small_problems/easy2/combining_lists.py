#Problem
    #Input: 2 lists
    #Output: 1 set that is the union of the values from both lists
    #Rules:
        #No duplicate values
        #assume both arguments are always sets
        # lists may be any length and not necessarily the same

#Examples


#Data Structures:
    # Need to use a set

#Algorithm
    #Turn list 1 into a set.
    #Turn list 2 into a set.
    # return: Perform a union of the two.
    # Or iterate through set 2 and add each digit if its not in the set.

def union(list1, list2):
    result = set(list1)

    for num in list2:
        if num not in result:
            result.add(num)
    
    return result

#return set(list1).union(set(list2))

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True