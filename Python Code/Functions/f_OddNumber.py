# Mostrar impares dados dos numeros
def InOddBetween(num1, num2):
    between_list = []
    if num1 < num2:
        for num1 in range(num1, num2 + 1, 1):
            if num1 % 2 == 1:
                between_list.append(num1)
    else:
        for num2 in range(num2, num1 + 1, 1):
            if num2 % 2 == 1:
                between_list.append(num2)
    return between_list


b_l = InOddBetween(99, 43)
print(b_l)

#Mostrar cual es el impar
def OddNumber(num1, num2):
    if num1 % 2 == 1 and num2 % 2 == 1:
        return num1, num2
    elif num1 % 2 == 1:
        return num1
    elif num2 % 2 == 1:
        return num2

res = OddNumber(23, 99)
print(res)
