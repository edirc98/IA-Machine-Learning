Algoritmo PintaTrianglos
	Escribir "Dame una altura para el triangulo: "
	leer altura
	Para i = 0 Hasta altura Con Paso 1 Hacer
		string  = Concatenar(string, "-")
	Fin Para
	contador = 1
	Mientras contador < altura hacer
		Escribir Subcadena(string,0 ,contador)
		contador = contador + 1
	FinMientras
	
	Mientras contador > 0 hacer
		Escribir Subcadena(string,0 ,contador)
		contador = contador - 1
	FinMientras

FinAlgoritmo
