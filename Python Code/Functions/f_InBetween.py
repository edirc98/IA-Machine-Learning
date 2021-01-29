#Mostrar numeros intermedios entre dos numeros dados
def InBetween(num1,num2):
    between_list = []
    if num1 < num2:
        for num1 in range(num1,num2+1,1):
            between_list.append(num1)
    else:
       for num2 in range(num2,num1+1,1):
            between_list.append(num2)

    return between_list

b_l = InBetween(10,50)
print(b_l)