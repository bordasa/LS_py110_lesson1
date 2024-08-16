#input: list
#output: reversed elements in place
#rules: no list.reverse method ad no slicing

#Example:

#Algorithm
    #1. look at every element of the list
    #2. swap each beginning element with eacch end element until you have gone through half the list
    #3. Return the list

def reverse_list(list):
    
    middle_index = len(list) // 2

    for i in range(middle_index):
        list[i], list[-i - 1] = list[-i - 1], list[i]
    
    return list



list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True
