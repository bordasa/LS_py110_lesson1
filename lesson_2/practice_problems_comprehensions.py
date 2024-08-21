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

## Practice Problem 3