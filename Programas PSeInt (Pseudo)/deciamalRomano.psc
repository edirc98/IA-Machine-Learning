Algoritmo decimalRomano
	Escribir "Introduce un numero: "
	Leer num
	numRomano <- ""
	Mientras num > 0 Hacer
		cant <- trunc(num / 1000)
		Si cant > 0 Entonces
			Para i <- 1 Hasta cant Con Paso 1 Hacer
				Escribir Sin Saltar "M"
				num <- num - 1000
			Fin Para
		Fin Si
		cant <- trunc(num / 500)
		Si cant > 0 Entonces
			Para i <- 1 Hasta cant Con Paso 1 Hacer
				Escribir Sin Saltar "D"
				num <- num - 500
			Fin Para
		FinSi
		cant <- trunc(num / 100)
		Si cant > 0 Entonces
			Para i <- 1 Hasta cant Con Paso 1 Hacer
				Escribir Sin Saltar "C"
				num <- num - 100
			Fin Para
		FinSi
		cant <- trunc(num / 50)
		Si cant > 0 Entonces
			Para i <- 1 Hasta cant Con Paso 1 Hacer
				Escribir Sin Saltar "L"
				num <- num - 50
			Fin Para
		FinSi
		cant <- trunc(num / 10)
		Si cant > 0 Entonces
			Para i <- 1 Hasta cant Con Paso 1 Hacer
				Escribir Sin Saltar "X"
				num <- num - 10
			Fin Para
		FinSi
		
		Segun num Hacer
			1:
				Escribir Sin Saltar "I"
				num <- num - 1
			2:
				Escribir Sin Saltar "II"
				num <- num - 2
			3:
				Escribir Sin Saltar "III"
				num <- num - 3
			4:
				Escribir Sin Saltar "IV"
				num <- num - 4
			5:
				Escribir Sin Saltar "V"
				num <- num - 5
			6:
				Escribir Sin Saltar "VI"
				num <- num - 6
			7:
				Escribir Sin Saltar "VII"
				num <- num - 7
			8:
				Escribir Sin Saltar "VIII"
				num <- num - 8
			9:
				Escribir Sin Saltar "IX"
				num <- num - 9
		Fin Segun
		
		
		
	Fin Mientras
FinAlgoritmo
