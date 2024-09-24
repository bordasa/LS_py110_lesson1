#Problem Overview
    #input: 2 strings
    #Output: True if substring in string1 can be rearranged to match string2
            #Else, False
            #Assume all lowercase alphabetic characters
            #Assume no empty strings

#Example

#Data Structure: dictionary

#Algorithm:
    #1. Iterate through string1
    #2. Add char to dict and/or increment count
    #3. Make dict for string2
    #4. Make sure that there are enough count in dict1 for each value in dict2

#Code

def make_count_dict(string):
    char_count_dict = {}
    for char in string:
        char_count_dict.setdefault(char, 0)
        char_count_dict[char] += 1
    
    return char_count_dict


def unscramble(string1, string2):
    char_count_dict1 = make_count_dict(string1)
    char_count_dict2 = make_count_dict(string2)

    for char, count in char_count_dict2.items():
        if char_count_dict1.get(char, 0) < count:
            return False
    
    return True

print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)