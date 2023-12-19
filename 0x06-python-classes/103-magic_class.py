#!/usr/bin/python3
class MagicClass:
    import math
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) != int and type(radius) is not float:
            print("radius must be a number", end='')
            raise TypeError
        else:
            self.__radius = radius

    def area(self):
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        return (2 * math.pi * self.__radius)
