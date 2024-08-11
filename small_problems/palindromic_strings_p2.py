# PEDAC

# Problem --- 
# -Input: String
# -Output: True/False
# - Explicit Rules
#     -Same as part 1, but now ignore non-letters and now case insensitive
# - Implicit Rules
# - Questions

# Examples ---


# Data Structures ---
# Can probably get away with just using strings

# Algorithm ---
# -1. check that all characters are alpha numeric
# -2. save as a new string
# -3. make the new string all lowercase
# -4. Compare new string to itself backwards

# Code ----

def is_real_palindrome(word):

    new_word = ''
    for char in word:
        if char.isalnum():
            new_word += char.casefold()
    
    return new_word == new_word[::-1]

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True
# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True
#only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True


# cleaned string is a better variable name. That is what LS solution has