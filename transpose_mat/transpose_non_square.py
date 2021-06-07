''' 
Given a 2D array A, convert all rows to columns and columns to rows for any sized matrix. 

'''


def transpose_non_square(mat):

    if not mat:
        print("Empty matrix")   
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

if __name__ == "__main__": 
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    print(transpose_non_square(mat))