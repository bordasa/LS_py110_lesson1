#Problem Overview
    #Input: 2 strings as arguments
    #Output: True if some portion of the chars in string1 can rearrange
            #to  match the chars in string2. Else False
        #Rules:
            #both strings only contain lower alphanumerics
            #No empty strings

#Examples:

#Data Structures: Use 2 dictionaries

#Algorithm:
    #1. Make a count dict for string1 and string2
    #2. Iterate through counts in string2 dict.
    #3. If count in string1_dict < count in string2_dict, return False
    #4. Else, return True

#Code:
def make_count_dict(string):
    count_dict = {}

    for char in string:
        count_dict.setdefault(char, 0)
        count_dict[char] += 1
    
    return count_dict

def unscramble(string1, string2):
    string1_dict = make_count_dict(string1)
    string2_dict = make_count_dict(string2)

    for char, count in string2_dict.items():
        if string1_dict.get(char, 0) < count:
            return False
    
    return True

print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)