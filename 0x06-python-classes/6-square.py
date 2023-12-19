#!/usr/bin/python3
''' class Square that defines a square by:
(based on 5-square.py)'''


class Square:
    '''The Square class'''
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(numb, int) for numb in value) or
                not all(numb >= 0 for numb in value)):
            print("position must be a tuple of 2 positive integers", end='')
            raise TypeError
        self.__position = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for j in range(0, self.__size):
            [print(" ", end="") for k in range(0, self.__position[0])]
            [print("#", end="") for i in range(0, self.__size)]
            print("")
