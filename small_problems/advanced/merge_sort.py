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

def merge_sort(full_list):
    if len(full_list) <= 1:
        return full_list
    
    midpoint = len(full_list) // 2

    left_half = full_list[:midpoint]
    right_half = full_list[midpoint:]

    left_half = merge_sort(left_half)
    
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)


# All of these examples should print True
print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
print(merge_sort([5, 3]) == [3, 5])
print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
            'Kim', 'Bonnie']
expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
            'Sue', 'Tyler']
print(merge_sort(original) == expected)

original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
            43, 5, 25, 35, 18, 46]
expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
            35, 37, 43, 46, 51, 54]
print(merge_sort(original) == expected)