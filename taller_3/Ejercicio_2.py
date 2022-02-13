""" 
Entradas: 1 valor entero que es el salario de la personas
Salario --> float --> A 
Salidas: 1 valor entero que será el nuevo sueldo del trabajador
Salario neto --> float --> B
"""

# Entrada 
A =float(input("Dime tu salario actual "))

# Caja negra 
if A < 900000: 
    B = (A * 0.15) + A
else:
    B = (A * 0.12) + A
    
# Salida 
print("Tu salario neto es de",B,"")