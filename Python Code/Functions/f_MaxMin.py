def MinMax(lista):
    min = lista[0]
    max = lista[0]
    for n in lista:
        if n > max:
            max = n
        if n < min:
            min = n
    return min, max


lista1 = [1, 5, 8, 50, 46, 10, 48, -49, 70, 50, 30, 2]

print(MinMax(lista1))
