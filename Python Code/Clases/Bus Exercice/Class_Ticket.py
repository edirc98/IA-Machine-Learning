 
class Ticket:
    def __init__(self,Precio):
        self.__precio = Precio
        self.__nombre = ""

    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre = nombre

    def getPrice(self):
        return self.__precio

    def __str__(self):
        if self.__nombre == "":
            texto = "Price: "+str(self.__precio)
        else:
            texto = "Name: "+str(self.__nombre)+"; Price: "+str(self.__precio)
        return texto