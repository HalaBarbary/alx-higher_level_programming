#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if 97 <= ord(letter) <= 122:
            up_str = chr(ord(letter)-32)
        else:
            up_str = chr(ord(letter))
        print("{:s}".format(up_str), end='')
    print("\n")
