#!/usr/bin/python3
def no_c(my_string):
    no_c = "cC"
    for letter in my_string:
        if letter not in no_c:
            modified_str += letter
    return (modified_str)
