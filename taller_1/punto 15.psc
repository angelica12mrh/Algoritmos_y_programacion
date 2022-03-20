Algoritmo Inicio
	Definir n,b Como Entero
	Definir a,x Como Caracter
	Escribir" ingresa un numero de dos cifras "
	Leer n
	a=ConvertirATexto(n)
	b=Longitud(a)
	x =""
	Mientras b > 0 Hacer
		X = X + Subcadena(a,b,b)
		b = b - 1
	FinMientras
	Escribir " El numero " ,n, " invertido es: " ,ConvertirANumero(x)
FinAlgoritmo
