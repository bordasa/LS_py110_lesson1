#Problem Overview
    #Input: string
    #Output: True if pangram, False if not
        #Rules: pangram contains every letter of the alphabet at least once

#Examples:

#Data Structure: Using a set will simplify the problem

#Algorithm:
    #1. for each char in string, if char.isalpha(), add to set
    #2. Check count of set. if == 26, return True, else False

#Code
def is_pangram(string):
    char_set = set()

    for char in string:
        if char.isalpha():
            char_set.update(char.lower())
    
    return len(char_set) == 26

print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)