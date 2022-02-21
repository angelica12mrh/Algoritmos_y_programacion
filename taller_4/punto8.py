"""
Entradas: un valor entero que va a ser nuesta contraseña
Contraseña --> int --> A 
Salidas: 2 cadenas de texto dependiendo si la contraseña es correcta o no
Correcta --> str --> B 
Incorreta --> str ---> C
"""
# Entrada
A = int(input())

# Caja negra
while A != 2002:
    print("Senha Invalida") 
    A = int(input())

# Salida
print("Acesso Permitido")