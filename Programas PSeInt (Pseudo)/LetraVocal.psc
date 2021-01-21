Algoritmo Comprobar_vocal
	Escribir "Pon una letra y te digo si es vocal o consonante"
	leer letra
	letra = Minusculas(letra)
	Si letra = "a" o letra = "e" o letra = "i" o letra = "o" o letra = "u" Entonces
		Escribir "La letra que has puesto es una VOCAL"
	SiNo
		Escribir "La letra es una consonante u otra cosa"
	Fin Si
FinAlgoritmo
