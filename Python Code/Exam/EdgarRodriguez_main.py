from EdgarRodriguez_Class_Contact import Contact
from EdgarRodriguez_Class_Direction import Direction

#Hard Coded Directions
dir1 = Direction("Fake Street","123","Sprigfield","SP")
dir2 = Direction("Sweet Home","7","Alabama","AL")

#Hard Coded Contacts
contact1 = Contact("Homer","Simpson", "555-930-127",dir1)
contact2 = Contact("Jhon", "Doe","555-123-456",dir2)

#List of contacts
MyContactsList = [contact1,contact2]


def main():
    for contact in MyContactsList:
        print(contact)


#Execution
main()
