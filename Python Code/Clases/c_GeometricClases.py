import math

class Square:

    #Constructor
    def __init__(self,b,h):
        self.base = b
        self.height = h
        self.__area = self.__area()

    #Setters
    def setSquareData(self,newBase,newHeight):
        self.base = newBase
        self.height = newHeight
    def setSquareBase(self,newBase):
        self.base = newBase
    def setSquareHeight(self,newHeight):
        self.height = newHeight

    #Getters
    def getSquareBase(self):
        return self.base
    def getSquareHeight(self):
        return self.height
    def getSquareArea(self):
        return self.__area
    #Functions
    def __area(self):
        return self.base * self.height


class Triangle:
    #Constructor
    def __init__(self,base,height):
        self.base = base
        self.height = height
        self.__area = self.__area()
    
    #Setters
    def setTriangleBase(self,newBase):
        self.base = newBase
    def setTriangleHeigth(self,newHeigth):
        self.base = newHeigth

    #Getters
    def getTriangleBase(self):
        return self.base
    def getTriangleHeight(self):
        return self.height
    def getTriangleArea(self):
        return self.__area

    #Functions
    def __area(self):
        return ((self.base * self.height) / 2)


class Circle:
    #Constructor
    def __init__(self,radius):
        self.radius = radius
        self.__area = self.__area()
    
    #Setters
    def setCircleRadius(self,newRadius):
        self.radius = newRadius
    #Getters
    def getCircleRadius(self):
        return self.radius
    def getCircleArea(self):
        return self.__area

    #Functions
    def __area(self):
        return math.pi * self.radius**2

s1 = Square(10,10)
t1 = Triangle(10,5)
c1 = Circle(5)

