class Person:
    def __init__(PersonClass,name,age):
        print("Persona siendo creada")
        PersonClass.name = name
        PersonClass.age = age 

    def ChangeName(self,newName):
        self.name = newName

P1 = Person("Edgar", 22)

