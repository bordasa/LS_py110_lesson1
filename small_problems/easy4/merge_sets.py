def merge_sets(l1, l2):
    set1 = set(l1)
    set2 = set(l2)

    return set1.union(set2)

list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]

print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})


