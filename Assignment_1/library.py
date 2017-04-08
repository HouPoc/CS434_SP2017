#!/usr/bin/python

from itertools import product

def read_data (file_name):
    data_set = []
    data_file = open (file_name,'rb')
    for line in data_file:
        data_set.append(list(map(float,line.split())))
    Y_data = [row.pop() for row in data_set]
    return [data_set, Y_data] 
    
def matrix_invert (matrix):
    dimention = len(matrix)
    inverse_matrix = [[0. for col in range(dimention)] for row in range(dimention)]

    for i in xrange(dimention):
        inverse_matrix[i][i] = 1.

    for i in xrange(dimention):
        for j in xrange(dimention):
            if i != j:
                if matrix[i][i] == 0:
                    return False
                ratio = matrix[j][i] / matrix[i][i]
                for k in range(dimention):
                    inverse_matrix[j][k] = inverse_matrix[j][k] - ratio * inverse_matrix[i][k]
                    matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]

    for i in xrange(dimention):
        a = matrix[i][i]
        for j in range(dimention):
            inverse_matrix[i][j] = inverse_matrix[i][j] / a

    return inverse_matrix    
    
def matrix_multiplication(matrix_left, matrix_right):
    rows = len(matrix_right)
    if rows is 0:
        return 0
    cols = len(matrix_right[0])
    resRows = range(len(matrix_left))
    rMatrix = [[0] * cols for _ in resRows]

    for idx in resRows:
        for j, k in product(range(cols), range(rows)):
            rMatrix[idx][j] += matrix_left[idx][k] * matrix_right[k][j]
    return rMatrix