#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    y = 0
    if len(matrix) == 1 and len(matrix[0]) == 0:
        print()
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if y == len(matrix[x]) - 1:
                print("{}".format(matrix[x][y]))
            else:
                print("{} ".format(matrix[x][y]), end="")
