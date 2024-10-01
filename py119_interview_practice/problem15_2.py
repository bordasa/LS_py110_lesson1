#Problem Overview
    #input: string argument all number digits
    #output: greatest product of 4 consecutive digits
        #Rules: Arg will always have more than 4 digits

#Examples:

#Data Structure: variable and tracking max product

#Algorithm:
    #1. Create helper function: string 4 digits to product of digits
    #2. Start at index 4 and iterate to end of string range(len(string))
    #3. Substring = string slice index - 4 : index
    #4. get product of substring
        #4. if product is greater than saved product, save new product
            #and save the substring
    #5. Return saved substring and product

#Code
def string_product(string):
    result = 1

    for char in string:
        result *= int(char)
    
    return result

def greatest_product(string):
    max_string_product = 0

    for index in range(4, len(string) + 1):
        substring = string[index - 4 : index]
        current_string_product = string_product(substring)

        if current_string_product > max_string_product:
            max_string_product = current_string_product
    
    return max_string_product

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6