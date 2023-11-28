#!/usr/bin/python3
'''Print all the letters except q and e'''

for alphabet in range(97, 123):
    if chr(alphabet) != 'q' and chr(alphabet) != 'e':
        print("{}".format(chr(alphabet)), end="")
