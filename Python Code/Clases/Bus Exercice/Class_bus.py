from Class_Ticket import Ticket

class Bus:
    def __init__(self, sites,id,price):
        self.__sites = sites
        self.__bus_id = id
        self.__tickets = self.createTicketsList(sites,price)
        self.__ticketModel = Ticket(price)

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

    def sell(self,numTickets):
        msg = ""
        if numTickets <= len(self.__tickets):
            del self.__tickets[:numTickets]
            msg = "Selled " + str(numTickets) + " on bus " + str(self.__bus_id) + "\n" + str(len(self.__tickets)) + " Tickets remaning"
        else:
            msg = "Not enought tickets" + "\n" + str(len(self.__tickets)) + " Tickets remaning"
        return msg


    def restore(self,numTickets):
        msg = ""
        if numTickets <= (self.__sites - len(self.__tickets)):
            for i in range(0,numTickets):
                self.__tickets.append(self.__ticketModel)
            msg = "Restored " + str(numTickets) + " on bus " + str(self.__bus_id) + "\n" + str(len(self.__tickets)) + " Tickets remaning"
        else:
            msg = "You can not restore more than total sites of the bus" + "\n" + str(self.__sites - len(self.__tickets)) + " Remaning Tickets for restore"
        return msg

    
    def __str__(self):
        tickStr = ""
        for ticket in self.__tickets:
            tickStr += "[ " + ticket.__str__() + " ]"
        return "Bus with id: " + str(self.__bus_id) + "\n" + "Number of sites: " + str(self.__sites) + "\n" + "Tickets remaning " + tickStr + "\n"
