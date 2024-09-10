import sys



def find_fibonacci_index_by_length(num):
    sys.set_int_max_str_digits(50_000)

    if num == 1:
        return 1
    
    index = 2
    length = 1

    previous, current = 1, 1
    
    while length < num:
        previous, current = current, previous + current

        length = len(str(current))

        index += 1
            
    
    return index


# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# # Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)