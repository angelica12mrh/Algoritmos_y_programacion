"""
Entradas: 2 valores enteros que indican el multiplicador de xp y el xp que dan los mounstruos
Multiplicador --> int --> A
XP --> int --> B
Salidas: El xp que dará el mounstruo actualmente
XP_actual --> int --> C
"""

while True:
    A = input().split() 
    X = int(A[0]) 
    M = int(A[1]) 
    if X == 0 and M == 0:
        break
    else: 
        C = M * X
    print(C) 