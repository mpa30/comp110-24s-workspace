"""Challange assigment 8"""

from __future__ import annotations
__author__: str="730671723"

class Point: 

    #  attributes  
    x:float
    y:float


    def __init__(self, x_init: float, y_init: float):
        self.x = x_init
        self.y = y_init

    
    def scale_by(self, factor: int) -> None:
        """ update x and y atributes """
        first_point: Point = Point(self.x, self.y)
        self.x *= factor
        self.y *= factor 
        first_point


    def scale(self, factor: int) -> Point:
        """Return a new point()."""
        first_point: Point = Point(self.x * factor, self.y * factor)
        return first_point

    