import mysql.connector

class Connector:
    def __init__(self):
        f = open("C:\\Users\Edgar\Documents\pass.txt", "r")
        password = f.read()
        self.__cnx = mysql.connector.connect(user='root', password = password, host='localhost', database='cdscollection')
        self.__cursor = self.__cnx.cursor()
         
    #Getters
    def getConection(self):
        return self.__cnx
    def getCursor(self):
        return self.__cursor