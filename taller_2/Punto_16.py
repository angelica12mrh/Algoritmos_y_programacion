"""
Entrada: 1 valor flotante de galones 
Galones --> float --> G 
Salida: 1 valor flotante que sería el costo 
"""
# Entrada
G = float(input("Dime la cantidad de galones"))

# Caja negra
G = (G * 3.785 * 50000)

# Salida 
print("El precio es",G,"COP")