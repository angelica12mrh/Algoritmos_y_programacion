"""
Entradas: 2 entradas de valor flotante que son las horas trabajadas y el pago por hora
Pago por hora --> float --> Ph
Horas trabajadas --> float --> h 
Salidas: 1 valor flotante que sería el sueldo neto sacando impuestos 
Sueldo neto --> float --> Neto 
"""
# Entrada
Ph = float(input("Dime el precio por cada hora trabajada\n"))
h = float(input("Dime el numero de horas trabajadas\n"))

# Caja negra
a = Ph*h
Neto = a - a * 0.20

# Salida
print("El salario Neto es",Neto)