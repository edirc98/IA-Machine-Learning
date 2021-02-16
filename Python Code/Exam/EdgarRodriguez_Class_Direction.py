class Direction: 
    def __init__(self,Street,Number,Province,PostalCode):
        self.__street = Street
        self.__num = Number
        self.__province = Province
        self.__PC = PostalCode

    #GETTERS AND SETTERS
    #STREET
    def getDirectionStreetName(self):
        return self.__street
    def setDirectionStreetName(self,newStreetName):
        self.__street = newStreetName
    
    #NUMBER
    def getDirectionStreetNumber(self):
        return self.__num
    def setDirectionStreetNumber(self,newNumber):
        self.__num = newNumber
    
    #PROVINCE
    def getDirectionProvince(self):
        return self.__province
    def setDirectionProvicne(self,newProvince):
        self.__province = newProvince
    
    #POSTAL CODE
    def getDirectionPostalCode(self):
        return self.__PC

    def setDirectionPostalCode(self, newPostalCode):
        self.__PC = newPostalCode


    #FUNCTIONS
    def __str__(self):
        return "Direction: " + self.getDirectionStreetName() + ", " + self.getDirectionStreetNumber() + ", " + self.getDirectionProvince() + ", " + self.getDirectionPostalCode() + "\n"