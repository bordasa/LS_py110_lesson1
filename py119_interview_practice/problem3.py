#Problem Overview
    #Input: string argument
    #Output: Copy of the string
        #Rules: make every 2nd character (%2!) of every 3rd word upper
            #All other characters remain the same
            #Punctuation works itself out?

#Examples:

#Data Structures: Manipulating strings
# and can use a list to split the input

#Algorithm:
    #1. Create a helper function to make the 2nd char upper in a word
    #2. Split the input string into a list
    #3. Iterate through the list, finding every 3rd word and replacing
    #4. Rejoin the list and return the final string

#Code

def char2_upper(word):
    if len(word) < 2:
        return word
    
    new_word_list = []

    for index, letter in enumerate(word, 1):
        if index % 2 == 0:
            letter = letter.upper()
        new_word_list.append(letter)
    
    return ''.join(new_word_list)

def to_weird_case(sentence):
    word_list = sentence.split()
    new_word_list = []

    for index, word in enumerate(word_list, 1):
        if index % 3 == 0:
            word = char2_upper(word)
        
        new_word_list.append(word)
    
    return ' '.join(new_word_list)

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)