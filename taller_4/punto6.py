"""
Entradas: 2 numeros enteros que se procederan a dividir utilizando restas sucesivas
Numero 1 --> int --> A
Numero 2 --> int --> B
Salidas: El resto de la división 
Resto --> int --> A
"""

# Entradas 
A = int(input("\nDime el primer numero (Dividendo) "))
B = int(input("Dime el Segundo numero (Divisor) "))

# Caja negra
print()
C = int(A/B)
N = 0
for i in range(C):
    print(f"{A} - {B} = {A-B}")
    A = A - B
    N += 1

# Salidas
print(f"\nEl resto de la división es {A}")
print(f"El cociente de la dicisión es {N}\n")
