# ## PEDAC

# Problem-------------
# Input: String (can be more than 1 word from ex)
# Output: True/ False

# -Explicit Rules:
#   - If palindrome, True
#   - If not palindrome, False
#   - Case matters and all characters matter
# -Implied Rules:
#   -Strings can contain any character, so mult words/symbols

# -Questions:

# Examples------------------
# All of these examples should print True

# print(is_palindrome('madam') == True)
# print(is_palindrome('356653') == True)
# print(is_palindrome('356635') == False)

# # case matters
# print(is_palindrome('Madam') == False)

# # all characters matter
# print(is_palindrome("madam i'm adam") == False)

# Data Structures-------------------------
# None needed

# Algorithms-------------
# Use string slicing backwards to get reversed string
# Assign reversed string to a var
# check if var is equivalent to old string

# Code

def is_palindrome(word):

    backwards = word[::-1]

    if word == backwards:
        return True
    else:
        return False
    

# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)

# LS answer is simpler: 
# def is_palindrome(s):
#    return s == s[::-1]