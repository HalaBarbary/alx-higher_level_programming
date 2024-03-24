#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        up_str = up_str + chr(ord(letter)-32)
    print("{}".format(up_str))
