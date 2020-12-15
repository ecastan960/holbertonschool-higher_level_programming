#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    y = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[y])):
            if y == len(matrix[y]) - 1:
                print("{}".format(matrix[x][y]), end="")
            else:
                print("{} ".format(matrix[x][y]), end="")
        print()
