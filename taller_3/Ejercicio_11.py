"""
Entradas: 1 valor flotante que es la temperatura en farenheit
Temperatura --> float --> Temp
Salida: 1 valor str que es el deporte mas apto a practicar
Deporte --> str --> B
"""

# Entrada 
Temp = float(input("\nDime tu temperatura en Farenheit "))

# Caja negra 
if Temp > 85:
    B = "Natación"
elif 70 < Temp <= 85:
    B = "Tenis"
elif 32 < Temp <= 70:
    B = "Golf"
elif 10 < Temp <= 32:
    B = "Esquí"
else: 
    B = "Marcha"

# Salida 
print("\n" + B + "\n")