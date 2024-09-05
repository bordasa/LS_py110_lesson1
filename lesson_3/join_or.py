def join_or(item_list, delimiter = ', ', connector = 'or'):

    item_list = [str(item) for item in item_list]

    if len(item_list) == 0:
        return ""
    elif len(item_list) == 1:
        return item_list[0]
    elif len(item_list) == 2:
        return f"{item_list[0]} {connector} {item_list[1]}"
    else:
        return f"{delimiter}".join(item_list[:-1]) + f"{delimiter}{connector} {item_list[-1]}"
    
print(join_or([1, 2, 3]))               # => "1, 2, or 3"
print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
print(join_or([]))                      # => ""
print(join_or([5]))                     # => "5"
print(join_or([1, 2]))                  # => "1 or 2"