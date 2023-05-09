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


set_matrix_zeroes(matrix)
set_matrix_zeroes(matrix2)



#Better Solution Time complexity



