Algoritmo CaptialAñadido
	Escribir "Inserte a cantidad de dinero a invertir:"
	leer capital
	Escribir "En cuantos años: "
	leer años
	i = 1
	Mientras i <= años Hacer
		incremento = (capital / 100) * 2
		capital =  capital + incremento
		i = i + 1
	FinMientras
	Escribir "El capital al cabo " años " años es de: " capital
FinAlgoritmo
