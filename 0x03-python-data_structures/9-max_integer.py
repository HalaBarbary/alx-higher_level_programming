#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return ()
    else:
        sorted_lst = my_list.sort()
        max_v = sorted_lst[-1]
        return (max_v)
