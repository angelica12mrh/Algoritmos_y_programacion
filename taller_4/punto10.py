"""
entradas
altura-->a-->float
continuar-->c-->int
salidas
alturamayor-->a-->float
"""
altura=[]
while True:
    a=float(input("Digite la altura ")) #entradas
    altura.append(a)
    c=int(input("Desea continuar?\nDigite 0 para SI o 1 para NO "))  #entradas
    if(c==1):
        print("La altura mayor es: ",max(altura)) #salidas
        break