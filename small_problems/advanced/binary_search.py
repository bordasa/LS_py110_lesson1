def binary_search(lst, item):
    if len(lst) == 0:
        return 'Empty list'
    
    left = 0
    right = len(lst) - 1

    while left <= right: # not down to 1 element
        midpoint = (right + left) // 2
        guess = lst[midpoint]

        if guess == item:
            return midpoint
        elif guess > item:
            right = midpoint -1
        elif guess < item:
            left = midpoint + 1

    return -1
        
# All of these examples should print True
businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']
print(binary_search(businesses, 'Pizzeria') == 7)
print(binary_search(businesses, 'Apple Store') == 0)

print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
         'Tyler']
print(binary_search(names, 'Peter') == -1)
print(binary_search(names, 'Tyler') == 6)