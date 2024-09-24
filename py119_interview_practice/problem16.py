#Problem Overview
    #Input: string
    #Output: count of distint, case-insensitive, 
    #   alpha-num that occur more than once
    #Rules - assume all strings only contain alphanumerics

#Examples:

#Data Structure: list or set of tuples using comprehension

#Algorithm:
    #1. For each char in string
    #2. convert to lower
    #3. get count in string
    #4. save both to the set as tuple
    #6. if count > 1
    #7. return len(set of tuples)

#Code
def distinct_multiples(alnum_str):
    str_list = [char.lower() for char in alnum_str]
    distinct_set = {(char, str_list.count(char)) for char in str_list
                    if str_list.count(char) > 1}
    
    return len(distinct_set)

print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5