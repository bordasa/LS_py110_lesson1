import string

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
        
        else:
            if word[-1] in string.punctuation:
                word = word_num_dict.get(word[:-1], word[:-1]) + word[-1]
        
        new_list.append(word)



    return ' '.join(new_list)

message = 'Please call me at five, five, five, one, two, three, four.'
print(word_to_digit(message) == "Please call me at 5, 5, 5, 1, 2, 3, 4.")
# Should print True