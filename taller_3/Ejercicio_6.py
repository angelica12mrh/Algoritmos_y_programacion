"""
Entradas: 4 valores enteros A, B, C y D que vamos a convertir en str
A --> str --> A
B --> str --> B
C --> str --> C
D --> str --> D
Salidas: 1 valores entero redondeado a su centena mas cercana 
N --> int --> N
"""

# Entrada
A = str(input("\nDime el valor de A "))
B = str(input("Dime el valor de B "))
C = str(input("Dime el valor de C "))
D = str(input("Dime el valor de D "))

# Caja negra
N = A + B + C + D
N = int(N)

if N <= (int(A) * 1000 + int(B)*100 + 50):
    N = N - int(C + D) 
else:
    Dn = N - ((int(A)*1000)+ (int(B)*100))
    N = N + 100 - Dn


# Salida 
print(f"\nEl resultado redondeado es {N}\n")