"""
Entradas: 4 entradas de valor flotante, 3 son las ventas de cada departamento y uno el sueldo de los vendedores
Departamento 1 --> float --> A
Departamento 2 --> float --> B 
Departamento 3 --> float --> C
Sueldo --> float --> D
Salidas: 3 valores flotantes que es el sueldo de los vendedores de los departamentos
Departamento 1 --> float --> E 
Departamento 2 --> float --> F 
Departamento 3 --> float --> G
"""

# Entrada
A = float(input("\nDime la ventas del departamento 1 "))
B = float(input("Dime la ventas del departamento 2 "))
C = float(input("Dime la ventas del departamento 3 "))
D = float(input("Dime el sueldo de los vendedores "))

# Caja negra 
Total = (A + B + C)*.33

if A > Total:
    E = D + D*.20 
else:
    E = D
    
if B > Total:
    F = D + D*.20 
else:
    F = D
    
if C > Total:
    G = D + D*.20 
else:
    G = D
    
#saida
print(f"\nEl sueldo para el departamento 1: {E}\nEl sueldo para el departamento 2: {F}\nEl sueldo para el departamento 3: {G}\n")
 