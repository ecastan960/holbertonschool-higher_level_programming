#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = []
    for i in range(len(matrix)):
        a.append(list(map(lambda x: x*x, matrix[i])))
    return a
