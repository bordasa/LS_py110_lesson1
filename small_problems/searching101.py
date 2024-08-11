# PEDAC
# Problem
## Input: 6 numbers, 5 main and 1 last one
## Output: 1 sentence. If the last number appears in the first 5

# Rules:
# -1. Must ask user for 6 numbers
# -2. The number either is explicitly in the list of the first 5 or its not
# -3. Implied: No need to handle user putting in the wrong input?

# Examples
# 2 given in the problem

# Data Structures
# A list should be sufficient

# Algorithms
# -0. Initialize empty list
# -1. Ask user for 1st number
# -2. Store in list
# -3. Repeat steps 1 and 2 4 more times
# -4. Ask for last number
# -5. Store last number in a variable
# -6. If last number is in list, print 1 sentence. Else, print the other

# Code

tracking_list = []

number = input('Enter the 1st number: ')
tracking_list.append(number)

number2 = input('Enter the 2nd number: ')
tracking_list.append(number2)

number3 = input('Enter the 3rd number: ')
tracking_list.append(number3)

number4 = input('Enter the 4th number: ')
tracking_list.append(number4)

number5 = input('Enter the 5th number: ')
tracking_list.append(number5)

last_num = input('Enter the last number: ')

if last_num in tracking_list:
    print(f"{last_num} is in {','.join(tracking_list)}.")

else:
    print(f"{last_num} isn't in {','.join(tracking_list)}.")