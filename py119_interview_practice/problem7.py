#Problem Overview:
    #Input: A list of integers
    #Output: the number of identical pairs of integers in the list
        #Rules:
            #If the list is empty or len() = 1, return 0
            #If a number occurs more than once, count only complete pairs

#Examples

#Data Structures: Dict to hold the counts, couple of variables, list?

#Algorithm
    #1. Iterate through list
    #2. Count number of occurrances of each integer in list. Add to dict
    #3. Iterate through dict, checking for // 2 (equal pairs)
    #4. Add up the values in the list after // 2
    #5 Return sum

#code

def pairs(lst):
    if len(lst) < 2:
        return 0
    
    tracking_dict = {}

    for num in lst:
        tracking_dict.setdefault(num, 0)
        tracking_dict[num] += 1
    
    pairs_list = [num // 2 for num in tracking_dict.values()]

    return sum(pairs_list)

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)