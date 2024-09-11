# def merge(list1, list2):
#     sorted_list = []

#     pointer1 = 0
#     pointer2 = 0

#     while pointer1 < len(list1) and pointer2 < len(list2):
#         if list1[pointer1] <= list2[pointer2]:
#             sorted_list.append(list1[pointer1])
#             pointer1 += 1
#         else:
#             sorted_list.append(list2[pointer2])
#             pointer2 += 1
        
#     if pointer1 == len(list1):
#         sorted_list += list2[pointer2:]
#     else:
#         sorted_list += list1[pointer1:]

#     return sorted_list

def merge(list1, list2):
    copy1 = list1.copy()
    copy2 = list2.copy()
    merged_list = []

    while copy1 and copy2:
        if copy1[0] <= copy2[0]:
            merged_list.append(copy1.pop(0))
        else:
            merged_list.append(copy2.pop(0))
    
    return merged_list + copy1 + copy2

# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)