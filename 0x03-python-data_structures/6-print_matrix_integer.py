#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in (len(matrix)-1):
        for item in matrix[list]:
            print("{:d}".format(matrix[list[item]]), end=" ")
