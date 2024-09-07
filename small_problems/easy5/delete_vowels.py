def remove_vowels(my_list):
    vowels = 'aeiou'
    no_vowels_list = []

    for string in my_list:
        new_string = ''

        for letter in string:
            if letter.casefold() not in vowels:
                new_string += letter
        
        no_vowels_list.append(new_string)
    
    return no_vowels_list

# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True