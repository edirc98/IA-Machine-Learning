

print("Responde con 's' o con 'n'")

res = input("¿Colon descubrió América?")

if res == 's':
    print("La respuesta es correcta!")
    res2 = input("La capital de Inglaterra es Campbridge?")
    if res2 == 'n':
        print("La respuesta es correcta!")
        res3 = input("¿El sol, es una estrella?")
        if res3 == 's':
            print("La respuesta es correcta! Has ganado!")
else:
    print("Has perdido, vuelve a intentarlo.")
