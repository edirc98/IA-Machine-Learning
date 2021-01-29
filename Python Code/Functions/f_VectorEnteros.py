def isInList(lista, num1):
    if lista.count(num1) > 0:
        return True
    else:
        return False


lista1 = [1, 2, 5, 70, 25, 366, 45]

print(isInList(lista1, 0))
