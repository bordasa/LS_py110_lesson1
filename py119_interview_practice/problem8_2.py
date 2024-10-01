#Problem Overview
#Input: non-empty string, all lower
#Output: length of the longest vowel substring 'aeiou'

#Examples:

#Data Structure: Some variables should do the trick

#Algorithm:
    #create empty current_count and max_count
    #Iterate through the list
    #When you see a vowel, add to current count
    #when you see a consonant or end of the list:
        #if current_count > max_count, reset it
        #current_count = 0
    #return max count

#Code:
def longest_vowel_substring(string):
    current_count = 0
    max_count = 0

    for char in string:
        if char in 'aeiou':
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count

            current_count = 0

    return max(max_count, current_count) #in case it ends in a vowel

print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)