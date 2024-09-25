#!/usr/bin/python3

"""class Rectangle that inherits from Base"""

from models.base import Base

class Rectangle(Base):
    """Rectangle class"""
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize Rectangle instance
        
        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
            x (int): X-coordinate of the rectangle (default=0)
            y (int): Y-coordinate of the rectangle (default=0)
            id (int): Unique identifier for the rectangle (default=None)
        """
        super().__init__(id)

        # Validate width
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        # Validate height
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        # Validate x
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        # Validate y
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        """Return the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """Return the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Print the rectangle using the '#' character, taking into account x and y."""
        # Print empty lines for the y-coordinate
        for _ in range(self.y):
            print()

        # Print the rectangle with spaces for the x-coordinate
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """Return string representation of the rectangle"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Update attributes of the rectangle"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            # Update attributes using kwargs
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

   