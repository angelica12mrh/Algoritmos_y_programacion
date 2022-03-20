"""
Entrada: 2 valores enteros correspondiente a una fecha de nacimientos
Días --> int --> A
Meses --> int --> B
Años --> int --> D
Salidas: 1 valor str con el signo del zodiaco 
Zodiaco --> str --> C
"""
# Entrada 
A = int(input("\nDime el día de tu nacimiento "))
B = int(input("Dime el mes de tu nacimiento "))
C = int(input("Dime el Año de tu nacimiento "))

# Caja negra 
Signo = ["Sagitario", "Capricornio", "Acuario","Picis","Aries","Tauro","Géminis","Cáncer","Leo","Virgo","Libra","Escorpión"]
lista = [22,22,21,20,21,21,22,22,23,24,23,23]
lista0 = [11,12,1,2,3,4,5,6,7,8,9,10]
lista1 = [21,20,19,19,20,21,21,22,23,22,22,21]
lista2 = [12,1,2,3,4,5,6,7,8,9,10,11]
for i in range(12):
    if ((B == lista0[i]) and (A >= lista[i])) or ((B == lista2[i]) and (A <= lista1[i])):
        # Salida
        print("Tu signo es",Signo[i])

# Salida 
print("Tu edad es",2021-C) if B < 10 else print("Tu edad es",2020-C) 