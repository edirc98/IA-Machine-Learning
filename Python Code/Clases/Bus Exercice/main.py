from Class_gestor import busGestion
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def menu(): 
    menu_str = """
    -------------------------------------------------
    |                                               |
    |       Management options:                     |
    |   1. Sell Tickets (Keyword "Sell")            |
    |   2. Return Tickets (Keyword "Return")        |
    |   3. Chek current status (Keyword "Status")   |
    |   4. Exit and Close (Keyword "Exit")          |
    |                                               |
    -------------------------------------------------
    """ 
    print(menu_str)   
    command = input("Select option writing the keyword: ")
    clear_screen()
    return command

def sellingData():
    busID = int(input("Bus number or ID: "))
    numTickets = int(input("Number of tickets to sell: "))
    return busID, numTickets
def returnData():
    busID = int(input("Bus number or ID: "))
    numTickets = int(input("Number of tickets to return: "))
    return busID, numTickets 


def main():
    running = True
    Gestion = busGestion()
    
    while running: 
        
        command = menu()
        if command == "Sell":
            busID,selledTickets = sellingData()
            print(Gestion.sellBusTickets(busID,selledTickets))
        elif command == "Return":
            busID,returnedTickets = returnData()
            print(Gestion.restoreBusTickets(busID,returnedTickets))
        elif command == "Status":
            print(Gestion)
        elif command == "Exit":
            print("Have a nice day")
            running = False


main()