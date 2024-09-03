#input: a number and a count
#output: a new number with the last 'count' digits rotated by 1
#rules:
    #move the first of the 'count' to the end and shft the others to the left


#Algorithm:
    #convert the number to a list or string
    #take a slice of the number based on the count, starting from the right
    #rotate the first number of the slice to the end
    #re-join the list or string
    #return the new number (convert to int if needed)

#Code

def rotate_rightmost_digits(number, count):
    number_string = str(number)
    right_side = number_string[len(number_string) - count :]
    left_side = number_string[: len(number_string) - count]

    right_side_rotated = right_side[1:] + right_side[0]

    num_string_rotated = left_side + right_side_rotated

    return int(num_string_rotated)


#Examples:
print(rotate_rightmost_digits(735291, 2) == 735219)
print(rotate_rightmost_digits(735291, 3) == 735912)
print(rotate_rightmost_digits(735291, 1) == 735291)
print(rotate_rightmost_digits(735291, 4) == 732915)
print(rotate_rightmost_digits(735291, 5) == 752913)
print(rotate_rightmost_digits(735291, 6) == 352917)
print(rotate_rightmost_digits(1200, 3) == 1002)
