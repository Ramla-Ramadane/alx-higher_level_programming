#!/usr/bin/python3
'''function that prints an integer'''


import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (true)
    except Exception as identifier:
        print("Exception: {}".format(identifier), file=sys.stderr)
        return (false)
