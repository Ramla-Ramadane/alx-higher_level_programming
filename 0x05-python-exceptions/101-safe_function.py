#!/usr/bin/python3
'''function that executes a function safely'''


import sys


def safe_function(fct, *args):
    try:
        return (fct(*args))
    except Exception as identifier:
        print("Exception: {}".format(identifier), file=sys.stderr)
        return None
