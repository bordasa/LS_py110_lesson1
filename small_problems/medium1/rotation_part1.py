#input: a list
#output: a new list with the first element moved to the end of the list
#rules:
    #Do not modify the original list.
    #if input is empty list, return an empty list
    #if input is not a list, return None

#Algorithm
    #1. Check the input. If not list, return None
    #1.5 Check if list is empty. If empty, return empty list
    #2. Slice the list. Take the list minus 1st element.
    #3. Append 1st element to end.


#Code
def rotate_list(lst):
    if type(lst) is not list:
        return None
    
    if len(lst) < 2:
        return lst
    
    # first_part = lst[1:]
    # new_list = first_part + lst[:1]

    return lst[1:] + lst[:1]

#Examples:
print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

print(rotate_list(None) == None)
print(rotate_list(1) == None)

lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])

