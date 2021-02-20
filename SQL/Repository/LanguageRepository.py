from Models.Language import Language

class AdminLanguage:
    #Have and handle the conection to DataBase
    def __init__(self,Connection):
        self.__SQL_Connector = Connection
        self.__tableName = "languages"


    #Getters
    def getConnection(self):
        return self.__cnx
    def getTableName(self):
        return self.__tableName
    
    #CRUD OPERATIONS
    #Create
    def createLanguage(self,Language):
        #INSERT Query
        q = "INSERT INTO " + self.__tableName + " (language) VALUES ('%s')" % (Language.getLanguageName())
        cursor = self.__SQL_Connector.getCursor()
        cursor.execute(q)
        self.__SQL_Connector.getConection().commit()
        

    #Read
    def getLanguages(self):
        #SELECT * Query
        languages = []
        
        q = "SELECT * FROM " + self.__tableName 
        cursor = self.__SQL_Connector.getCursor()
        cursor.execute(q)
        db_languages = cursor.fetchall()

        for language in db_languages:
            l = Language(language[0],language[1])
            languages.append(l)

        return languages

    #Update
    def updateLanguage(self,Language):
        #Update Query
        pass
    #Delete
    def deleteLanguage(self,Language):
        #Delete Query
        pass