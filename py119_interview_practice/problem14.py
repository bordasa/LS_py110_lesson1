#Problem Overview
    #Input: 1 integer
    #Output: sum of all multiples of 7 or 11 that are < Input
        #Rules:
            #If num is multiple of both 7 and 11, count it once
            #If argument is negative, return 0

#Examples:

#Data Structure: just variables

#Algorithm:
    #0. Check if input is negative. yes, return 0
    #1. Create an empty list
    #2. check each num in range(0, input)
    #3. if num % 7 == 0 or num % 11 == 0: append to list
    #4. return sum of list

#Code
def seven_eleven(input_num):
    if input_num <= 6:
        return 0
    
    multiples = [num for num in range(7, input_num)
                 if num % 7 == 0 or num % 11 == 0]

    # for n in range(7, num):
    #     if n % 7 == 0 or n % 11 == 0:
    #         multiples.append(n)

    return sum(multiples)

print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(7) == 0)
print(seven_eleven(-100) == 0)