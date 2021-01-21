Algoritmo SegundosAFecha
	Escribir "Dame un numero de segundos: "
	Leer secss
	horas = secss/3600
	horas = trunc(horas)
	minutos = secss-(horas*3600)
	minutos = minutos/60
	minutos = trunc(minutos)
	sec = secss-(minutos*60)-(horas*3600)
	Escribir horas " horas, " minutos " minutos, " sec " segundos."
FinAlgoritmo
