#Problem Overview:
    #Input: string
    #Output: a dict
        #Rules: output dict -- keys = lower letters in str
                        #   -- values = how often the letter occurs in str

#Examples

#Data Struct: Dict

#Algorithm:
    #1. Iterate through string
    #2. If letter.islower(): add to dict or +1 to dict
    #3. Return dict

#Code

def count_letters(string):
    result_dict = {}

    for char in string:
        if char.islower():
            # if char in result_dict:
            #     result_dict[char] += 1
            # else:
            #     result_dict[char] = 1
            result_dict.setdefault(char, 0)
            result_dict[char] += 1
    
    return result_dict

expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})