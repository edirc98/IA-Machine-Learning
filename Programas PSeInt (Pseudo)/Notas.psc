Algoritmo NotaAlumno
	Escribir "Escriba la nota numerica de un alumno:"
	Leer nota
	Si nota < 4 Entonces
		Escribir "Muy mal,has suspendido."
	SiNo
		Si nota > 4 y nota < 5.5 Entonces
			Escribir "Has aprobado por los pelos, suficiente."
		SiNo
			Si nota >= 5.5 y nota < 6.9 Entonces
				Escribir "Has aprobado, bien."
			SiNo
				Si nota >= 6.9 y nota < 8.9 Entonces
					Escribir "Has aprobado, Notable."
				SiNo
					Si nota >= 8.9 y nota <= 10Entonces
						Escribir "Has aprobado, Excelente."
					SiNo
						Escribir "Escribir una nota valida entre 0 y 10"
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
	
FinAlgoritmo
