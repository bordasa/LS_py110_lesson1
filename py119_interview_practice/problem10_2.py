#Problem Overview
    #Input: string of digits
    #Output: number of even-numbered substrings
        #Rules: if substring occurs more than once, count each occurrence

#Examples:

#Data Structuree: strings

#Algorithm:
    #Idea: when you find an even digit, all numbers to the left + 1
    #Flip the string to make life easier?
    #iterate through string
    #For each char, if even, len(string) - index = number of substrings
    #add number to total count. return total count

#Code
def even_substrings(main_string):
    flipped_string = main_string[::-1]
    length = len(main_string)
    total_count = 0

    for index in range(length):
        if int(flipped_string[index]) % 2 == 0:
            total_count += (length - index)
    
    return total_count

print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)