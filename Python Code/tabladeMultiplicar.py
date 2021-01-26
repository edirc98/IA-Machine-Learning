num = int(input("Numero para la tabla: "))

for i in range(11):
    multi = num * i
    print(str(num) + " x " + str(i) + " = " + str(multi))
    i+=1