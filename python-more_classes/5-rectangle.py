#!/usr/bin/python3
"""rectangle class"""


class Rectangle:
    """class creation"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """area module that returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """prints the rectangle based on size and position"""
        if self.width == 0 or self.height == 0:
            print()
        else:
            return "\n".join(["#"*self.__width for _ in range(self.__height)])

    def __repr__(self):
        """repr"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """deletes the rectangle"""
        print("Bye rectangle...")
