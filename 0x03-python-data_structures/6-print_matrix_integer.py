#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and len(matrix[0]) == 0:
        print("".format())
        return
    for x in range(len(matrix)):
        if len(matrix[x]) == 0:
            print("".format())
        for y in range(len(matrix[x])):
            if y == len(matrix[x]) - 1:
                print("{}".format(matrix[x][y]))
            else:
                print("{} ".format(matrix[x][y]), end="")
