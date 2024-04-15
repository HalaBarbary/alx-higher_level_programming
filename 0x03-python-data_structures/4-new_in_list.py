#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (len(my_list)-1) < idx < 0:
        list = my_list
    else:
        my_list[idx] = element
        list = my_list
    return(list)
