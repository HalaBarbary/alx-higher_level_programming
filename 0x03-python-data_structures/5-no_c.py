#!/usr/bin/python3
def no_c(my_string):
    for letter in my_string:
        if letter == "c":
            my_string[letter].replace("c", "")
        elif letter == "C":
            my_string[letter].replace("C", "")
    return (my_string)
