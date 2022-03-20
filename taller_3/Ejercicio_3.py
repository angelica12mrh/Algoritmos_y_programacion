"""
Entradas: 4 valores enteros correspondientes a: A, B, C y D
A --> int --> A 
B --> int --> B 
C --> int --> C 
D --> int --> D 
Salidas: un valor flotante con el resultado de la operación 
Resultado de la operación --> float --> E
"""

# Entrada 
A = int(input("Dime el valor de A "))
B = int(input("Dime el valor de B "))
C = int(input("Dime el valor de C "))
D = int(input("Dime el valor de D "))

# Caja negra 
if D == 0:
    E = (A-C)**2
else: 
    E = ((A-B)**3)/D
    
# Salida 
print(f"El resultado es {E} cuando D es igual a {D}")