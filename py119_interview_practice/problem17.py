#Problem Overview
    #Input: a list of integers
    #Output: min integer value that can be appened to list so
    #  sum = next prime
        #Rules:
            #All values in list > 0
            #list will always have at least 2 int
            #numbers can occur multiple times in the list

#Example:

#Data Structures: Lists

#Algorithm:
    #1. Get current sum of list
    #2. Find next prime
    #3. Subtract current sum from next prime
    #4. Add this new number to the end of the list

#Code
import math

def is_prime(num):
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            return False
    return True


def get_next_prime(num):
    new_num = num + 1

    while not is_prime(new_num):
        new_num += 1
    
    return new_num

def nearest_prime_sum(integer_list):
    current_sum = sum(integer_list)

    return (get_next_prime(current_sum) - current_sum)

print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)