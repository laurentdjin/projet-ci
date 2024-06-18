"""!
@file geometry.py
@brief This module provides basic arithmetic operations.
"""

import math

def circle_area(radius):
    """!
    Calculate the area of a circle.

    @Parameters:
    @radius : The radius of the circle.

    @Returns:
    @The area of the circle.
    """
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")
    
    return math.pi * radius ** 2

def rectangle_area(width, height):
    """!
    Calculate the area of a rectangle.

    @Parameters:
    @width : The width of the rectangle.
    @height : The height of the rectangle.

    @Returns:
    @The area of the rectangle.
    """
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive numbers.")
    
    return width * height

def rectangle_perimeter(length, width):
    """!
    Calculate the perimeter of a rectangle.

    @Parameters:
    @length : The length of the rectangle.
    @width : The width of the rectangle.

    @Returns:
    @float: The perimeter of the rectangle.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    
    return 2 * (length + width)

def circle_circumference(radius):
    """!
    Calculate the circumference of a circle.

    @Parameters:
    @radius : The radius of the circle.

    @Returns:
    @The circumference of the circle.
    """
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")
    
    return 2 * math.pi * radius
