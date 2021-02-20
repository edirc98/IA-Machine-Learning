from Models.Language import Language

class AdminLanguage:
    #Have and handle the conection to DataBase
    def __init__(self,Connection):
        self.__cnx = Connection
        self.__tableName = "languages"


    #Getters
    def getConnection(self):
        return self.__cnx
    def getTableName(self):
        return self.__tableName
    
    #CRUD OPERATIONS
    #Create
    def createLanguage(self,Language):
        #Create Query
        pass
    #Read
    def getAll(self):
        #Select * Query
        pass
    #Update
    def updateLanguage(self,Language):
        #Update Query
        pass
    #Delete
    def deleteLanguage(self,Language):
        #Delete Query
        pass