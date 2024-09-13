# def append_to_list(value, lst=[]):
#     new_list = lst + [value]
#     return new_list

# print(append_to_list(1))# == [1])
# print(append_to_list(2))# == [2])
# print(append_to_list(3))
# print(append_to_list(0))

'''
The list is mutating and returning the list that is
set as the default argument. As a result, each time the function is called
without a list argument, items are being added to the defualt argument.
In order to fix this, I would return a new list that adds the new value
without mutating the default list (not using the append method).

'''
'''
Better solution, from LS:
default mutable arguments are shared between function calls. It is better
to set a condition for if the there is no default list, and create a
new, fresh, empty list for the return value if needed.
'''

def append_to_list(value, lst= None):
    if lst == None:
        lst = []
    
    lst.append(value)
    return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])