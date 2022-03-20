"""
Entradas:  2 valores flotantes; el dinero invertido en el banco ; los intereses del banco por su inversión
Dinero invertido en el banco --> float --> A
Intereses del banco --> float --> B
Salidas: El dinero total en el banco
Dinero total --> float --> C
"""

# Entrada
A = float(input("\nHola cuanto dinero tienes invertido en el banco "))
B = float(input("Cuales son los intereses (%) de tu banco por inversión "))

# Caja negra 
B = B/100
C = A * B
E = C + A 

# Salida 
print("El dinero de tu cuenta es",E )  if C > 100000 else print("El dinero de tu cuenta es",A)