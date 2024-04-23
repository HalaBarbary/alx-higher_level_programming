#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        if lst < len(matrix):
            for item in lst:
                if item < len(lst):
                    print("{:d}".format(matrix[lst[item]]), end=" ")
