"""
Entradas: 3 valores, uno flotante que es la edad, otro flotante que es nivel de hemoglobina, otro srt que 
es el sexo de la persona 
Edad --> float --> B
Hemoglobina --> float --> C
Sexo --> float --> D
Salidas: 1 cadena de texto que le indica a la persona si esta positivo para hemoglobina
Positivo --> str --> E
"""

# Entrada 
B = float(input("\nDime tu edad en años "))
C = float(input("Dime tu nivel de hemoglobina en g% "))
if B > 15:
    D = float(input("Dime tu sexo, utiliza\n1 para masculino\n2 para femenino\n"))
else: 
    D = 0
# Caja negra 
lista0 = [0,1/12,0.5,1,5,10,15,15]
lista1 = [1/12,0.5,1,5,10,15,100,100]
lista2 = [12,10,11,11.5,12.6,13,14,12]

J = 0
for i in range(8):
    if B <= 15:
        if (lista0[i] < B <= lista1[i]) and (C < lista2[i]):
             print("Positivo para anemia\n") # Salida
        else:
            J += 1
    if J == 8:
        print("Negativo para Anemia\n") # Salida

#salida       
if B > 15:
        if D == float(1):
            if (lista0[7] < B < lista1[7]) and (C < lista2[6]):
                print("Positivo para anemia\n") # Salida
            else: 
                print("Negativo para anemia\n") # Salida
        else:
            if (lista0[6] < B < lista1[6]) and (C < lista2[7]):
                print("Positivo para anemia\n") # Salida
            else: 
                print("Negativo para anemia\n") # Salida