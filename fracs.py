class Frac:
    """Klasa reprezentująca ułamki."""

    def __init__(self, x=0, y=1):
        # Sprawdzamy, czy y=0.
        self.x = x
        self.y = y

    def __str__(self): 
        return self.x if self.y == 1 else "{}/{}".format(self.x, self.y)          # zwraca "x/y" lub "x" dla y=1

    def __repr__(self): 
        return "Frac({}, {})".format(self.x, self.y)      # zwraca "Frac(x, y)"

    # Python 2.7 i Python 3
    def __eq__(self, other):
        return float(self.x/self.y) == float(other.x/other.y)

    def __ne__(self, other):
        return not (float(self.x/self.y) == float(other.x/other.y))

    def __lt__(self, other): 
        return float(self.x/self.y) < float(other.x/other.y)

    def __le__(self, other): 
        return float(self.x/self.y) <= float(other.x/other.y)

    def __gt__(self, other): 
        return float(self.x/self.y) > float(other.x/other.y)

    def __ge__(self, other): 
         return float(self.x/self.y) >= float(other.x/other.y)

    def __add__(self, other):
        if self.y == other.y:
            return Frac(self.x + other.x, self.y)
       
        elif other.y == 1:
            return Frac((self.x + other.x * self.y), self.y)

        else:
            return Frac((self.x * other.y + self.y * other.x ), (self.y * other.y))


    __radd__ = __add__              # int+frac

    def __sub__(self, other):
          # frac1-frac2, frac-int
        if self.y == other.y:
            return Frac(self.x - other.x, self.y)
       
        elif other.y == 1:
            return Frac(self.x - self.y * other.x, self.y)

        else:
            return Frac((self.x * other.y - self.y * other.x ), (self.y * other.y))


    def __rsub__(self, other):      # int-frac
        
        return Frac(self.x * other.y - other.x, other.y)

    def __mul__(self, other): 
        # frac1*frac2, frac*int
        return Frac(self.x * other.x, self.y * other.y)

    __rmul__ = __mul__              # int*frac

    def __truediv__(self, other): 
        if other.y == 1: 
            return Frac(self.x, self.y * other.x)
        else: 
            return Frac(self.x * other.y, self.y * other.x)

    def __rtruediv__(self, other):
        if self.y == 1: 
           return Frac(self.x * other.y, other.x)
        else:
            return Frac(self.x * other.y, self.y * other.x) 

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return Frac(self.x, self.y)

    def __neg__(self): 
        return Frac(self.x, self.y)         # -frac = (-1)*frac

    def __invert__(self):       # odwrotnosc: ~frac
         return Frac(self.y, self.x) 

    def __float__(self):       # float(frac)
        return float(self.x/self.y)
        
    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # assert set([2]) == set([2.0])


# Kod testujący moduł.

print(Frac.__str__(Frac(2,2)))

import unittest

class TestFrac(unittest.TestCase): 
    def test__str__(self):
        self.assertEqual(Frac.__str__(Frac(1,2)), '1/2')

    def test__repr__(self):
        self.assertEqual(Frac.__repr__(Frac(1,2)), 'Frac(1, 2)')

    def test__eq__(self):
        self.assertEqual(Frac.__eq__(Frac(1,2), Frac(1, 2) ), True)
        self.assertEqual(Frac.__ne__(Frac(1, 2), Frac(3, 4)), True)
        self.assertEqual(Frac.__lt__(Frac(1, 2), Frac(3, 4)), True)
        self.assertEqual(Frac.__le__(Frac(1, 2), Frac(5, 6)), True)
        self.assertEqual(Frac.__le__(Frac(3, 4), Frac(3, 4)), True)
        self.assertEqual(Frac.__gt__(Frac(8, 9), Frac(3, 4)), True)
        self.assertEqual(Frac.__ge__(Frac(1, 2), Frac(2, 4)), True)
        self.assertEqual(Frac.__ge__(Frac(3, 4), Frac(1, 2)), True)

    def test__add__(self):
        self.assertEqual(Frac.__add__(Frac(1,2), Frac(3,4)), Frac(10,8))
        self.assertEqual(Frac.__add__(Frac(5,2), Frac(7,4)), Frac(17,4))

    def test__sub__(self):
        self.assertEqual(Frac.__sub__(Frac(5,6), Frac(3,6)), Frac(2, 6))
        self.assertEqual(Frac.__sub__(Frac(5,6), Frac(3,1)), Frac(-13, 6))
        self.assertEqual(Frac.__sub__(Frac(5,6), Frac(3,4)), Frac(2, 24))

    def test__rsub__(self):
        self.assertEqual(Frac.__rsub__(Frac(3,1), Frac(5,6)), Frac(13, 6))
       
    def test__mul__(self):
        self.assertEqual(Frac.__mul__(Frac(1,2), Frac(3,4)), Frac(3,8))

    def test__truediv(self):
        self.assertEqual(Frac.__truediv__(Frac(1, 2), Frac(3,4)), Frac(4,6))
        self.assertEqual(Frac.__truediv__(Frac(1, 2), Frac(3,1)), Frac(1,6))

    def test__rtruediv(self):
        self.assertEqual(Frac.__rtruediv__(Frac(3, 1), Frac(1,2)), Frac(6,1))
        self.assertEqual(Frac.__rtruediv__(Frac(1, 2), Frac(3,1)), Frac(1,6))
    
    def test_invert__(self):
        self.assertEqual(Frac.__invert__(Frac(1,2)), Frac(2,1))

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()