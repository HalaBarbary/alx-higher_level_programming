#!/usr/bin/python3
def print_last_digit(number):
    if number != 0:
        print("{:d}".format(abs(number) % 10))
    else:
        print(number)
