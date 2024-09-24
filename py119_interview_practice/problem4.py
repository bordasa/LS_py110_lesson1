#Problem Overview:
    #Input: a list of integers
    #Output: a tuple of two numbers that are closest in value
        #Rules:
            #If multiple pairs are equally close, return the 1st to occur

#Examples

#Data Structures: Tuple for the return, variables to keep track

#Algorithm:
    #Initialize a difference set at 0
    #Start with pointer 1 at index 0
    #Start with pointer 2 at index[pointer1 + 1]
    #Use pointer 2 to iterate through the list
    #Take the difference between value at pointer 1 and pointer2 (abs val)
    #If difference is lower than current difference, save the values p1 p2
    #When pointer 1 reachest len(list) - 2, we have check them all

#Code
def closest_numbers(lst):
    difference = abs(lst[0] - lst[1])
    result = (lst[0], lst[1])

    index = 0
    
    while index < len(lst) - 1:
        for num in lst[index + 1:]:
            if abs(lst[index] - num) < difference:
                difference = abs(lst[index] - num)
                result = (lst[index], num)
        index += 1
    
    return result

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))