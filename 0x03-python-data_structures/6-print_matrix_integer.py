#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if y == len(matrix[x]) - 1:
                print("{}".format(matrix[x][y]))
            else:
                print("{} ".format(matrix[x][y]), end="")
