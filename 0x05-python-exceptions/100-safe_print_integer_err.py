#!/usr/bin/python3
'''function that prints an integer'''


def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return (True)
    except Exception as identifier:
        print("Exception: {}".format(identifier), file=sys.stderr)
        return (False)
