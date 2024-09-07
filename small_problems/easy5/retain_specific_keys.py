def keep_keys(my_dict, selected_keys):
    return {key: my_dict[key]
            for key in my_dict
            if key in selected_keys}

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True