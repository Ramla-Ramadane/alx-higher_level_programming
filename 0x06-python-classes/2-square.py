#!/usr/bin/python3
'''class Square that defines a square by:
(based on 1-square.py)'''


class Square:
    '''The class square'''
    def __int__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer", end='')
        elif size < 0:
            print("size must be >= 0", end='')
            raise ValueError
        self._size = size