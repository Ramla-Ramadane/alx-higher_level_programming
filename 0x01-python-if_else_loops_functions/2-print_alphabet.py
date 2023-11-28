#!/usr/bin/python3
'''program that prints the ASCII alphabet, in lowercase'''

i = range(97, 123)
for alphabet in i:
    print("{}".format(chr(alphabet)), end="")
