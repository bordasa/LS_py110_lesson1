# #Pracice Problem 1

# munsters = {
#     'Herman':  {'age': 32,  'gender': 'male'},
#     'Lily':    {'age': 30,  'gender': 'female'},
#     'Grandpa': {'age': 402, 'gender': 'male'},
#     'Eddie':   {'age': 10,  'gender': 'male'},
#     'Marilyn': {'age': 23,  'gender': 'female'},
# }

# total_age = 0

# for key, value in munsters.items():
#     if value['gender'] == 'male':
#         total_age += value['age']

# print(total_age)

# total_age2 = 0

# for member_dict in munsters.values():
#     if member_dict['gender'] == 'male':
#         total_age2 += member_dict['age']

# print(total_age2)

# age_list = [info_dict['age'] for name, info_dict in munsters.items()
#                     if info_dict['gender'] == 'male']

# print(sum(age_list))

# print(sum([member_dict['age'] for member_dict in munsters.values()
#            if member_dict['gender'] == 'male']))

# #Practice Problem 2

# lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# new_lst = [sorted(inner_lst) for inner_lst in lst]
# print(new_lst)

# ## Practice Problem 3

# lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# new_lst = [sorted(inner_lst, key=str) for inner_lst in lst]
# print(new_lst)

# #Practice Problem 4
# lst = [
#     ['a', 1],
#     ['b', 'two'],
#     ['sea', {'c': 3}],
#     ['D', ['a', 'b', 'c']]
# ]

# new_dict = {sublist[0]: sublist[1] for sublist in lst}
# print(new_dict)

# Practice Problem 5
#lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]
##____________________________
# tracking_list = []

# for sublist in lst:
#     sum = 0
#     for num in sublist:
#         if num % 2 == 1:
#             sum += num
    
#     tracking_list.append([sum, sublist])

# sorted_by_sum_of_odds = sorted(tracking_list)
# final = [item[1] for item in sorted_by_sum_of_odds]
# print(final)
##_____________________________
# def sum_of_odds(list1):
#     return sum([num for num in list1 if num % 2 == 1])

# sorted_lst = sorted(lst, key = sum_of_odds)
# print(sorted_lst)

#Practice Problem 6
# lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

# def incremenet_values(my_dict):
#     return {key: value + 1 for key, value in my_dict.items()}

# new_lst = [incremenet_values(inner_dict) for inner_dict in lst]
# print(new_lst)

# #Practice Problem 7
# lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

# def extract_multiples_of_3(my_list):
#     return [num for num in my_list if num % 3 == 0]

# new_lst = [extract_multiples_of_3(sublist) for sublist in lst]
# print(new_lst)

#Practice Problem 8

# dict1 = {
#     'grape': {
#         'type': 'fruit',
#         'colors': ['red', 'green'],
#         'size': 'small',
#     },
#     'carrot': {
#         'type': 'vegetable',
#         'colors': ['orange'],
#         'size': 'medium',
#     },
#     'apricot': {
#         'type': 'fruit',
#         'colors': ['orange'],
#         'size': 'medium',
#     },
#     'marrow': {
#         'type': 'vegetable',
#         'colors': ['green'],
#         'size': 'large',
#     },
# }

# result_list = []

# for food_dict in dict1.values():
#     if food_dict['type'] == 'fruit':
#         color_list = [color.capitalize() for color in food_dict['colors']]
#         result_list.append(color_list)
#     else:
#         result_list.append(food_dict['size'].upper())

# print(result_list)

# Practice Problem 9
# lst = [
#     {'a': [1, 2, 3]},
#     {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
#     {'e': [8], 'f': [6, 10]},
# ]

# def is_all_evens(my_dict):
#     for sublist in my_dict.values():
#         for num in sublist:
#             if num % 2 == 1:
#                 return False
    
#     return True

# new_lst = [subdict for subdict in lst if is_all_evens(subdict)]
# print(new_lst)

# Practice Problem 10
import random

def uuid_part(num_chars):
    hex_chars = '0123456789abcdef'
    part = ''

    for _ in range(num_chars):
        part += random.choice(hex_chars)
    
    return part

def create_uuid():
    pattern = [8, 4, 4, 4, 12]

    uuid_parts_list = [uuid_part(num) for num in pattern]

    return '-'.join(uuid_parts_list)

print(create_uuid())

