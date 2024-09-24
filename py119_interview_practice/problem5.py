#Problem Overview
    #Input: string
    #output: the character that occurs the most often
        #Rules: consider upper and lower to be the same
                #if multiple chars have same freq, return the first one

#Examples

#Data Structures: Dictionary to track the freq of each letter

#Algorithm
    #1. Create a dictionary
    #2. For each char in string
        #2a. If char not in dict, add to dict with starting value 1
        #3a. If char is in dict, add 1 to the count
    #3. Return the key associated with the max value

#Code

def most_common_char(string):
    char_dict = {}

    for char in string:
        if char.casefold() not in char_dict:
            char_dict[char.casefold()] = 1
        else:
            char_dict[char.casefold()] += 1
    
    max_freq = 0

    for char, freq in char_dict.items():
        if freq > max_freq:
            max_freq = freq
            result = char
    
    return result


print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')