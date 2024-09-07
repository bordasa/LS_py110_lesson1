def multiply_items(list1, list2):
    return [num1 * num2 for num1, num2 in zip(list1, list2)]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True