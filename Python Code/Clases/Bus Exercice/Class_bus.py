
class bus:
    def __init__(self, sites,id):
        self.__sites = sites
        self.__bus_id = id
        self.__selledTickets = 0
        self.__remainTickets = sites

    def getBusSites(self):
        return self.__sites
    def getBusId(self):
        return self.__bus_id

    def getSelledTickets(self):
        return self.__selledTickets
    def setSelledTickets(self, numSelled):
        self.__selledTickets = numSelled
        self.__remainTickets -= numSelled
