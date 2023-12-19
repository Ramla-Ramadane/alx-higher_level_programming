#!/usr/bin/python3
'''class Square that defines a square by:
(based on 2-square.py)'''


class Square:
    '''The Square class'''
    def __init__(self, size=0):
        if type(size) != int:
            print("size must be an integer", end='')
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end='')
            raise ValueError
        self.__size = size

    def area(self):
        '''Return area of the square'''
        return (self.__size * self.__size)
