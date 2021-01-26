inversion = float(input("Cantidad a Invertir: "))
time  = int(input("Años de inversion: "))
i = 0
for i in range(time+1):
    inc = (inversion / 100) * 2
    inversion += inc
    i+=1
print("La cantidad despues de " + str(time) + " es de: " + str(inversion))
