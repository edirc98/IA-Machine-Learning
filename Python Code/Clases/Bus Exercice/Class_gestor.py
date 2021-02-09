from Class_bus import Bus
class busGestion:
    __BusList = []
    def __init__(self):
        self.createEnterpriseStructure()


    #GETTERS
    def getBusLits(self):
        return self.__BusList
    #FUNCTIONS    
    def createEnterpriseStructure(self):
        numbuses = int(input("Number of buses in your enterprise: "))
        for i in range(0,numbuses):
            busSites = int(input("Number of sites of bus numnber " + str(i + 1) + ": "))
            TickePrice = int(input("Price of each ticket: "))
            self.__BusList.append(Bus(busSites,i,TickePrice))


    def __str__(self):
        strAux = ""
        for bus in self.__BusList:
            strAux += bus.__str__() + "\n"
        return strAux
