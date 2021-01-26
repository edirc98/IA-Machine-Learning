num = int(input("Numero para la tabla: "))

def tablaMultiplicar(num):
    for i in range(11):
        multi = num * i
        print(str(num) + " x " + str(i) + " = " + str(multi))
        i+=1

tablaMultiplicar(num)