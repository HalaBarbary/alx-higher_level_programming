#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        for item in lst:
            if item == lst[-1]:
                print("{:d}".format(item), end="")
            else:
                print("{:d}".format(item), end=" ")
        print()
