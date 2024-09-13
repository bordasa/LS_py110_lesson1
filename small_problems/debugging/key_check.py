def get_key_value(my_dict, key):
    if key in my_dict:
        return my_dict[key]
    else:
        return None

print(get_key_value({"a": 1}, "b"))

'''
The code is raising an error because you cannot reference a value from a
dictionary that does not exist. As a result, the truthiness of the 
statement 'if my_dict[key]:' cannot be evaluated. I would fix this code
by changing the 'if' statement to read 'if key in my_dict:' or 
'if key in my_dict.keys():'
Simply using the 'get' method would also accomplish the same thing.
'return my_dict.get(key, None)'
'''