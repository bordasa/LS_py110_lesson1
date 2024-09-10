#Problem Overview:
    #Input: a list of lists
    #Output: a new list of lists
    #Rules: do not modify the original list
        # Swap the rows for the columns

#Examples

#Data Structures: Nested Lists

#Algorithm:
    #1. Iterate through each nested list
    #2. Take the first element of each list and add to new list
    #3. Add new list to a result list
    #4. repeat for 2nd element

def transpose(matrix):
    new_matrix = []
    
    for col in range(len(matrix[0])):
        new_row = [row[col] for row in matrix]
        new_matrix.append(new_row)
    
    return new_matrix


matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True