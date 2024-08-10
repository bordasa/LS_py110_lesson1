## Input:
# -A list of strings

## Output:
# -New list with strings sorted based on highest num of adjacent consonants

## Rules
# - New string should be sorted highest to lowest
# - If 2 strings contain the same highest num of adjacent consonants,
#   they should retain the original order with each other
# - Adjacent consonants = next to each other in same word or separated by space in adjacent words
# - No empty strings
# - Single consonants in a string do not affect sort order in comparison to strings with no consonants. Only adjacent consonants affect sort order.
# - String may contain multiple words

## Questions:
# Should an empty list return an empty list?
# Are multiple spaces OK between consonants?

## Data Structure: Probably going to use a dictionary

## Algorithm
## 1. Look at the first word in the list
## 2. Determine the number of adjacent consonants
## 3. Add the word to a dictionary as the key with the adjacent consonants as value
## 4. Repeat with the next word until you reach the last word in list
## 5. Sort words by adding them to a new list based on highest value first
## 6. Return the new list

def count_max_adjacent_consonants(my_string):
    no_spaces = my_string.replace(' ', '')

    adj_consonant_tracker = []
    max_num_adj_consonants = 0

    for char in no_spaces:
        if char not in ['a', 'e', 'i', 'o', 'u', 'y']:
            adj_consonant_tracker.append(char)
            max_num_adj_consonants = len(adj_consonant_tracker)

        else:
            if len(adj_consonant_tracker) > max_num_adj_consonants:
                max_num_adj_consonants = len(adj_consonant_tracker)
            
            adj_consonant_tracker.clear()
    
    if max_num_adj_consonants > 1:
        return max_num_adj_consonants
    else:
        return 0

print(count_max_adjacent_consonants('month'))       # 3
# print(count_max_adjacent_consonants('ccaa') == 2)        # 2
# print(count_max_adjacent_consonants('baa') == 0)         # 0
# print(count_max_adjacent_consonants('aa') == 0)          # 0
# print(count_max_adjacent_consonants('rstafgdjecc') == 4) # 4

def sort_by_consonant_count(my_list):

    tracking_list = []

    for string in my_list:
        max_adj_cons = count_max_adjacent_consonants(string)
        tracking_list.append((max_adj_cons, string))

    final_list = []
    max_adj_cons_tracker = -1

    while tracking_list:
        for item in tracking_list:
            if item[0] > max_adj_cons_tracker:
                word_to_add = item[1]
                max_adj_cons_tracker = item[0]
        
        final_list.append(word_to_add)
        tracking_list.remove((max_adj_cons_tracker, word_to_add))
        max_adj_cons_tracker = -1

    return final_list


my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']