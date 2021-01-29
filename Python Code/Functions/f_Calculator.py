def calculator(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2
    else:
        return "Invalid Operator"


isActive = False

while not isActive:
    option = input("calculator(c), exit (e)")
    if option == "c":
        num1 = float(input("Introduce un numero: "))
        op = input("Elije operación a realizar: (+, -, /, *, %): ")
        num2 = float(input("Introduce otro numero: "))
        res = calculator(num1, op, num2)
        print(str(num1) + " " + op + " " + str(num2) + " = " + str(res))
    elif option == "e":
        isActive = True
