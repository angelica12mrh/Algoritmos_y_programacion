from turtle import*
title('practica')
bgcolor('black') #color al fondo


#comandos
speed(5) #tiempo 
pencolor('red') #color a la linea
pensize(3) #tamaño del lapiz
forward(100) #avanzar 
right(90) #girar derecha
forward(100)
left(90) #girar izquierda
forward(100)
backward(50) #regresar
right(90)
forward(100)
circle(60) #circulo 
penup() #omitir linea (no se hace dibuja pero se hace una linea imaginaria)
circle(100)


#bucles 
#1

speed(5)
pencolor('red')
pensize(3)
fillcolor('red') #rellenar o coloriar la figura 
begin_fill() #inicio de fillcolor
for i in range(4): #repeticion
    forward(100)
    right(90)
end_fill() #final de fillcolor

#2

pencolor('purple')
speed(0)
x=1
while x<800:
    colormode(225)
    forward(20+x)
    right(300)
    x+=1


pencolor('purple')
speed(0)
x=1
while x<800:
    forward(20+x)
    right(93)
    x+=1

mainloop()



