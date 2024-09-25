#Problem Overview
    #input: list of int
    #Output: the integer that appears an odd number of times
        #Rules: there will always be exactly one such integer

#Examples:

#Data Struct: Dictionary

#Algorithm:
    #1. Make a count dict for the list
    #2. Iterate through values, find the odd number. Return the key

#Code
def create_count_dict(list):
    count_dict = {}

    for num in list:
        count_dict.setdefault(num, 0)
        count_dict[num] += 1
    
    return count_dict

def odd_fellow(lst):
    count_dict = create_count_dict(lst)

    for num, count in count_dict.items():
        if count % 2 != 0:
            return num

print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)