#!/usr/bin/python3
'''class Rectangle that inherits from BaseGeometry'''


class Rectangle(BaseGeometry):
    """ base geometry"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
