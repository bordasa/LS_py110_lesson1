data_set = {1, 2, 3, 4, 5}
copy = data_set.copy()

for item in data_set:
    if item % 2 == 0:
        copy.remove(item)

print(copy)

data_set = {1, 2, 3, 4, 5}
remove_set = set()
for item in data_set:
    if item % 2 == 0:
        remove_set.add(item)

data_set -= remove_set
print(data_set)
'''
The code is throwing an error because we are itarating over a set that
is being modified. When we are mutating the set that we are iterating over,
unexpected behaviors will occur. It is best practice to not modify a list
or set when we are iterating over it, and to instead use a new object.
To fix this, we can save the items we want to remove in a new set and
remove them from the set when we are done iterating. Or we can make a copy
of the set and remove items from the copy.
'''

'''
Using set comprehensions would achieve this result in a more simple way.
'''
data_set = {1, 2, 3, 4, 5}

data_set = {item for item in data_set if item % 2 != 0}
print(data_set)
