class Language:
    def __init__(self,id,Language):
        self.___id = id
        self.__language = Language
    
    #Getters and Setters

    def getLanguageId(self):
        return self.___id
    def setLanguageId(self,newId):
        self.___id = newId

    def getLanguageName(self):
        return self.__language
    def setanguaeName(self,newLanguageName):
        self.__language = newLanguageName