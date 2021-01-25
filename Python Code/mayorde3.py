num1 = float(input("Introduce un numero: "))
num2 = float(input("Introduce un numero: "))
num3 = float(input("Introduce un numero: "))

if num1 > num2 and num1 > num3:
    print(str(num1) + "es el numero más grande.")
elif num2 > num1 and num2 > num3:
    print(str(num2) + "es el numero más grande.")
else:
    print(str(num3) + "es el numero más grande.")



