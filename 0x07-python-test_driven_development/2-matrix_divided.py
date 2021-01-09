#!/usr/bin/python3
"""Documentation for a function that divides
elements from a matrix by a number
"""


def matrix_divided(matrix, div):
    """[summary]

    Args:
        matrix (list): [description]
        div (int or float): [description]

    Raises:
        TypeError: [description]
        ZeroDivisionError: [description]
        TypeError: [description]
        TypeError: [description]

    Returns:
        [type]: [description]
    """
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists)\
        of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if len(matrix) != len(matrix[0]):
        raise TypeError("Each row of the matrix must have the same size")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")
            matrix[i][j] = round(matrix[i][j] / div, 2)
    return matrix
