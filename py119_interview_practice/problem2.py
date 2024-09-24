#Problem Overview:
    #Input: a list of integers
    #Output: 1 number: the minimum sum of 5 consecutive numbers in the list
    #rules:
        #If the list has fewer than 5 elements, return None

#Examples

#Data Structures: A list to hold potential solutions

#Algorithm:
    #1. Check if the list is long enough. If len < 5, return None
    #2. Create 2 pointers. L at 0, right at index 4 (5 elements)
    #3. Get the sum of this slice, add to tracking list
    #4. While Right pointer < len(list), Add 1 to both pointers
    #5. Repeat 3 and 4 until you reach the end of the list
    #6. return minimum of the tracking list

#Code

def minimum_sum(lst):
    if len(lst) < 5:
        return None
    
    left = 0
    right = 4
    tracking_list = []

    while right < len(lst):
        tracking_list.append(sum(lst[left:right + 1]))
        left += 1
        right += 1
    
    return min(tracking_list)

print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)