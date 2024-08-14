#Input: a string consistingn of zero or more space-separated words
#Output: a dict that shows the number of words of different sizes
# Rules
    # Explicit
    # input is a string. String can be empty.
    # words consisst of any sequence of non-space characters
    # from ex. if string is empty, return an empty dict

# Examples


# Data Structures: take a list and make a dict

# Algorithm:
    # -Initialize an empty dict
    # -Split string by spaces. Save as a new list
    # -Get the len of each word in the string
    # -Add each len to a dict as key.
    # -Update Value by adding 1 each time len comes up
    # -Return dict

# Code

def word_sizes(string):
    result = {}

    string_list = string.split()
    # remember the default is to split at spaces but if I put a space in the split it changes the output

    for word in string_list:
        length = len(word)

        if length in result:
            result[length] += 1
        
        else:
            result[length] = 1

    return result



# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})
