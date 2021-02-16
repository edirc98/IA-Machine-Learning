from EdgarRodriguez_Class_Direction import Direction

class Contact:
    def __init__(self, Name, SurName,PhoneNumber,Direction):
        self.__name = Name
        self.__surName = SurName
        self.__phone = PhoneNumber
        self.__direction = Direction

    #GETTERS AND SETTERS
    #NAME
    def getContactName(self):
        return self.__name
    def setContactName(self,newName):
        self.__name = newName
    
    #SURNAME
    def getContactSurName(self):
        return self.__surName
    def setContactSurName(self, newSurName):
        self.__surName = newSurName
    
    #PHONE
    def getContactPhone(self):
        return self.__phone
    def setContactPhonte(self, newPhone):
     self.__phone = newPhone

    #FUNCTIONS (ADDED BY ME)
    def getContactFullName(self):
        return self.__name + " " + self.__surName
    def SetContactFullName (self,newName,newSurName):
        self.__name,self.__surName = newName,newSurName

    #DUNDERS
    def __str__(self):
        return "Contact: " + self.getContactFullName() + " / Phone: " + self.getContactPhone() + "\n" + self.__direction.__str__()
        