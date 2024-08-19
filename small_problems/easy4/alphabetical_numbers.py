#input: a list of integers 0 to 19
#output: a list of integers sorted by the English word for each num
#Rules: Implicit: don't mutate the list?

#Examples

# input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
#               10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
#                    7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

# print(alphabetic_number_sort(input_list) == expected_result)
# # Prints True

#Data Structures - list or dict

#Algorithm
    #Create a dict to convert numbers to string words
    #Iterate through the input list
    #Convert each letter to its english word
    #Sort by the english word
    #Output the new, sorted list

#Code
def num_to_english(num):
    num_dict = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen', 
        15: 'fifteen', 
        16: 'sixteen', 
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen'
    }
    return num_dict[num]

def alphabetic_number_sort(input_list):
    sorted_english = sorted(input_list, key = num_to_english)
    return sorted_english


input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True