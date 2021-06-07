''' 
Given a 2D array A, convert all rows to columns and columns to rows for a square matrix. 

'''


def transpose_square(mat):

    if not mat:
        print("Empty matrix")

    for i in range(len(mat)):
        for j in range(len(mat[0])): 
            mat[i][j], mat[j][i]  = mat[j][i], mat[i][j]    
    return mat