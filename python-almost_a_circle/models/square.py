#!/usr/bin/python3

"""class Square that inherits from Rectangle"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize Square instance
        
        Args:
            size (int): Size of the square (width and height)
            x (int): X-coordinate of the square (default=0)
            y (int): Y-coordinate of the square (default=0)
            id (int): Unique identifier for the square (default=None)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return the size of the square"""
        return self.width  # or self.height, both are the same

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        self.width = value  # This also sets height due to inheritance
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes of the square"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]  # This uses the size setter
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            # Update attributes using kwargs
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value  # This uses the size setter
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def __str__(self):
        """Return string representation of the square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
