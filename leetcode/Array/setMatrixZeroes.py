# https://leetcode.com/problems/set-matrix-zeroes/ 

#brute force solution time complexity = n^3

matrix = [
            [1,1,1],
            [1,0,1],
            [1,1,1]
]

matrix2 = [
            [0,1,2,0],
            [3,4,5,2],
            [1,3,1,5]]

def set_row_to_minus_one(i,j,matrix):
    for x in range(len(matrix)):
        if matrix[x][j] != 0:
            matrix[x][j] = -1
    return matrix

def set_column_to_minus_one(i,j,matrix):
    for y in range(len(matrix[0])):
        if matrix[i][y] != 0:
            matrix[i][y] = -1
    return matrix

def set_matrix_zeroes(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                set_row_to_minus_one(i,j,matrix)
                set_column_to_minus_one(i,j,matrix)

    #updating -1 to 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    print(matrix)
    return


# set_matrix_zeroes(matrix)
# set_matrix_zeroes(matrix2)

#Better Solution Time complexity n^2

def set_matrix_to_zeroes(matrix):
    row = []
    col = []

    #creating array for tracking row and col which needs to be set to zero
    for i in range(len(matrix)):
        row.append(0) 
    for i in range(len(matrix[0])):
        col.append(0)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1

    #mark zeros
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if row[i] == 1 or col[j] == 1:
                matrix[i][j] = 0
    
    print(matrix)
    return


#uncomment below to test
# set_matrix_to_zeroes(matrix)
# set_matrix_to_zeroes(matrix2)