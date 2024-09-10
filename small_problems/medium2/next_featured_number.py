#Problem Overview:
    #Input: number
    #Output: number > input or error message
    #Rules:
        #output must be a featured number
        #featured: output % 2 == 1
                #output % 7 == 0
                #len of set(str(output)) == len(str(output))
        #output <= 9876543201

#Examples

#Data Structures: using variables and a set

#Algorithm:
    #1. Get input number
    #2. Add 1 to input until you reach first odd mult of 7
    #3. Check if its featured (all digits unique)
    #4. If yes, return number
    #5. Else, add 14 and repeat 3 while numbers less than largest possible
    #6. Return Error if get out of while loop

#Code
def all_digits_unique(num):
    str_num = str(num)
    return len(set(str_num)) == len(str_num)


def next_featured(num):

    new_num = num + 1
    num_limit = 9876543201

    # while True:
    #     if new_num % 7 == 0 and new_num % 2 != 0:
    #         break
    #     else:
    #         new_num += 1
    
    while new_num % 7 != 0 or new_num % 2 == 0:
        new_num += 1

    while new_num <= num_limit:
        if all_digits_unique(new_num):
            return new_num
        
        new_num += 14
    
    return "There is no possible number that fulfills those requirements."
    

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True