#!/usr/bin/python3
for i in range(8):
    for n in range((i+1), 10):
        print("{:d}{:d}, ".format(i, n), end='')
print("{:d}{:d}".format(i+1, n))
