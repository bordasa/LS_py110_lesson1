#Problem Overview:
    #Input: list of integers
    #Output: minimum int that can be added to list so sum of all elements
            #is equal to the closest prime number > current sum of list
        #Rules: -list will always have >= 2 ints
            # - all values in list must be > 0
            # - numbers can repeat

#Examples:

#Data Structure: variables and work with the list

#Algorithm:
    #Find sum of current list
    #Find next smallest prime number
    #return difference between next smallest prime and sum of current list

#Code
import math

def is_prime(num):
    for possible_factor in range(2, int(math.sqrt(num)) + 1):
        if num % possible_factor == 0:
            return False
    return True

def nearest_prime_sum(list):
    list_sum = sum(list)
    new_num = list_sum + 1

    while not is_prime(new_num):
        new_num += 1
    
    return new_num - list_sum
    
print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)