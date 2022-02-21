"""
Entradas ---
Salidas: todos los numeros enteros impares menores que 100, sin contar multiplos de 7 
Numeros --> int --> A
"""

# Caja negra 
A = 1
for i in range(50):
    if (A%7) != 0:
        print(A) 

# Salida
        A += 2
    else: 
        A += 2