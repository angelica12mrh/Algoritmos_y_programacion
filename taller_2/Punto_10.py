"""
Entradas: 3 Valores flotantes que son el valor de diferentes monedas 
Chelines autriacos --> float --> x 
Dramas griegos --> float --> z
Pesetas --> float --> w 
Salidas 4 valores flotantes que es la conversión de las anteriores monedas
Pesetas --> float --> x
Francos franceses --> float --> z 
Dolares --> float --> a
Liras italianas --> float --> b
"""
# Entradas
x1 = float(input("Dime los chelines autríacos\n"))
z1 = float(input("Dime los dracmas griegos\n"))
w = float(input("Dime las pesetas\n"))

# Caja negra
x = (x1 * 956871)/100
z = z1/22.64572381
a = w/122499
b = (w*100)/9289

# Salidas 
print(f"\n{x1} Chelines austríacos en pesetas son {x}\n{z1} Dracmas griegos en Francos franceses son {z}\n{w} Pesetas en Dolares son {a}\n{w} Pesetas en Liras italianas son {b}\n")
