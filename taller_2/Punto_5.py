"""
Entradas: 5 valores flotantes que son las notas del estudiante
Nota 1 parcial --> float --> N0
Nota 2 parcial --> float --> N1 
Nota 3 parcial --> float --> N2
Nota 4 Examen final --> float --> N3
Nota 5 trabajo final --> float --> N4 
Salida: Nota del estudiante
Notal final --> float --_ N5 
"""
# Entradas
N0 = float(input("la nota del primer parcial\n"))
N1 = float(input("la nota del segundo parcial\n"))
N2 = float(input("la nota del tercer parcial\n"))
N3 = float(input("la nota del examen final\n"))
N4 = float(input("la nota del trabajo final\n"))

# Caja negra
a = float((N0+N1+N2)/3) * 0.55
b = float(N3 * 0.3)
c = float(N4 * 0.15)
d = a + b +c 

# Salidas
print("La nota final es",d)