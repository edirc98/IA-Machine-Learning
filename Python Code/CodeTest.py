print("Hello World")
numero = 1000
print(numero)
numero = 10.7
print(numero)
numero = "Hola"
print(numero)

palabras = "Hola me lo paso muy bien"
cn1 = "Cadena 1"
cn2 = "Cadena 2"

Cadenas = cn1 + cn2

cortada = cn1[1:4]
thelast = cn1[:-1]
print(thelast)
print(len(Cadenas))

h = 4
c = "-"
cT = ""
i = 0

while i < h*2:
    if i < h:
        cT += c
    else:
        cT = cT[:-1]

    i += 1
    print(cT)

    
name = input("Say your name: ")
print("Hello " + name + "!")