"""
Entradas: 8 valores enteros para cada billete 
N1 --> int --> N1
N2 --> int --> N2
N3 --> int --> N3
N4 --> int --> N4
N5 --> int --> N5
N6 --> int --> N6
N7 --> int --> N7
N8 --> int --> N8
Salida: el valor total en el banco 
Valor total --> float --> Dinerof 
"""

# Entradas
N1=int(input("\nNumero de billetes que tenga de 50000 "))
N2=int(input("Numero de billetes que tenga de 20000 "))
N3=int(input("Numero de billetes que tenga de 10000 "))
N4=int(input("Numero de billetes que tenga de 5000 "))
N5=int(input("Numero de billetes que tenga de 2000 "))
N6=int(input("Numero de billetes que tenga de 1000 "))
N7=int(input("Numero de billetes que tenga de 500 "))
N8=int(input("Numero de billetes que tenga de 100 "))
 
# Caja negra
Dinerof = (N1*50000)+(N2*20000)+(N3*10000)+(N4*5000)+(N5*2000)+(N6*1000)+(N7*500)+(N8*100)

# Salida
print("El dinero total del banco es",Dinerof)