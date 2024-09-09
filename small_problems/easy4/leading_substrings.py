# def leading_substrings(string):
#     idx = 1
#     substrings = []

#     while idx <= len(string):
#         substrings.append(string[:idx])
#         idx += 1
    
#     return substrings

def leading_substrings(string):
    return [string[:idx + 1] for idx in range(len(string))]

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])