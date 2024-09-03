def rotate_rightmost_digits(number, count):
    number_string = str(number)
    right_side = number_string[len(number_string) - count :]
    left_side = number_string[: len(number_string) - count]

    right_side_rotated = right_side[1:] + right_side[0]

    num_string_rotated = left_side + right_side_rotated

    return int(num_string_rotated)

def max_rotation(number):
    index = 0
    num_length = len(str(number))
    new_num = number

    while index < num_length:
        new_num = rotate_rightmost_digits(new_num, (num_length - index))
        index += 1

    return new_num

print(max_rotation(735291) == 321579)
print(max_rotation(3) == 3)
print(max_rotation(35) == 53)
print(max_rotation(8703529146) == 7321609845)
print(max_rotation(105) == 15)