from Class_bus import Bus
class busGestion:
    __BusList = []
    def __init__(self):
        self.createEnterpriseStructure()

    #MANAGEMENT FUNCTIONS
    def sellBusTickets(self,busId,numToSell):
        if busId <= len(self.__BusList) and busId >= 0:
            return self.__BusList[busId].sell(numToSell)
        else: return "Incorrect bus number"
    def restoreBusTickets(self,busId,numToRestore):
        if busId <= len(self.__BusList) and busId >= 0:
            return self.__BusList[busId].restore(numToRestore)
        else: return "Incorrect bus number"

    #FUNCTIONS    
    def createEnterpriseStructure(self):
        numbuses = int(input("Number of buses in your enterprise: "))
        for i in range(0,numbuses):
            busSites = int(input("Number of sites of bus numnber " + str(i + 1) + ": "))
            TickePrice = float(input("Price of each ticket: "))
            self.__BusList.append(Bus(busSites,i,TickePrice))


    def __str__(self):
        strAux = ""
        for bus in self.__BusList:
            strAux += bus.__str__() + "\n"
        return strAux
