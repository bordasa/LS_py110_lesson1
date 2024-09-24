#Problem Overview
    #Input: 2 strings
    #Output: num ofo times that the second string occurs in the first
        #rules: overlapping strings don't count
                #Assume the second argument is never empty

#EXamples

#Data Structures: Can probably get it done with list slicing alone. Just vars

#Algorithm:
    #Get len(string2)
    #Use string1.find(string2)
        #if -1, return 0
        #else index + len(string2) = start of new string
    #repeat until find = -1 should be enough?

#code

def count_substrings(string, substr):
    substr_len = len(substr)
    index = string.find(substr)
    count = 0

    if index == -1:
        return count
    
    new_string = string[index + substr_len :]
    
    while True:
        count += 1
        index = new_string.find(substr)

        if index == -1:
            break
    
        new_string = new_string[index + substr_len :]
    
    return count

print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)