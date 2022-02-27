archivo = open('C:\Users\ASUS\AppData\Roaming\Easeware\DriverEasy\drivers\paises.txt', 'r')

#imprima la posicion de colombia
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(c)

#Imprima todos los paises
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]

#Imprima todas las Capitales
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]

#Imprimir todos los paises que inicien con la letra C
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)

#imprima todas las capitales que inicien con la leta B
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i)  

#Cuente e imprima cuantas ciudades inician con la latra M 
contador=0
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="M"):
    contador=contador+1
    print(contador,i)  

#Imprima todos los paises y capitales, cuyo inicio sea con la letra U
lista=[]
paises=[]
ciudades=[]
for i in archivo:
  a=i.index(":")
  b=i.index(":")
  for m in range(0,a):
    lista.append(i[m])
  a="".join(lista)
  paises.append(a)
  lista=[]
  for r in range(b+2,len(i)):
    lista.append(i[r])
  b="".join(lista)
  ciudades.append(b)
  lista=[]
print("Los paises son:\n")
for i in paises:
  if(i[0]=="U"):
    print(i,"\n")  
print("\nLas ciudades son:\n")
for i in ciudades:
  if(i[0]=="U"):
    print(i)

#Cuente e imprima cuantos paises que hay en el archivo
contador=0
lista=[]
for i in archivo:
  a=i.index(":")
  contador=contador+1
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(contador,a)
  lista=[]

#Busque e imprima la ciudad de Singapur
lista=[]
for i in archivo:
  lista.append(i)
  a="".join(lista)
  if(a[0]=="S" and a[1]=="i" and a[2]=="n"):
    b=a.index(":")
    lista=[]
    break
  lista=[]
for i in range(b+2,len(a)):
  lista.append(a[i])
a="".join(lista)
print(a)

#Busque e imprima el pais de Venezuela y su capital
lista=[]
for i in archivo:
  lista.append(i)
  a="".join(lista)
  if(a[0]=="V" and a[1]=="e" and a[2]=="n"):
    break
  lista=[]
print(a)

#Cuente e imprima las ciudades que su pais inicie con la letra E
contador=0
lista=[]
paises=[]
for i in archivo:
  a=len(i)
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="E"):
    a=i.index(":")
    contador=contador+1
    for r in range(a+2,len(i)):
      lista.append(i[r])
    a="".join(lista)
    lista=[]
    print(contador,a)

#Buesque e imprima la Capiltal de Colombia
lista=[]
for i in archivo:
  lista.append(i)
  a="".join(lista)
  if(a[0]=="C" and a[1]=="o" and a[2]=="l"):
    b=a.index(":")
    lista=[]
    break
  lista=[]
for i in range(b+2,len(a)):
  lista.append(a[i])
a="".join(lista)
print(a)

#imprima la posicion del pais de Uganda
contador=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  contador=contador+1 
  if(a=="Uganda: Kampala\n"):
    break
  lista=[]   
print("La posición de Uganda es:",contador)

#imprima la posicion del pais de Mexico
contador=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  contador=contador+1 
  if(a[0]=="M" and a[2]=="x"):
    break
  lista=[]   
print("La posición de Mexico es:",contador)

#El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato

lista = []
for i in archivo:
    lista.append(i)
file1=open("paises.txt","w")
for i in lista:
  if (i=="Madagascar: rey julien\n"):
    file1.write("Madagascar: Antananarivo\n")
  else:
    file1.write(i)
file1.close()

#Agregue un país que no esté en la lista 
archivo1=open('paises.txt', 'a')
archivo1.write(" \nMinato: pais")
archivo1.close()

