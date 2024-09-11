# def rotate90(matrix):
#     old_row_count = len(matrix)
#     old_col_count = len(matrix[0])

#     new_matrix = []

#     for col in range(old_col_count): # 0 , 1, 2
#         new_row = []

#         for row in range(old_row_count - 1, -1, -1): #(1, 0)
#             new_row.append(matrix[row][col])
        
#         new_matrix.append(new_row)
    
#     return new_matrix

def rotate90(matrix):
    new_matrix = []
    
    for col in range(len(matrix[0])):
        new_row = [row[col] for row in matrix]
        new_matrix.append(new_row)
    
    for row in new_matrix:
        row.reverse()

    return new_matrix

matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)