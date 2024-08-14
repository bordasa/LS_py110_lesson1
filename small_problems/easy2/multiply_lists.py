#Problem
    #Input: 2 lists
    #Output: 1 list multiplying elements from the inputs that have same index
    #Rules: Both lists are the same length

#Examples:

#Data Structures: Lists

#Algorithm:
    #1. track index. Start at 0
    #2. make an empty results list
    #3. append the product of the two elements at the index
    #4. Increment the index until all elements have been seen
    #5. REturn the result list

# def multiply_list(list1, list2):
#     idx = 0
#     product_list = []

#     while idx < len(list1):
#         product_list.append(list1[idx] * list2[idx])

#         idx += 1
    
#     return product_list

# def multiply_list(list1, list2):
#     result = []

#     for idx in range(len(list1)):
#         result.append(list1[idx] * list2[idx])
    
#     return result

def multiply_list(list1, list2):
    return [num1 * num2 for (num1, num2) in zip(list1, list2)]

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True