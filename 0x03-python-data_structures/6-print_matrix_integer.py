#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        for item in matrix[lst]:
            print("{:d}".format(matrix[lst[item]]), end=" ")
