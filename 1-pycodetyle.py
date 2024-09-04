#!/usr/bin/python3
"""
This module defines the `MyClass` class.
"""


class MyClass:
    """
    A class used to represent an example class.
    
    Attributes
    ----------
    attribute1 : type
        Description of attribute1.
    attribute2 : type
        Description of attribute2.

    Methods
    -------
    method1():
        Description of method1.
    method2(param1):
        Description of method2.
    """

    def __init__(self, attribute1, attribute2):
        """
        Initializes the MyClass instance.

        Parameters
        ----------
        attribute1 : type
            Description of attribute1.
        attribute2 : type
            Description of attribute2.
        """
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def method1(self):
        """
        Example method1 that performs an action.

        Returns
        -------
        type
            Description of the return value.
        """
        # Perform some action
        pass

    def method2(self, param1):
        """
        Example method2 that takes a parameter and performs an action.

        Parameters
        ----------
        param1 : type
            Description of param1.

        Returns
        -------
        type
            Description of the return value.
        """
        # Perform some action with param1
        pass


if __name__ == "__main__":
    # Example usage
    obj = MyClass(attribute1="value1", attribute2="value2")
    obj.method1()
    obj.method2(param1="example_param")
