#Input: positive integer
#Output: True if number is prime, false if it is not prime
#Rules: Cannot use any Python add-ons or packages

#Algorithm:
    #1. Get input number
    #2. Iterate through all lower numbers up to 1/2 way point rounded down
    #3. If any number divides into input number with no remainder, return False
    #4. If no numbers divide in, return True

#Code:

def is_prime(number):

    if number == 1:
        return False

    half_way_point = number // 2 + 1

    for factor in range(2, half_way_point):
        if number % factor == 0:
            return False
        
    return True


# #Examples:
print(is_prime(1) == False)
print(is_prime(2) == True)
print(is_prime(3) == True)
print(is_prime(4) == False)
print(is_prime(5) == True)
print(is_prime(6) == False)
print(is_prime(7) == True)
print(is_prime(8) == False)
print(is_prime(9) == False)
print(is_prime(10) == False)
print(is_prime(23) == True)
print(is_prime(24) == False)
print(is_prime(997) == True)
print(is_prime(998) == False)
print(is_prime(3_297_061) == True)
print(is_prime(23_297_061) == False)