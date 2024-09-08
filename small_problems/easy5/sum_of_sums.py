#Problem:
    #Input: a list of numbers
    #Output: sum of the sums of each leading subsequence in the list
    #rules: Assume the last contains at least one number
#Algorithm:
    #1. Get length of list
    #2. Iterate through the list
    #3. Take a slice of the list start with 1 item and building to full list
    #4. Get the sum of each list slice
    #5. Add the sums together in each iteration

#Code
def sum_of_sums(list):
    length_of_list = len(list)
    total = 0

    for idx in range(length_of_list):
        total += sum(list[:(idx + 1)])
    
    return total

print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True