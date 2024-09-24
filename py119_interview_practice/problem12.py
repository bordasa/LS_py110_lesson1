#Problem Overview
    #Input: string
    #Output: bool
        #Rules: True if pangram, False if not
        #pangram contains every letter in the alphabet

#Example

#Data Structure: Use a set

#Algorithm:
    #1. look at every char in string
    #2. if char is alpha, add to set. else skip
    #3. Check the size of the set. If == 26, return True. else False

#Code

def is_pangram(string):
    alpha_set = {char.lower() for char in string if char.isalpha()}

    if len(alpha_set) == 26:
        return True
    else:
        return False
    

print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)