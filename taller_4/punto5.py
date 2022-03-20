"""
Entradas: ----
Salidas: El numero de terminos nesesarios para que la exprexión se acerque a 1000
Terminos --> int --> E
Sumatoria --> int --> d
"""
# Caja negra
e = 1
while True:
    d = ((e**2)+1)/e
    if d > 1000:
        e -= 1
        d = ((e**2)+1)/e
        break
    else: 
        print(e)
        e += 1
# Salidas
print("\nEl numero de terminos necesarios es:",e)
print("El resultado de la sumatoria es:",d,"\ncuando k es:",e,"\n")