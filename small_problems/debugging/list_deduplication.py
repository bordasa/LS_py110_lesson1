data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = []

for num in data:
    if num not in unique_data:
        unique_data.append(num)

print(unique_data == [4, 2, 1, 3]) # order not guaranteed

'''
In order to preserve the order of the elements in the list, we could simply
use a for loop to iterate throuogh the 'data' list and only add the items
to the 'unique_data' list if they are not already contained in the
'unique_data' list.
'''