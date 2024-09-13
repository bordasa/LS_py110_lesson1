def factor_x_sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(factor_x_sum(numbers, 2) == 20)

'''
In python, certain variable names are reserved for functions and methods
already built into the language. Sum is one of those reserved names.
In order to fix this code, we need to change the name of the custom
 function.
'''