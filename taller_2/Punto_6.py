"""
Entradas: 2 Valores enteros uno para la cantidad de hombres y otro para la cantidad de mujeres
Hombres --> int --> H
Mujeres --> int --> M 
Salidas: 2 valores flotantes para indicar el porcentajes de hombres y mujeres
Porcentaje de hombres --> float --> Ph 
Porcentaje de muheres --> float --> Pm
"""
# Entradas
H = int(input("Dime la cantidad de hombres\n"))
M = int(input("Dime la cantidad de mujeres\n"))

# Caja negra
Ph = (H*100)/(H+M)
Pm = (M*100)/(H+M)
 
# Salida
print("El porcentaje de hombres es",Ph,"%","El porcentaje de mujeres es",Pm,"%\n")