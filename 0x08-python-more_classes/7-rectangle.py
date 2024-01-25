#!/usr/bin/python3
'''This file defines a Rectangle class'''


class Rectangle:
    '''Represents a Rectangle class'''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''initializes new Rectangle'''
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        '''set the width of the Rectangle'''
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
    def height(self):
        '''set the height of the Rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ('')

        rectang = []
        for j in range(self.__height):
            [rectang.append('#') for j in range(self.__width)]
            if j != self.__height - 1:
                rectang.append('\n')
        return (''.join(rectang))

    def __repr__(self):
        rectang = "Rectangle(" + str(self.__width)
        rectang += ", " + str(self.__height) + ")"
        return (rectang)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
