lista=[12, 23, 5, 12, 92, 5, 12, 5, 29, 92, 64, 23] 
coleccion=list(set(lista))
diccionario={}
tamaño=len(coleccion)-1
while tamaño>=0:
    c=0
    for i in lista:
        if (coleccion[tamaño]==i):
            c=c+1
        diccionario.update({coleccion[tamaño]:c})
    tamaño=tamaño-1
print(diccionario)