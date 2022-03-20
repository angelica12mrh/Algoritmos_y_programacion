"""
Entradas: 3 valores flotantes que seran los 3 lados del triangulo
Lado 1 --> float --> a 
Lado 2 --> float --> b
Lado 3 --> float --> c 
Salida: Un valor flotante equivalente al area del triangulo 
Area --> float --> Area
"""

# Entradas
a = float(input("Dime el los lados de triángulo\n"))
b = float(input())
c = float(input())

# Caja negra
s = (a+b+c)/2
Area = (s*(s-a)*(s-b)*(s-c))**0.5

# Salida
print(Area)