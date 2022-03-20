"""
Entradas: 2 valores flotantes que son el valor de venta al público y el precio por el cual lo obtuviste
Venta al público --> float --> PVP
Precio final --> float --> Pf
Salidas: 1 valor flotante que es el descuento aplicado 
Descuento --> float --> D
"""


# Entradas
PVP = float(input("\nDime cual es el precio de venta al público "))
Pf = float(input("Dime cual es el precio final "))        

# Caja negra 
D = 100 -((Pf*100)/PVP)

# Salida
print(f"\nTu descuento fue de {D}%\n")