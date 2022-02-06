"""
Entradas: 1 valor str que es el nombre, 3 valores flotantes que son horas trabajadas, pago por hora, y horas extra
1 valor entero que son la cantidad de hijos
Nombre --> str --> nombre 
Horas normales trabajadas --> float --> horas
Pago por hora --> float --> Ph 
Horas extra --> float --> ex 
Hijos --> int --> hijos
Salidas: 3 valores flotantes, que son la deducciones, las asignaciones y el sueldo neto 
Sueldo neto --> float --> Sueldo 
Asignaciones --> float --> x 
Deduccciones --> float --> Dec
"""
# Entradas
nombre = str(input("\n¿Cuál es tu nombre? "))
horas = float(input("¿Cuantas horas normales has trabajado? ")) 
Ph = float(input("¿Cuanto te pagan por hora normal? "))
ex = float(input("¿Cuantas horas extra has trabajado? "))
hijos = int(input("¿Cuantos hijos tienes? ")) 

# Caja negra
Base = horas * Ph
ex = ex * (Ph + Ph * 0.25)
Sueldob = Base + ex 
Dec = Sueldob * 0.14
x = 430000 + 173000 * hijos
Sueldo = Sueldob - Dec + x 

# Salidas
print(f"\n{nombre} Por asignaciones tienes un total de {x}\nTus deducciones son un total de: {Dec}\ntu sueldo neto es de: {Sueldo}\n")