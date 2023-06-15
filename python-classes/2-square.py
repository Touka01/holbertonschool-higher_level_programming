#!/usr/bin/python3
"""Class Definition"""


class Square:
    """A class representing a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, __size): Initializes a Square object.
    """

    def __init__(self, size=0):

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
