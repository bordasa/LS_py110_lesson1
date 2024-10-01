#Problem Overview:
    #Input: string
    #Output: count of distinct case-insensitive alphanumeric char > 1
        #Rules: Assume input string only has alphanumeric chars

#Examples:

#Data Structure: Dict

#Algorithm:
    #1. Create a count dict for each alnum
    #2. list comp for dict.items() with value > 1
    #3. return len(list)

#Code
def make_count_dict(string):
    count_dict = {}

    for char in string:
        count_dict.setdefault(char, 0)
        count_dict[char] += 1
    
    return count_dict

def distinct_multiples(alnum_string):
    alnum_dict = make_count_dict(alnum_string.lower())

    distinct_multiples_list = [char for char, value in alnum_dict.items()
                               if value > 1]
    
    return len(distinct_multiples_list)

print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5