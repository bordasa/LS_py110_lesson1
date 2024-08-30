def intersection(l1, l2):
    frozenset1 = frozenset(l1)
    frozenset2 = frozenset(l2)

    return frozenset1.intersection(frozenset2)

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result)