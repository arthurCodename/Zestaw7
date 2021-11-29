import math

class Point:
#     """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x ,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return '(' + str(self.x) +', '+str(self.y)+')'

    def __repr__(self):
        return 'Point('+str(self.x)+', '+str(self.y)+')'

    def __eq__(self, other: object):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: object):
        return not self.x == other.x or self.y == other.y

    def __add__(self, other: object):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: object):
        return Point(other.x - self.x, other.y - self.y)
    
    def __mul__(self, other: object):
        return self.x * other.x + self.y * other.y

    def __cross__(self, other: object): 
        return abs(self.x * other.y - self.y * other.x)

    def length(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def __hash__(self): 
        return hash(self.x, self.y)