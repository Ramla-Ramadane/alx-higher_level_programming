#!/usr/bin/python3
'''class Square that defines a square by:
(based on 3-square.py)'''


class Square:
    '''The square class'''
    def __init__(self, size=0):
        if type(size) != int:
            print("size must be an integer", end='')
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end='')
            raise ValueError
        self.__size = size

        def area(self):
            'Return area of the square'
            return (self._size * self._size)

        @property
        def size(self):
            return (self.__size)

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                print("size must be an integer", end='')
                raise TypeError
            elif value < 0:
                print("size must be >= 0", end='')
                raise ValueError
            self.__size = value
