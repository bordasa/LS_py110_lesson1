#Input
    #string of words separated by spaces
#Output
    #string of words with first and last letter in each word swapped
#Rules
    #Every word contains at least 1 letter
    #the string will always contain at least one word
    #each string contains nothing but words and spaces
    #no leading, trailing or repeated spaces

# #Examples


# Data Structure
#   probably a list to iterate through

# Algorithm
    #Split the string at the spaces and assign it to a new list
    #Iterate through the list of words
    #Swap the first and last letter in each word
    #replace the word in the list with the swapped word
    #Join the final list into a new string
    #return the new string

# Code
def swap(s):
    words_list = s.split()
    swapped_words = []

    for word in words_list:
        new_word = ''

        if len(word) < 2:
            new_word = word

        else:
            new_word += word[-1] + word[1:-1] + word[0]
        
        swapped_words.append(new_word)
    
    result = ' '.join(swapped_words)

    return result
    



print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True