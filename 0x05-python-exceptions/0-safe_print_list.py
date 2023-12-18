#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    for num in range(0, x):
        try:
            print("{:d}".format(my_list[num]), end="")
            printed = 0 + 1
        except Exception:
            break;
    print("")
    return (printed)
