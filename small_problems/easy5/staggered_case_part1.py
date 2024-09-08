# def staggered_case(string):
#     index = 0
#     new_string = ''

#     while index < len(string):
#         if index % 2 == 0:
#             new_string += string[index].upper()
#         else:
#             new_string += string[index].casefold()
        
#         index += 1
    
#     return new_string

def staggered_case(string):
    new_string = ''

    for idx, char in enumerate(string):
        if idx % 2 == 0:
            new_string += char.upper()
        else:
            new_string += char.casefold()
        
    return new_string

string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True