# Input: String 
# Output: new string with all consonants doubled
# Rules: not doubled - 'aeiou', digits, punctuation, or whitespace
    #Only ascii characters

# Examples


#Algorithm
    #Look at each char of the string
    #Check to see if its a consonant
    #If yes, add it twice, if not, add it once to a new string
    #return the new string

#Code
def double_consonants(string):
    new_string = ""
    vowels = 'aeiou'

    for char in string:
        if char.isalpha() and char.casefold() not in vowels:
            new_string += char * 2
        else:
            new_string += char

    return new_string



# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")