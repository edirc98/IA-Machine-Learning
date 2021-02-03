import math

class Square:
<<<<<<< HEAD
=======

>>>>>>> f7ca382d4d89378769d10acb3e9e7ff1f4e34e04
    def __init__(self,b,h):
        self.base = b
        self.height = h

    def area(self):
        return self.base * self.height


class Triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height
    
    def area(self):
        return ((self.base * self.height) / 2)


class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius**2

s1 = Square(10,10)
t1 = Triangle(10,5)
c1 = Circle(5)

