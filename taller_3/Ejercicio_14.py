"""
Entradas: 2 valores flotantes que son la lectura anterior y la actual
Anterior --> float --> A
Actual --> float --> B 
Salidas: 1 valor entero que es el total a pagar 
Total --> float --> C
"""

# Entrada 
A = float(input("\nDime la lectura anterior "))
B = float(input("Dime la lectura actual "))
D = (B-A)

# Caja negra 
Valor = [4600, 80000, 100000, 120000]
lista = [0, 100, 300, 500, 100, 300, 500, 1000000000000000000000000000000000] # El ultimo valor para representa infinito

for i in range(4):
    if lista[i] <= D <= lista[4 + i]:
        C = D * Valor[i]

# Salida
print("La cantidad a pagar es de",C,"\n")