#Problem Overview
    #Input: integer
    #Output: sum of all numbers less than Input that are multiples of 7/11
        #Rules: if input is negative, return 0
            # if input is mult of 7 and 11, only count it once

#Examples:

#Data Structure: list

#Algorithm:
    #1. Check if arg is less than 7. If yes, return 0
    #2. Iterate in range(7, num)
    #3. Check if each num is evenly divided by 7 or 11
        #4. If yes, add to list.
    #5. return sum(list)

#Code
def seven_eleven(input_num):
    if input_num <= 7:
        return 0
    
    tracking_list = []

    for num in range(7, input_num):
        if num % 7 == 0 or num % 11 == 0:
            tracking_list.append(num)
    
    return sum(tracking_list)

print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)