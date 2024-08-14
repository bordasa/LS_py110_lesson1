#Problem
    #Input: a list of integers
    #Output: return the average of all of the integers in the list
    #Rules:
        #- Output rounds down to the integer component
        #- List will never be empty
        #- Numbers will always be positive integers

#Examples

#Data Structure: 

#Algorithm
    #Compute the average of the list
    #Convert the result to an integer
    #Output the result

#Code

# def average(list):
#     sum = 0

#     for num in list:
#         sum += num
    
#     ave = sum / len(list)
    
#     return int(ave)

def average(list):
    total = sum(list)

    return total // len(list)

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                    # True      