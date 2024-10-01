#Problem Overview
    #Input: two string arguments
    #Output: Number of times substring occurs in main_string
        #Rules:
            #Overlapping strings don't count. Assume substring never empty

#Examples:

#Data Structure: work with the strings I am given and variables

#Algorithm:
    #call split on the two  strings
    #take length  of output and subtract 1

#Code

def count_substrings(main_string, substring):
    split_string = main_string.split(substring)

    return len(split_string) - 1

print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)