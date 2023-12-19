#!/usr/bin/python3
'''class Square that defines a square by:
(based on 4-square.py)'''



class Square:
    '''The Square class'''
    def __init__(self, size=0):
        if type(size) != int:
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        self.__size = size

    def area(self):
        '''return the area of the square'''
        return (self.__size * self.__size)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                print("size must be >= 0", end='')
                raise ValueError
            else:
                print("size must be an integer", end='')
                raise TypeError
            else:
                self.__size = value

    def my_print(self):
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
