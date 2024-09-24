#Problem Overview
    #Input: Non-Empty String
    #Output: length of longest vowel substring
    #Rules: vowels are "aeiou"
            #String will only be lowercase letters

#Examples

#Data Structure: list?

#Algorithm:
    #Create tracking list
    #iterate through string
    #If char in vowels: count += 1
    #if char not in vowelse: add count to list. set count to 0
    #Index += 1
    #return max of tracking list

#Code

def longest_vowel_substring(string):
    tracking_list = []
    index, count = 0, 0

    while index < len(string):
        if string[index] in 'aeiou':
            count += 1
        else:
            tracking_list.append(count)
            count = 0
        
        index += 1
    
    tracking_list.append(count)

    return max(tracking_list)

print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)