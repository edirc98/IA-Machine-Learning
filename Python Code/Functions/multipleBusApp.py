import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

bus = """             .---------------------------.
           /,--..---..---..---..---..--. `.
          //___||___||___||___||___||___\_|
          [j__ ######################## [_|
             \============================|
          .==|  |```||```||```||```| |```||
         /======"---""---""---""---"=|  =||
         |____    []*          ____  | ==||
         //  \\               //  \\ |===|| 
         "\__/"---------------"\__/"-+---+"""
busLetters = """             
88                                   88                                          88  
88                                   88                                          88   
88,dPPYba,  88       88 ,adPPYba,    88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,88   
88P'    "8a 88       88 I8[    ""    88P'    "8a ""     `Y8 88P'   `"8a a8"    `Y88    
88       d8 88       88  `"Y8ba,     88       d8 ,adPPPPP88 88       88 8b       88 
88b,   ,a8" "8a,   ,a88 aa    ]8I    88b,   ,a8" 88,    ,88 88       88 "8a,   ,d88    
8Y"Ybbd8"'   `"YbbdP'Y8 `"YbbdP"'    8Y"Ybbd8"'  `"8bbdP"Y8 88       88  `"8bbdP"Y8"""


def createBusTickets():
    print(bus + busLetters + "\n")
    buses = []
    total_buses = int(input("Escribir el numero de buses que tiene la organización: "))
    total_places = int(input("Escribir el numero de plazas totales del bus: "))
    # [VENDIDOS(0),RESTANTES(1)]
    for i in range(total_buses):
        buses.append([0, total_places])
    clear_screen()
    return buses


def sellTickets(tl, numSell, busId):
    if 0 <= busId < len(tl):
        if numSell <= tl[busId][1]:
            tl[busId][1] -= numSell
            tl[busId][0] += numSell
            return "Vendidos " + str(numSell) + " tickets"
        else:
            return "Error, no se pueden vender mas tickets de los disponibles"
    else:
        return "Error, la compañia no tiene tantos buses porque no tiene dinero."


def returnTickets(tl, numReturn, busId):
    if 0 <= busId < len(tl):
        if numReturn <= tl[busId][0]:
            tl[busId][1] += numReturn
            tl[busId][0] -= numReturn
            return "Devueltos " + str(numReturn) + " tickets"
        else:
            return "Error, no se pueden devolver mas tickets de los vendidos"
    else:
        return "Error, la compañia no tiene tantos buses porque no tiene dinero."


def sellState(tl):
    info = ""
    for i in range(len(tl)):
        info += bus + "\nBus: " + str(i) + "\nTotal Plazas: " + str(tl[i][0] + tl[i][1]) + "\nTickets vendidos: " + str(
            tl[i][0]) + "\nTickets restantes: " + str(tl[i][1]) + "\n"
    return info



def ventaTickets():
    buses = createBusTickets()
    # print(buses)

    exitProgram = False

    while not exitProgram:
        print(bus + busLetters + "\n")
        print("""Que quieres hacer?
        1. Vender billetes (V)
        2. Devolucion de billetes (D)
        3. Estado de la venta (E)
        0. Salir (S)
        """)
        command = input("Escribe tu comando:")
        # print(buses)
        clear_screen()
        if command.capitalize() == "V":
            busId = int(input("Escoge el bus en el que quieras viajar: de 0 a " + str(len(buses) - 1) + ": "))
            numSell = int(input("Numero de tickets a vender: "))
            print(sellTickets(buses, numSell, busId))
        elif command.capitalize() == "D":
            busId = int(input("Escoge el bus en el que quieras viajar: de 0 a " + str(len(buses) - 1) + ": "))
            numReturn = int(input("Numero de tickets a devolver: "))
            print(returnTickets(buses, numReturn, busId))
        elif command.capitalize() == "E":
            print(sellState(buses))
        elif command.capitalize() == "S":
            exitProgram = True
        else:
            print("Invalid Command")

# Ejecucion de codigo
ventaTickets()
