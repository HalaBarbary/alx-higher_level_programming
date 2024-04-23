#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in (len(matrix)-1):
        for item in matrix[lst]:
            print("{:d}".format(matrix[lst[item]]), end=" ")
