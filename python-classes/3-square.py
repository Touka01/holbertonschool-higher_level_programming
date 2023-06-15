#!/usr/bin/python3
""" Class Definition"""


class Square:
    """CLass representing a square
     Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, __size): Initializes a Square object.
    """

    def __init__(self, size=0):
        """Initialize a Square object with the given size.
        Args:
            size (int, optional): The size of the square. Defaults to 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        Attributes:
            __size (int): The size of the square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square.
         Returns:
         int: The area of the square.
         """
        return self.__size**2
