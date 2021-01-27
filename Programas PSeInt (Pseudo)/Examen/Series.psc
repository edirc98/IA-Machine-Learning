Algoritmo Series
	Escribir "Entra dos numero menores a 50: "
	leer num1
	leer num2 
	Si num1<50 y num2 <50
		Si num1>num2 Entonces 
			Mientras num2 < num1 Hacer
				num2 = num2 + 5
				Escribir num2
				num1 = num1 - 2
				Escribir num1
			FinMientras
		SiNo
			Mientras num1 < num2 Hacer
				num1 = num1 + 5
				Escribir num1
				num2 = num2 - 2
				Escribir num2
			FinMientras
		FinSi
	SiNo
		Escribir"Deben ser numero menores a 50"
	FinSi
	
FinAlgoritmo
