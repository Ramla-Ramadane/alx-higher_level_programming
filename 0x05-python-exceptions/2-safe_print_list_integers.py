#!/usr/bin/python3
''' function that prints the first x elements
of a list and only integers'''


def safe_print_list_integers(my_list=[], x=0):
    ret_int = 0
    for num in range(0, x):
        try:
            print("{:d}".format(my_list[num]), end="")
            ret_int += 1
        except (TypeError, ValueError):
            continue
    print("")
    return (ret_int)
