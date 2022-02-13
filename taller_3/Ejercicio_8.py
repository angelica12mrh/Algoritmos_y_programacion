"""
Entradas: 2 valores enteros P y Q
P --> int --> P 
Q --> int --> Q
Salidas: los 2 valores P y Q mas un mensaje
P --> str --> P 
Q --> str --> Q 
"""

# Entrada 
P = int(input("\nDime el valor de P "))
Q = int(input("Dime el valor de Q "))

# Caja negra
if P**3 + Q**4 - (2*(P**2)) > 680:
    # Salida
    print(str(P) + " y " + str(Q) + " satisfacen la expresión\n")
else: 
    # Salida
    print(str(P) + " y " + str(Q) + " no Satisfacen la expresión\n")