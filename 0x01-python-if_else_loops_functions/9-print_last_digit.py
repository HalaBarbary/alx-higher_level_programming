#!/usr/bin/python3
def print_last_digit(number):
    l_dig = abs(number % 10)
    print("{:d}".format(l_dig))
    return (l_dig)
