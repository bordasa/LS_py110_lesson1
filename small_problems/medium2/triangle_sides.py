#Problem Overview
    #Input: 3 numbers (sides of a triangle)
    #Output: string
    #Rules: Only 4 outputs: equi, isosc, scal, invalid
        #sum of the 2 shorter sides > longest side
        #all sides > 0
        #else: invalid
        #Equi - all sides are the same
        #isosceles - 2 sides are the same
        #scalene - all different
        #Sides can be floats

#Algo
    #0. Check that no numbers are Zero, else return invalid
    #1. Find max of the inputs
    #2. Test that max < sum(other sides), else return invalid
    #3. Check to how many sides are the same

def triangle(side1, side2, side3):
    sides_list = sorted([side1, side2, side3], reverse = True)
    
    if 0 in sides_list or sides_list[0] > sum(sides_list[1:]):
        return 'invalid'
    
    sides_set = set(sides_list)

    match len(sides_set):
        case 1:
            return 'equilateral'
        case 2:
            return 'isosceles'
        case 3:
            return 'scalene'


print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True