#Input: a string of a first name, a space, and a last name
#Output: a new string of last name, a comma, a space, and a 1st name
#Rules: -No middle names, initials, or suffixes

#Example


#Algorithm:
    #1. split the string
    #2 Return a reorganized f string

def swap_name(string):
    name_list = string.split()
    first_and_middle = ' '.join(name_list[:-1])

    return f"{name_list[-1]}, {first_and_middle}"


print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True