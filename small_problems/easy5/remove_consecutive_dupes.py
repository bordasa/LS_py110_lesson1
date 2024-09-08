def unique_sequence(list):
    if not list:
        return []
    
    new_list = [list[0]]

    for num in list[1:]:
        if num != new_list[-1]:
            new_list.append(num)
 
    return new_list


original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True

print(unique_sequence([]))