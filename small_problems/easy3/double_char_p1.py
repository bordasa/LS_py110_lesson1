#Input: a string
#Output: a new string with each char doubled
#Rules: none
#Examples:
#Algorithm:
    #Iterate through the char in string
    #add the character twice to a new string
    #return the new string

#Code

def repeater(string):
    new_string = ""

    for char in string:
        new_string += (char * 2)
    
    return new_string

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True