def reverse_string(string):
    reversed_string = ''
    for char in string:
        reversed_string = char + reversed_string

    return reversed_string

print(reverse_string("hello") == "olleh")

'''
The main bug in this code is that the input string is being used as the
variable within the 'for' loop. As a result, the initial string is
appended to the result string along with the reversed string. A solution
to this problem is to create a new, empty string variable and use this
new string within the 'for' loop as well as in the 'return' statement.
'''