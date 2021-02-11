Algoritmo HorasExtra
	Escribir "Cuantas horas extra has hecho esta semana?"
	Leer num_horas
	Escribir"Cuanto cobras a la hora"
	Leer precio_hora
	Si num_horas <= 8 Y num_horas > 0 Entonces
		remuneracion = num_horas * (precio_hora*2)
	FinSi
	Si num_horas > 8
		remuneracion = 8 * (precio_hora*2)
		num_horas = num_horas - 8
		remuneracion = remuneracion + num_horas * (precio_hora*3)
	SiNo
		Escribir "Debes hacer almenos alguna hora"
	FinSi
	Escribir "Has ganado " remuneracion " en horas extra" 
FinAlgoritmo
