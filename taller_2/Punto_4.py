"""
Entradas: 1 valor floatante del total de la venta
Total de venta --> float --> Venta
Salidas: La venta con el 15% de descuento
Total --> float --> Total
"""

# Entradas
Venta = float(input("Dime el total de compra\n"))

# Caja negra
Total = Venta - Venta * 0.15

# Salidas
print("El total de la venta es", Total)