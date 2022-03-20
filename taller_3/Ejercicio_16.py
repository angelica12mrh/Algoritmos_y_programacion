"""
Entradas: 3 valores flotantes correspondientes a A, B y C
A --> float --> A 
B --> float --> B
C --> float --> C
Salidas: 2 valores flotantes correspondientes a la solución Ax2 +Bx + C que salen 2 valores x1 y x2
X1 --> float --> E
X2 --> float --> F
"""

# Entrada
A = float(input("\nDime el valor de A "))
B = float(input("Dime el valor de B "))
C =  float(input("Dime el valor de C "))

# Caja negra
D = B**2 -4*A*C
if D == 0:
    E = F = -B/(2*A)
elif D > 0: 
    E = (-B + (B**2 -4*A*C)**0.5)/(2*A)
    print(E)
    F = (-B - (B**2 -4*A*C)**0.5)/(2*A)
else: 
    E = F = "No tiene solución en los reales"

# Salida
print(f"\nEl valor de X1 es: {E}\nEl valor de X2 es: {F}\n") if D >= 0 else print(E,"\n") 