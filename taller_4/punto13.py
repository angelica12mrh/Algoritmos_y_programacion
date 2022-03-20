"""
entradas
nombre-->n-->str
puntajefinal-->pf-->float
seguir-->s-->int
salidas
estudiante mayor puntaje-->str
estudiante menor puntaje-->str
mayorpuntaje-->float
menorpuntaje-->float
porcentaje inferior al promedio-->por_in-->float
porcentaje superior al promedio-->por_su-->float
"""
nombre=[]
puntaje=[]
pun_in = pun_su = 0

while True:
    n=input("Ingrese su nombre ")  #entrada
    pf=float(input("Ingrese su puntaje final "))  #entrada
    nombre.append(n)  
    puntaje.append(pf)

    s=int(input("Desea ingresar mas datos?\nDigite 0 para SI y 1 para NO ")) #entrada
    if s==1:
        break

for x in range(len(puntaje)):
    if puntaje[x]<(sum(puntaje)/len(puntaje)): 
            pun_in+=1
        
    elif puntaje[x]>(sum(puntaje)/len(puntaje)):
            pun_su+=1

por_in=round((pun_in*100)/len(puntaje),2)
por_su=round((pun_su*100)/len(puntaje),2)


p_m=0
pun_m=puntaje[0]

for x in range(len(puntaje)):
    if puntaje[x]>pun_m:
        pun_m=puntaje[x]
        p_m=x
print("El estudiante con mayor puntaje es: ",nombre[p_m])  #salidas
    
for x in range(len(puntaje)):    
    if puntaje[x]<pun_m:
        pun_m=puntaje[x]
        p_m=x
print("El estudiante con menor puntaje es: ",nombre[p_m])  #salidas

#salidas
print("El puntaje maximo obtenido es: ",max(puntaje))
print("El puntaje minimo obtenido es: ",min(puntaje))
print("El promedio de todos los puntajes es: ",round(sum(puntaje)/len(puntaje),2))
print(por_in,'% fue inferior al promedio')
print(por_su,'% fue superior al promedio')