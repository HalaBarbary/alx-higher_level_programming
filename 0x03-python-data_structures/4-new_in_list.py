#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (len(my_list)-1) < idx < 0:
        list = my_list.copy()
    else:
        list = my_list.copy()
        list[idx] = element
    return(list)
