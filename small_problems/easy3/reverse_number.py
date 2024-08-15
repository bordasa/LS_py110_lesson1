#Input: positive integer
#Output: digits of the input, reversed
#Rules: nothing specific. No formatting needed



#Data Structure: Maybe use a list
#Algorithm:
    #1. Turn argument into string
    #2. Slice backwards through the string
    #3. Return the new string

#Code

def reverse_number(number):
    num_string = str(number)

    reversed_string = num_string[::-1]

    return int(reversed_string)

#Examples
print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True