"""
Entradas: 2 valores flotantes que son los bolivares prestados y los cobrados en intereses
Bolivares prestados --> float --> x 
Bolivares por intereses --> float --> i 
Salidas: El interes anual 
Interes anual --> float --> a
"""

# Entradas
x = float(input("¿De cuantos bolivares fue el prestamo?"))
i = float(input("¿Cuánto se pago por intereses?"))

# Caja negra
a = ((i*100)/x)/4

# Salida 
print(f"El interes anual fue de {a}%")