#Problem Overview
#Input: String of digits
#Output: number of even numbered substrings that can be formed
    #Rules: If a substring occurs more than once, count each separately

#Examples:

#Data Structure: Strings and variables should be fine

#Algorithm:
    #1. Start from right, look for even numbers
    #2. When even number is found, add to count
    #3. Can add +1 for every other number to the left in string
    #4. Return Count after iterating through all digits

def even_substrings(digits_str):
    count = 0

    for index in range(-1, -(len(digits_str) + 1), -1):
        if int(digits_str[index]) % 2 == 0:
            num_of_substrings = (len(digits_str) + 1 + index)
            count += num_of_substrings
    
    return count

print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)