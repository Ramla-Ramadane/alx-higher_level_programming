#!/usr/bin/python3
'''class Square that defines a square by:
(based on 1-square.py)'''


class Square():
    '''The class square'''
    def __int__(self, size=0):
        if type(size) != int:
            print("size must be an integer", end='')
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end='')
            raise ValueError
        self.__size = size
