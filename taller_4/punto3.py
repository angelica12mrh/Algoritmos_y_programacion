"""
Entradas ----
Salidas: la suma de todos los numeros pares 
Suma --> int --> A
"""

#entrada
A = 0 

# Caja negra 
for i in range(98,1003,2):
    A += i 

# salida
print(f"\n{A}\n") 