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

#PADRE(FIGURA GEOMETRICA)
class GeometricFigrue:

    def __init__(self,CoordsList,Color):
        self.__coords = Coord(CoordsList)
        self.__color = Color
    
    def getCoord_X(self):
        return self.__coords.getX()
    def getCoord_Y(self):
        return self.__coords.getY()
    #Get/Set Color
    def getColor(self):
        return self.__color
    def setColor(self,newColor):
        self.__color = newColor


#HIJA(CUADRADO) Hereda de figura Geometrica
class Cuadrado(GeometricFigrue):
    def __init__(self,CoordsList,b,h,Color):
        super().__init__(CoordsList,Color)
        self.__base = b
        self.__height = h
        self.__area = self.__CalcArea()

    def __CalcArea(self):
        return self.__base * self.__height

    def GetArea(self):
        return self.__area

    def Myfunc(self):
        print(self.getCoord_X()) 

class Circle(GeometricFigrue):
    def __init__(self,CoordsList,radius,Color):
        super.__init__(CoordsList,Color)
        self.radius = radius

c1 = Cuadrado([4,4],5,6,"Red")

print(c1.getCoord_X())
print(c1.GetArea())
print(c1.getColor())




