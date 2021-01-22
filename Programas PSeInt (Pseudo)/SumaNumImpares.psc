Algoritmo SumaNumImpares
	num = 100
	Mientras num > 0 Hacer
		Si num MOD 2 <> 0 Entonces
			Escribir num
			sumaTotal = sumaTotal + num
		FinSi
		Num = num - 1
	FinMientras
	Escribir "La suma de los 100 primeros numeros impares es de " sumaTotal
FinAlgoritmo
