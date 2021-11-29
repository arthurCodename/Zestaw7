from points import Point
import math
class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self): 
        return  "Circle({}, {}, {})".format(self.pt.x, self.pt.y, self.radius)      # "Circle(x, y, radius)"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self): 
        return math.pi * math.pow(self.radius, 2)# pole powierzchni

    def move(self, x, y):    # przesuniecie o (x, y)
        self.pt = Point(self.pt.x + x, self.pt.y + y)
        return self

    def cover(self, other):    # najmniejszy okrąg pokrywający oba
        if not isinstance(other, Circle):
            raise ValueError("Value is not instance of class Circle. Cannot be operated on")
        else:
            covering_circle = self if self.radius > other.radius else other
            center_x = (self.pt.x + other.pt.x) // 2
            center_y = (self.pt.y + other.pt.y) // 2
            equation = round(math.sqrt(pow(covering_circle.pt.x - center_x,2) + pow(covering_circle.pt.y - center_y, 2)), 2)

        covering_circle.pt = Point(center_x, center_y)
        covering_circle.radius += equation

        return covering_circle
            
# Kod testujący moduł.

import unittest

class TestFrac(unittest.TestCase):
    def test__repr__(self):
        self.assertEqual(Circle.__repr__(Circle(1,3,4)), "Circle(1, 3, 4)")

    def test__eq__(self):
        self.assertEqual(Circle.__eq__(Circle(1,3,4), Circle(1,3,4)), True)

    def test__ne__(self):
        self.assertEqual(Circle.__ne__(Circle(1,3,4), Circle(2,3,4)), True)

    def test__area__(self):
        self.assertAlmostEquals(Circle.area(Circle(1,2,4)), 50.26548245743669 )

    def test__move__(self):
        self.assertEqual(Circle.move(Circle(1,2,4), 2, 4), Circle(3,6,4))

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()


