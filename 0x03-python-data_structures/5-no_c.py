#!/usr/bin/python3
def no_c(my_string):
    for letter in my_string:
        if letter == "c":
            my_string[letter] = ""
        elif letter == "C":
            my_string[letter] = ""
    return (my_string)
