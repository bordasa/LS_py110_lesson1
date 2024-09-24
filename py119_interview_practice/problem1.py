#problem overview
#input: a list of numbers
#output: a list of numbers
    #rules:
        #for each number, determine how many numbers in the list are smaller
        #When counting, only count unique values

#Examples

#Data Structures: A set will create unique values only. A list for output

#Algorithm
    #1. create a set from the list to get unique values
    #2. Iterate through original list
    #3. For each num in list, iterate through the set
    #4. If num in set is < num in list, add to count
    #5. Add count to the results list
    #6. repeat 3-5 until all elements are done
    #7. Potential for optimizing with a cache dict

#Code

def smaller_numbers_than_current(lst):
    unique_numbers = set(lst)
    results = []

    for list_num in lst:
        count = 0
        for set_num in unique_numbers:
            if set_num < list_num:
                count += 1
        results.append(count)
    
    return results


print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)
print(smaller_numbers_than_current([]))