Algoritmo CaptialA�adido
	Escribir "Inserte a cantidad de dinero a invertir:"
	leer capital
	leer a�os
	Mientras i <= a�os Hacer
		incremento = ( capital / 100) * 2
		capital =  capital + incremento
		i = i + 1
	FinMientras
	Escribir "El capital al cabo " a�os " a�os es de: " capital
FinAlgoritmo
