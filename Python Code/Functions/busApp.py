def CreateBusTickets():
    total_places = int(input("Escribir el numero de plazas totales del bus: "))
    #[VENDIDOS(0),RESTANTES(1)]
    return [0,total_places]

def SellTickets(tl,numSell):
    if(numSell <= tl[1]):
        tl[1] -= numSell
        tl[0] += numSell
        return "Vendidos " + str(numSell) + " tickets"
    else:
        return "Error, no se pueden vender mas tickets de los disponibles"
    
def ReturnTickets(tl,numReturn):
    if numReturn <= tl[0]:
        tl[1] += numReturn
        tl[0] -= numReturn
        return "Devueltos " + str(numReturn) + " tickets"
    else:
        return "Error, no se pueden devolver mas tickets de los vendidos"

def SellState(tl):
    return "Total Plazas: " + str(tl[0] + tl[1] ) +"\nTickets vendidos: "  + str(tl[0]) + "\nTickets restantes: " + str(tl[1])


def VentaTickets():
    Tickets = CreateBusTickets()
    exitProgram = False
    while exitProgram != True:
        print("""Que quieres hacer?
        1. Vender billetes (V)
        2. Devolucion de billetes (D)
        3. Estado de la venta (E)
        0. Salir (S)
        """)
        command = input("Escribe tu comando:")

        if command.capitalize() == "V":
            numSell = int(input("Numero de tickets a vender: "))
            print(SellTickets(Tickets,numSell))  
        elif command.capitalize() == "D":
            numReturn = int(input("Numero de tickets a devolver: "))
            print(ReturnTickets(Tickets, numReturn))
        elif command.capitalize() == "E":
            print(SellState(Tickets))
        elif command.capitalize() == "S":
            exitProgram = True
        else:
            print("Invalid Command")



#Ejecucion de codigho
VentaTickets()