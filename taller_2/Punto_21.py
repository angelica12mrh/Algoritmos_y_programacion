"""
Entradas: 2 valores flotantes equivalentes al precio del computar de contados o por cada cuota
Precio de contado --> float --> P 
Precio por cuota --> float --> C 
Salidas: 2 salidas que es el porcentaje de recargo y el procentaje por cuota
Porcentaje --> float --> a
Porcentaje por cuota --> float --> b
"""
# Entrada
P = float(input("\nDimé el valor del Computador pagando de contados\n"))
C = float(input("\nDimé el valor por cada cuota\n "))

# Caja negra
C = C*12
a = (((C*100)/P)-100)
b = (((C*100)/P)-100)/12
# Salida 
print(f"Por recargo el porcentaje es de {a}% y por cuota es de {b}%")