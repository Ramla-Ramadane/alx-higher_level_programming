#!/usr/bin/python3
'''class Rectangle that inherits from BaseGeometry'''


class Rectangle(BaseGeometry):
    '''base geometry'''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
