#!/usr/bin/python3
'''This file defines a Rectangle class'''


class Rectangle():
    '''The Rectangle class'''
    def __init__(self, width=0, height=0):
        '''Initiliaze new Rectangle'''
        self.width = width
        self.height = height

    @property
    '''set the width of the rectangle'''
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    '''set the height of the rectangle'''
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
