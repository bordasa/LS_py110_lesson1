def triangle(side1, side2, side3):
    sides_list = [side1, side2, side3]
    sides_list.sort()

    if 0 in sides_list or (sides_list[0] + sides_list[1] < sides_list[2]):
        return "invalid"
    
    sides_set = set(sides_list)

    match len(sides_set):
        case 1:
            return "equilateral"
        case 2:
            return "isosceles"
        case 3:
            return "scalene"
        
print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True