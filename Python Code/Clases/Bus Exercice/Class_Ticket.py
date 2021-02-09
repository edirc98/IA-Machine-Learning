 
class Ticket:
    def __init__(self,Precio):
        self.__precio = Precio

    def getPrice(self):
        return self.__precio

    def __str__(self):
        return str(self.__precio)