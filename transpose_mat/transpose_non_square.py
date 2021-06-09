''' 
Given a 2D array A, convert all rows to columns and columns to rows for any sized matrix. 

'''


def transpose_non_square(mat):

    if not mat:
        print("Empty matrix")   
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))] 