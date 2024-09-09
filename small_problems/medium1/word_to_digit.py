#Input: Strings
#Output: String with number words converted to numbers
#Rules: Assume no punctuation

#Algorithm:
    #1. Create a dictionary with keys of word numbers and values of integers
    #2. Convert message into a list
    #3. Iterate through list, if word is in dic, convert word
    #4. Join the list into a string

#Code:

def word_to_digit(message_string):
    message_list = message_string.split()
    new_list = []

    word_num_dict = {'zero': '0',
                     'one': '1',
                     'two': '2',
                     'three': '3',
                     'four': '4',
                     'five': '5',
                     'six': '6',
                     'seven': '7',
                     'eight': '8',
                     'nine': '9'
                     }

    for word in message_list:
        if word in word_num_dict.keys():
            word = word_num_dict[word]
        
        new_list.append(word)

    # new_list1 = [word_num_dict.get(word, word) for word in message_list]
    
    # print(new_list1)


    return ' '.join(new_list)
    

#Example:
message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == 'Please call me at 5 5 5 1 2 3 4')