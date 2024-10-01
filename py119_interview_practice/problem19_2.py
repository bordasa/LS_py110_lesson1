#Problem Overview:
    #Input: list of int
    #output: the integer that appears an odd number of times
    #Rules: There will always be exactly 1 answer

#Examples:

#Data Structures: Dictionary

#Algorithm:
    #1. Create count dict for each element
    #2. Check count dict for value %2 == 1. Return that key

#Code

def create_count_dict(list):
    count_dict = {}

    for element in list:
        count_dict.setdefault(element, 0)
        count_dict[element] += 1
    
    return count_dict

def odd_fellow(lst):
    count_dict = create_count_dict(lst)

    for num, count in count_dict.items():
        if count % 2 == 1:
            return num

print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)