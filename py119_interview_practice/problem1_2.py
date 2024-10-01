#Problem Overview:
    #Input: list of nums
    #Output: lists of count of nums smaller than num in list at index
    #Rules:
        # - count only unique values

#Examples

#Data Structures: list and set

#Algorithm:
    #create a set of unique elements from input list
    #For each element in list, count number of elements in set that are <
    #Add count to results list
    #return results list

#Code
def smaller_numbers_than_current(input_list):
    result_list = []
    unique_input_nums = set(input_list)

    for input_num in input_list:
        less_than_list = [num for num in unique_input_nums
                          if num < input_num]
        result_list.append(len(less_than_list))
    
    return result_list

    # for input_num in input_list:
    #     result_list.append(len([num for num in unique_input_nums
    #                             if num < input_num ]))
    
    # return result_list

    # for input_num in input_list:
    #     count = 0
    #     for unique_num in unique_input_nums:
    #         if unique_num < input_num:
    #             count += 1
    #     result_list.append(count)
    
    # return result_list

print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)