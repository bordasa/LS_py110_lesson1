## Problem ----------
## Input: list of numbers
## Output: list of numbers that are a running total of the input
## Rules
## Explicit:
##  -input list len = output list len
##  -each element is the sum of the previous elements
## Implicit:
#   -only need to worry about proper inputs (list and numbers only) 

## Examples ---------


## Data Structures --------> still a list

## Algorithm -----------
#   -set empty sum variable
#   -set empty list
#   -iterate through given list
#   -add each element to the sum 1 by 1
#   -in each loop, add the sum to the empty list
#   - output the list

## Code -----------------

def running_total(list):
    total = 0
    running_total_list = []

    for num in list:
        total += num
        running_total_list.append(total)
    
    return running_total_list


print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True