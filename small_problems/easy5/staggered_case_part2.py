# def staggered_case(string):
#     new_string = ''
#     flip_index = 0

#     for char in string:
#         if char.isalpha():

#             if flip_index % 2 == 0:
#                 new_string += char.upper()

#             else:
#                 new_string += char.casefold()

#             flip_index += 1
#         else:
#             new_string += char

#     return new_string

def staggered_case(string):
    new_string = ''
    capitalize = True

    for char in string:
        if char.isalpha():
            new_string += char.upper() if capitalize else char.lower()
            capitalize = not capitalize

        else:
            new_string += char
    
    return new_string

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True