"""
Entradas: 2 números enteros positivos  N y K
N --> int --> N
K --> int --> K
Salidas: Enteros desde N hasta K
N hasta k--> int --> N
"""

# Entrada 
N = int(input("\nDime el valor de N "))
K = int(input("Dime el valor de K "))

# Caja negra
while K >= N:
    print("\nN tiene que ser mayor que K ")
    N = int(input("Dime el valor de N "))
    K = int(input("\nDime el valor de K "))
    D = N - K + 1
for i in range (D):
    print(N) 

# Salidas
    N -= 1