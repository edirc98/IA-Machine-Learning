Algoritmo SumaDeNumeros
	Escribir "Pon numeros para que sean sumados, hasta que pongas un 0 no dejara de pedirte numeros"
	Repetir
		Leer num
		SumaTotal = SumaTotal + num
		Counter = Counter + 1
	Hasta Que num = 0
	Escribir "Se han introducido " counter - 1 " numeros y su suma total es de " SumaTotal
FinAlgoritmo
