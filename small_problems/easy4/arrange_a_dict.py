#input: a dict
#output: a list of the keys sorted by the values of each key
#rules: Assume all values are distinct?

#algorithm:
    #1. Accept the dict
    #2. Save the first key and value
    #3. Iterate through the dictionary, checking the values
    #4. If key isn't in list and is lower than the saved one, save this one
    #5. Add to the list
    #6. Repeat
    #OR
    #1. Swap the keys and values, turn them into tuples
    #2. Sort the new tuples
    #3. Take the keys from the tuples

# def order_by_value(my_dict):
#     value_first_list = [(value, key) for key, value in my_dict.items()]

#     value_first_list.sort()

#     return [item[1] for item in value_first_list]

def sort_keys(item):
    return item[1]

def order_by_value(my_dict):
    sorted_items = sorted(my_dict.items(), key=sort_keys)

    return [key for key, value in sorted_items]

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True