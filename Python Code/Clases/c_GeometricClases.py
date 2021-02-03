import math

class Coord:
    def __init__(self,cl):
        self.__x = cl[0]
        self.__y = cl[1]
    
    #Setters
    def setX(self,new_X):
        self.__x = new_X
    def setY(self,new_Y):
        self.__y = new_Y
    
    #Getters
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y


class Square:
    #Constructor
    def __init__(self,b,h,CO):
        self.base = b
        self.height = h
        self.__area = self.__area()
        self.coords = Coord(CO)

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
        if self.__area != None:
            return self.__area
        else:
            self.__area = self.__area()
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

MySquare = Square(10,5,[3,4])
print(MySquare.coords.getY())

