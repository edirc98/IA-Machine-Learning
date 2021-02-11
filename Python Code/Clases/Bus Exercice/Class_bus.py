from Class_Ticket import Ticket

class Bus:
    __income = 0
    __returns = 0
    def __init__(self, sites,id,price):
        self.__sites = sites
        self.__bus_id = id
        self.__tickets = self.createTicketsList(sites,price)
        self.__t_vendidos = []
        self.__ticketModel = Ticket(price)


    def getBusSites(self):
        return self.__sites
    def getBusId(self):
        return self.__bus_id

    def getIncome(self):
        return self.__income
    def getReturns(self):
        return self.__returns

    
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
            for i in range (numTickets):
                name_input = input("Please, introduce passenger name: ")
                name = name_input.lower().capitalize()
                ticket_ref = Ticket(self.__ticketModel.getPrice())
                ticket_ref.setNombre(name)
                self.__t_vendidos.append(ticket_ref)
            self.__income += (numTickets * self.__ticketModel.getPrice())
            msg = "Selled " + str(numTickets) + " on bus " + str(self.__bus_id) + "\n" + str(len(self.__tickets)) + " Tickets remaning"
        else:
            msg = "Not enought tickets" + "\n" + str(len(self.__tickets)) + " Tickets remaning"
        return msg


    def restore(self,numTickets):
        msg = ""
        msg_no_name = ""
        cont_return = 0
        if numTickets <= (self.__sites - len(self.__tickets)):
            for i in range(numTickets):
                name_return = input("Indique el nombre del usuario a devolver: ")
                name_ret_cap= name_return.lower().capitalize()
                for k,j in enumerate(self.__t_vendidos):
                    if j.getNombre() == name_ret_cap:
                        del self.__t_vendidos[k]
                        self.__tickets.append(self.__ticketModel)
                        name_founded = True
                        cont_return += 1
                        break
                    else:
                        name_founded = False
                if not name_founded:
                    msg_no_name+="The name "+name_return+" isn't exist\n"

            self.__returns = (numTickets * self.__ticketModel.getPrice()) 
            self.__income -= self.__returns
            msg = "Restored " + str(cont_return) + " on bus " + str(self.__bus_id) + "\n" + str(len(self.__tickets)) + " Tickets remaning"
        else:
            msg = "You can not restore more than total sites of the bus" + "\n" + str(self.__sites - len(self.__tickets)) + " Remaning Tickets for restore"
        if msg_no_name != "":
            msg = msg+"\n"+msg_no_name
        return msg

    
    def __str__(self):
        tickStr = ""
        tickSell =  ""
        for ticket in self.__tickets:
            tickStr += "[ " + ticket.__str__() + " ]"
        for ticketS in self.__t_vendidos:
            tickSell += "[ "+ticketS.__str__()+" ]\n"
        return "Bus with id: " + str(self.__bus_id) + "\n" + "Number of sites: " + str(self.__sites) + "\n" + "Tickets remaning " + tickStr + "\n" +"Tickets Selled\n "+tickSell+" \nIncome henerated: " + str(self.__income) + "\n"
