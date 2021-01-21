Algoritmo ElJuegoDeLasPreguntas
	Escribir "Contestame las siguientes preguntas con s(SI) o n (NO)"
	Escribir "Colon descubrio America?"
	Leer respuesta
	respuesta = Minusculas(respuesta)
	Si respuesta = "s" Entonces
		Escribir "Correcto has acertado, sigue jugando"
		Escribir "La capital de Inglaterra es Cambridge?"
		Leer respuesta
		Si respuesta = "n" Entonces
			Escribir "Correcto has acertado, sigue jugando"
			Escribir "El sol, es una estrella?"
			Leer respuesta
			Si respuesta = "s" Entonces
				Escribir "Correcto has acertado, Has ganado, pero no hay premio, lo sentimos, somos pobres para dar premios"
			SiNo
				Escribir "Hsa fallado y has perdido"
			FinSi
		SiNo
			Escribir "Hsa fallado y has perdido"
		FinSi
	SiNo
		Escribir "Hsa fallado y has perdido"
	FinSi
	
FinAlgoritmo
