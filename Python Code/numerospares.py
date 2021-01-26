#Numeros PARES de 0 a 100
i = 0
while i <= 100:
    if i%2 == 0:
        print(i)
    i+=1

#Numeros IMPARES de 0 a 100
i = 0
c = 0
while i <= 100:
    if i%2!= 0:
        print(i)
        c+=1
    i+=1
print(c)