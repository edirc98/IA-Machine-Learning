from Class_bus import Bus
class busGestion:
    __BusList = []
    __collection = 0
    def __init__(self):
        self.createEnterpriseStructure()


    #GETTERS
    def getCollection(self):
        return self.__collection
    def setCollection(self,collect):
        self.__collection = collect
        
    #MANAGEMENT FUNCTIONS
    def sellBusTickets(self,busId,numToSell):
        if busId <= len(self.__BusList) and busId >= 0:
            msg = self.__BusList[busId].sell(numToSell)
            self.__collection += self.__BusList[busId].getIncome()
            return msg
        else: return "Incorrect bus number"

    def restoreBusTickets(self,busId,numToRestore):
        if busId <= len(self.__BusList) and busId >= 0:
            msg = self.__BusList[busId].restore(numToRestore)
            self.__collection -= self.__BusList[busId].getReturns()
            return msg 
        else: return "Incorrect bus number"

    #FUNCTIONS    
    def createEnterpriseStructure(self):
        numbuses = int(input("Number of buses in your enterprise: "))
        for i in range(0,numbuses):
            busSites = int(input("Number of sites of bus numnber " + str(i + 1) + ": "))
            TickePrice = float(input("Price of each ticket: "))
            self.__BusList.append(Bus(busSites,i,TickePrice))



    def __str__(self):
        strAux = "Total income generated: " + str(self.__collection) + "\n"
        for bus in self.__BusList:
            strAux += bus.__str__() + "\n"
        return strAux
