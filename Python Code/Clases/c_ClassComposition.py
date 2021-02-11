class Dog:
    def __init__(self, DogName):
        self.name = DogName

class Human:
    def __init__(self, HumanName, Dog):
        self.name = HumanName
        self.dog = Dog


Perrete = Dog("Bingo")
Girl = Human("Amaya",Perrete)

print(Girl.name + " tiene un perrete que se llama " + Girl.dog.name)