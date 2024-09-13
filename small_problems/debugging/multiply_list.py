def multiply_list(lst):
    new_list = []
    for item in lst:
        new_list.append(item * 2)

    return new_list

print(multiply_list([1, 2, 3]) == [2, 4, 6])

'''
In the above function, a new variable is being created and used to iterate
through the list, however the list is not being modified when the variable
'item' is reassigned. In order to fix this bug, the mutated item should be
 appended to a new list. A list comprehension would also produce a new list.
 
The loop variable is being modified but this does not change the elements
of the list. The 'item' variable is a separate reference to each list
element, so changing this variable does not mutate the original list.
'''