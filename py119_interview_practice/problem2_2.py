#Problem Overview:
    #Input: list of int
    #Output: minimum sum of 5 consecutive numbers in list
    #Rules:
        # -If list has < 5 elements, return None

#Examples:

#Data Structure: list to track the sums

#Algorithm:
    #1. check if len(lst) < 5: return None
    #2. for index in range(4, len(lst)), make a list of the sum of the slice
    #3. Return min of the list

#Code
# def minimum_sum(lst):
#     if len(lst) < 5:
#         return None
    
#     sums_list = [sum(lst[index - 4: index + 1]) 
#                  for index in range(4, len(lst))]

#     return min(sums_list)

#New Algorithm:
    #1. check if len(lst) < 5: return None
    #2. min_sum = sum(lst) (something too big)
    #3. for index in range(0, len(lst) - 5):
    #4. take slice that is 5 elements long lst[index: index + 5]
    #5. get sum of the slice. if sum < min_sum, save new min_sum
    #6. return min_sum

def minimum_sum(input_list):
    if len(input_list) < 5:
        return None
    
    min_sum = sum(input_list[:5])

    for index in range(0, len(input_list) - 4):
        current_sum = sum(input_list[index : index + 5])
        
        if current_sum < min_sum:
            min_sum = current_sum
    
    return min_sum

print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)