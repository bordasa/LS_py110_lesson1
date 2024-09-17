#Algorithm:
    #1. Create look up dictionary for num to str for individuual digits
    #2. Get input number
    #3. Use divmod to divide by 10 and get the remainder at once as tuple
    #4. divmod[0] is the number without the right most digit.
    #5. divmod[1] is the rightmost digit
    #6. look up the divmod[1] in dictionary. Add it to the front of result
    #7. Repeat 3-6 on divmod[0] until nothing is left
    #8. Return the result

def integer_to_string(num):
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    new_num, rightmost = divmod(num, 10)
    result = DIGITS[rightmost]

    while new_num > 0:
        new_num, rightmost = divmod(new_num, 10)
        result = DIGITS[rightmost] + result
    
    return result

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True