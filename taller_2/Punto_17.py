"""
Entradas: 1 valor flotante corrrespondiente al presupuesto 
Presupuesto --> float --> P 
Salidas: 3 valores flotantes para el presupuesto de cada area
Gineciología --> float --> G 
Traumatología --> float --> T 
Pediatría --> float --> P
"""

# Entrada
P = float(input("\nDime le presupuesto\n")) 

# Caja negra
G = P * 0.40
T = P * 0.30
P = P * 0.30

# Salida
print("Para Ginecología el presuesto es:",G,"Para Traumatología es:",T,"Para Pediatría es:",P,"\n")