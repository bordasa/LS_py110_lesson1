#Problem Overview
#Input: String
#Output: Dictionary
#Rules: Dict needs 3 things
    #1. % of chars in str that are lower
    #2. % of chars in str that are upper
    #3. % chars that are neither (whitespace, punct, special chars, etc.)
    #All %'s as str between "0.00" and "100.00". Round to 2 decimals
    #All input str will always contain at least 1 char

#Examples 


#Data Structures: manipulate str and save in dict

#Algorithm
    #1. iterate through str
    #2. If upper or lower, add to count of each. Remainder can be math'd
    #3. Calc %'s
    #4. Output using formatted str in dict

#Code

def letter_percentages(string):
    lowercase = 0
    uppercase = 0
    
    length = len(string)

    for char in string:
        if char.isalpha():
            if char == char.lower():
                lowercase += 1
            else:
                uppercase += 1

    lowercase /= length
    uppercase /= length
    neither = 1 - lowercase - uppercase

    result = {'lowercase': f'{round(lowercase * 100, 2):.2f}',
              'uppercase': f'{round(uppercase * 100, 2):.2f}',
              'neither': f'{round(neither * 100, 2):.2f}'
              }

    return result
    
expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)