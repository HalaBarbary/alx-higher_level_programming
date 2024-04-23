#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        if lst != matrix[-1]:
            for item in lst:
                if item != lst[-1]:
                    print("{:d}".format(matrix[lst[item]]), end=" ")
