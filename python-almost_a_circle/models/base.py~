#!/usr/bin/python3
"""class Base"""
from json import dumps

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
