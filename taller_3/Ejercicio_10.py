"""
Entradas: 1 valor flotante que es el sueldo bruto del trabajador
Sueldo --> float --> A
Salidas: 1 valor entero que es la categoría, y uno flotante que es su nuevo sueldo
Nuevo sueldo --> float --> B 
Categoría --> int --> C
"""
# Entrada 
A = float(input("\nDime tu sueldo bruto "))

# Caja negra
if A <= 900000:
    B = A + A*.60
    C = 5
elif 2000000 >= A > 900000:
    B = A + A*.40
    C = 4
elif 3600000 >= A > 2000000:
    B = A + A*.20
    C = 3
elif 4300000  >= A > 3600000:
    B = A + A*.15
    C = 2
else:
    B = A + A*.10
    C = 1
    
# Salida 
print(f"\nTu sueldo es categoría {C}\nTu nuevo sueldo es de {B}\n")