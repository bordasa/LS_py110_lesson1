#Problem Overview
    #Input: string argument of numbers
    #Output: greatest product of four consecutive digits
        #Rules: Argument will always have more than 4 digits

#Examples

#Data Structure: list for tracking

#Algorithm:
    #Start with index 0 to range len(string) - 4
    #Iterate through each index, taking slices of the string
    #For each slice of the string, add to list
    #Make new list that is the product of each digit
    #return the max of the new list

#Code
def product_of_digits(num_string):
    result = int(num_string[0])

    for digit in num_string[1:]:
        result *= int(digit)
    
    return result

def greatest_product(num_string):
    substrings = []

    for index in range(len(num_string) - 3):
        substrings.append(num_string[index: index + 4])
    
    products = [product_of_digits(substring) for substring in substrings]
    
    return max(products)

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6