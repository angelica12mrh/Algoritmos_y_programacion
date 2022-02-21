"""
entradas
consume licor-->l-->int
licor preferido-->lp-->int
edad-->e-->int
sexo-->se-->int
seguir-->seg-->int
salidas
personas que consumen licor-->s-->int
mujeres menores de edad-->me_muj-->int
hombres que no consumen aguardiente entre 20 y 25 años-->hom_no_a-->int
promedio edad de quienes consumen cerveza-->cer_e-->int
porcentaje de quienes consumen whisky-->por_w-->int
"""
s=0
me_muj=0
hom_no_a=0
cer_e=[]
whisky=[]
p_w=0
total=[]

while True:
    l=int(input("Consume licor?\nDigite 0 para SI y 1 para NO "))  #entrada
    if l==0:
        s=s+1
        lp=int(input("Licor preferido: "))  #entrada
        e=int(input("Edad: "))  #entrada

        if lp==3:
            cer_e.append(e)
        elif lp==5:
            whisky.append(lp)

        se=int(input("Sexo:\nDigite 0 si es MUJER y 1 si es HOMBRE "))  #entrada

        if se==1 and lp!=1 and e>=20 and e<=25:
            hom_no_a+=1

                          
    elif l==1: 
        lp=0
        e=int(input("Edad: "))  #entrada
        se=int(input("Sexo:\nDigite 0 si es MUJER y 1 si es HOMBRE "))   #entrada
        if se==1 and e>=20 and e<=25:
            hom_no_a+=1  

    total.append(l)

    if e<18 and se==0:
        me_muj=me_muj+1 

    seg=int(input("Desea seguir con la investigacion?\nDigite 0 para SI y 1 para NO "))   #entrada
    if seg==1:
        break

for x in range(len(whisky)):
    if whisky[x]==5: 
            p_w+=1
    
por_w=(p_w*100)/len(total)

#salidas
print(s," son las personas que consumen licor")
print(me_muj," son las mujeres menores de edad")  
print(hom_no_a," son los hombres que no consumen aguardiente y tienen entre 20 y 25 años")

if cer_e:
    print(sum(cer_e)/len(cer_e)," es el promedio de edad de quienes consumen cerveza")
else:
    print("0 es el promedio de edad de quienes consumen cerveza")

print(por_w,"% consumen whisky en relación con el total encuestado")  