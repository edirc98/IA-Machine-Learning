#CDS Collection Aplication. 
from Service.SQL_Connector import Connector
from Models.Language import Language
from Repository.LanguageRepository import AdminLanguage


#User input functions
def getUserCommand():
    command = input("Type yor command: ")
    return command
def userCreateLanguage():
    newName = input("Type the language: ")
    l = Language(0,newName)
    return l
def userUpdateLanguage():
    idlang = int(input("Type the id to update: "))
    newName = input("Type the new language: ")
    l = Language(idlang,newName)
    return l
def userDeleteLanguage():
    idLang = int(input("Type the index to delete: "))
    l = Language(idLang, "NONE")
    return l

menu = """
 ----------------------------------------
 |  CRUD OPERATIONS IN LANGUAGES TABLE  |
 |  1. Create Language - (create)       |
 |  2. Read Languages  -  (read)        |
 |  3. Update Language - (update)       |
 |  4. Delete Language - (delete)       |
 |  5. Exit Program    - (exit)         |
 ----------------------------------------
"""


def main():
    #Mani Loop Control
    ExitProgram = False
    #Conexion to database
    print("Establishing conection to database")
    c = Connector()
    aL = AdminLanguage(c)   

    #Main Loop
    while not ExitProgram:
        print(menu)
        command = getUserCommand()
        if command == "create":
            aL.createLanguage(userCreateLanguage())

        elif command == "read":
            listLanguages = aL.getLanguages()
            for l in listLanguages:
                print(l)
            del listLanguages

        elif command == "update":
            aL.updateLanguage(userUpdateLanguage())
        elif command == "delete":
            aL.deleteLanguage(userDeleteLanguage())
        elif command == "exit":
            ExitProgram = True
        else:
            print("Invalid Command")
    

    c.getCursor().close()
    c.getConection().close()
    print("Conexions closed, Bye bye")

#Main function Call
main()


