#!/usr/bin/python3
"""class Base"""
from json import dumps, loads

class Base:
    """Base class for managing id and JSON serialization"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of the Base instance
        
        Args:
            id (int): Unique identifier for the instance (default=None)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries
        
        Args:
            list_dictionaries (list): List of dictionaries to convert to JSON string
            
        Returns:
            str: JSON string representation of list_dictionaries or "[]"
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string
        
        Args:
            json_string (str): A string representing a list of dictionaries
            
        Returns:
            list: List represented by json_string or an empty list
        """
        if json_string is None or json_string == "":
            return []
        else:
            return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file
        
        Args:
            list_objs (list): List of instances to serialize to JSON and save to a file
        """
        filename = f"{cls.__name__}.json"  # File name based on class name
        if list_objs is None:
            list_objs = []
        
        # Convert list of objects to a list of dictionaries
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(list_dictionaries))

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with all attributes already set
        
        Args:
            **dictionary: Attributes to set for the instance
            
        Returns:
            Instance of the class with attributes set
        """
        # Create a dummy instance
        if cls.__name__ == "Rectangle":
            dummy = Rectangle(1, 1)  # Assuming dummy values for width and height
        elif cls.__name__ == "Square":
            dummy = Square(1)  # Assuming a dummy value for size
        else:
            raise ValueError("Unknown class")

        # Use the update method to set the actual values from dictionary
        dummy.update(**dictionary)
        return dummy

# Assuming Rectangle and Square classes are defined elsewhere with the required methods
