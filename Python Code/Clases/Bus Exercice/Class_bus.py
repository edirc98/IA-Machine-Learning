from Class_Ticket import Ticket

class Bus:
    def __init__(self, sites,id,price):
        self.__sites = sites
        self.__bus_id = id
        self.__Tickets = self.createTicketsList(sites,price)

    def getBusSites(self):
        return self.__sites
    def getBusId(self):
        return self.__bus_id

        


    #FUNCTIONS
    def createTicketsList(self,sites,price):
        aux = []
        for i in range(0,sites):
            ticket = Ticket(price)
            aux.append(ticket)
        return aux

    def __str__(self):
        return "Bus con id: " + str(self.__bus_id) + "\n" + "Numero de sitios: " + str(self.__sites) + "\n"
