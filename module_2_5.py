def get_matrix(n,m,value) :
    matrix = []
    matrix_2 = []
    for i in range (n) :
        matrix.append(matrix_2)
    for j in range (m) :
        matrix_2.append(value)
    return matrix
result_1 = get_matrix(3, 4, 5)
result_2 = get_matrix(4, 3, 2)
result_3 = get_matrix(5, 1, 3)
print (result_1)
print (result_2)
print (result_3)
