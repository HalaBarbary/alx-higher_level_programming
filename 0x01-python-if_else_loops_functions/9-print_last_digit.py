#!/usr/bin/python3
def print_last_digit(number):
    l_dig = abs(number) % 10
    print(f"{l_dig}", end='')
    return l_dig
