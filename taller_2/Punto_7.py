"""
Entradas: 2 dato flotante que seran los metros 
Metros --> float --> m
Salidas: 2 Datos flotanes que serán las pulgadas y los pies
Pulgadas --> float --> p
Pies --> float --> ft
"""

# Entrada
m = float(input("Dime los metros\n"))

# Caja negra
p = m * 39.37 
ft = p / 12

# Salida
print(f"La cantidad de pulgasdas es {p} y la cantidad de pies es {ft}")