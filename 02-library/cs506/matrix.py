def get_determinant(matrix):
    row, col = matrix.shape
    if(row == 1 and col == 1):
        return matrix[0][0]
    else:
        for i in range(col):
            #remove the column 
            cnum=matrix[0][i]
            newmatrix = matrix.drop(matrix.columns[i] , axis=1)
            newmatrix = newmatrix.iloc[1: , :]
            return ((-1)**cnum)*cnum*get_determinant(newmatrix)
 