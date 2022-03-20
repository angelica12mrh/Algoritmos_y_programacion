"""
Entradas: 1 Valor Flotante 
Dinero a invertir --> Float --> a
Salidas: El 2% del valor flotante y el valor flotante + el 2%
Ganado por mensualidad --> Float --> b 
Total en un mes --> Float --> c
"""

# Entradas
a = float(input("Dime el dinero que vas a invertir\n"))

# Caja negra
b = a*0.02
c = b + a 

# Salidas
print(f"Tu capital total en un mes es {c} es decir ganaste {b} ") 
