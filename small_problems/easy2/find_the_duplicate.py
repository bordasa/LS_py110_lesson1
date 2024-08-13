#Problem
    #input: unordered list
    #output: the 1 duplicate value
    #Rules:
        #Input list only has 1 value that occurs twice
        #List can be any size
        #List cannot be empty

#Examples:

#Data Structures:

#Algorithm:
    #Pop the last item from the list
    #check to see if that item is still in the list
    #if yes, return that number. Else: repeat

def find_dup(list):
    test_list = list
    test_num = test_list.pop()

    while test_num not in test_list:
        test_num = test_list.pop()
    
    return test_num



print(find_dup([1, 5, 3, 1]) == 1) # True
print(find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True
