#Input: 2 integers, count and starting number
# Output: a list with the count # of elements, all multiples of the start number
# Rules: starting number can be any integer. if count is 0, set should be empty

#Example


#Algorithm
    #1. Take start number
    #2. Loop for count # of times
    #3. Add the start number in each loop and save it to a list

#Code

def sequence(count, start_value):
    multiples = []

    for num in range(1, count + 1):
        multiples.append(start_value * num)
    
    return multiples



print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True