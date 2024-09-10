# def triangle(angle1, angle2, angle3):
#     angles_list = [angle1, angle2, angle3]

#     if 0 in angles_list or sum(angles_list) != 180:
#         return 'invalid'
#     elif 90 in angles_list:
#         return 'right'
#     elif [angle for angle in angles_list if angle > 90]:
#         return 'obtuse'
#     else:
#         return 'acute'

def triangle(angle1, angle2, angle3):
    angles_list = [angle1, angle2, angle3]

    if 0 in angles_list or sum(angles_list) != 180:
        return 'invalid'
    elif 90 in angles_list:
        return 'right'
    elif any([angle > 90 for angle in angles_list]):
        return 'obtuse'
    else:
        return 'acute'

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True