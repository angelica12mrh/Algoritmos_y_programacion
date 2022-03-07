usuarios = { 
    "iperurena": { 
        "nombre": "Iñaki", 
        "apellido": "Perurena", 
        "password": "123123" 
    }, 
    "fmuguruza": { 
        "nombre": "Fermín", 
        "apellido": "Muguruza", 
        "password": "654321" 
    }, 
    "aolaizola": { 
        "nombre": "Aimar", 
        "apellido": "Olaizola", 
        "password": "123456" 
    } } 
intentos=1
for i in usuarios:
    u=input("Usuario: ")
    c=input("Contraseña: ")
    if u in usuarios and c==usuarios[u]["password"]:
        nombre=usuarios[u]["nombre"]
        apellido=usuarios[u]["apellido"]
        print(nombre,apellido)
        break
    else:
        print("Fallo intento ",intentos)
        intentos=intentos+1