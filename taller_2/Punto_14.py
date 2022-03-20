"""
Entradas: 3 entradas de valor flotante 2 para consumo actual y anterior y otro para el valor por kilovatio
lectura anterior --> float --> Kw1
Lectura actual --> float --> Kw2 
Valor por kw --> float --> val
Salida: 1 salida de valor flotante que es el consumo total
Consumo total --> float --> T
"""

# Entradas
Kw1 = float(input("\nDime la lectura anterior y la actual "))
Kw2 = float(input())
val = float(input("Dime el valor por kilovatio "))

# Caja negra
T = (Kw2-Kw1)* val

# Salida
print("\nEl valor total es",T ,"\n")