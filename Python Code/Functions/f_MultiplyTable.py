import math

#Mostrar la tabla de multiplicar
def tablaMultiplicar(num):
    table = []
    for i in range(11):
        multi = num * i
        table.append(multi)
        i+=1
    return table

multiTable = tablaMultiplicar(5)
print(multiTable)



