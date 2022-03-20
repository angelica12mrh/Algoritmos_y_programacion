"""
Entradas: 1 valor flotante que es el monto total de la compra
Costo total --> float --> A 
Salidas: 3-4 valores flotantes según A, costo fondos de la empresa, la cantidad a pagar a crédito, 
el monto a pagar por intereses  y si es necesario, la cantidad prestada al banco.
Fondos de la empresa --> float --> B
Cantidad a pagar a credito --> float --> C 
Intereses --> float --> D 
Prestamo del banco --> float --> E
"""

# Entrada 
A = float(input("\nDime el valor total de la compra "))

# Caja negra 
if A > 5000000:
    B = float(A*.55)
    C = float(A*.25)
    E = float(A*.30)
    D = float(C*.20)
else:
    B = float(A*.70)
    C = float(A*.30)
    D = float(C*.20)
    E = 0

# Salida 
print(f"\nLos fondos utilizados de la empresa son: {B} \nEl credito al fabricante es de: {C} \nPor intereses del fabricante tenemos {D}\nEl prestamo del banco es: {E}\n")