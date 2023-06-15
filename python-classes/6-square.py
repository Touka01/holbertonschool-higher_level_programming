#!/usr/bin/python3
""" Class Definition"""


class Square:
    """Class representing a square object.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.

    Methods:
        __init__(self, size=0, position=(0, 0)): Initializes objects.
        area(self): Calculates and returns the area of the square.
        my_print(self): Prints a representation of the square.

    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square object with the given size and position.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square.

        Raises:
            TypeError: If size is not an integer
                       or position is not a tuple of 2 .
            ValueError: If size is less than 0.

        Attributes:
            __size (int): The size of the square.
            __position (tuple): The position of the square.

        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.
        Args:
            value (int): The size of the square.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square.
        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.
        Args:
            value (tuple): The position of the square.
        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Calculate the area of the square.
        Returns:
            int: The area of the square.

        """
        return self.__size**2

    def my_print(self):
        """Print a representation of the square.

        If the size is 0, it prints an empty line.
        Else, it prints a representation of the square using the "#" character,
        adjusting the positioning based on the position attribute.

        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
