def swap(list, index1, index2):
    list[index1], list[index2] = list[index2], list[index1]
    return list

def bubble_sort(list):
    if len(list) == 1:
        return list

    while True:
        swapped = False

        for index in range(1, len(list)):
            if list[index] < list[index - 1]:
                swap(list, index, index - 1)
                swapped = True
        
        if not swapped:
            break
    return list

lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True