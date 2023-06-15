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
        self.size = size

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
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size**2

    def my_print(self):
        """Prints a square pattern based on the size attribute.
            If the size is 0, it prints an empty line.
            Otherwise, it prints a square pattern
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)
