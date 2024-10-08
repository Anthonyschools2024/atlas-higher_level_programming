#!/usr/bin/python3
"""Python code that prints a string with first and last name variables"""


def say_my_name(first_name, last_name=""):
    """initialize function say_my_name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
