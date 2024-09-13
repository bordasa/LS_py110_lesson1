import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original)

original[0][0] = 99

print(copied[0] == [1])

'''
The problem in this code is that 'copy.copy()' creates a shallow copy of
the list. In a shallow copy, a new outer list is created but 
nested lists are not duplicated, only
references to the nested lists are created in the new list. As a result,
both lists are affected by changes to the nested lists because they share
references to the same lists.
In order to fix this, 'copy.deepcopy()' should be used in order to ensure
that new objects are created for each object referenced within the new
list.
'''