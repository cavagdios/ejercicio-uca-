contra="uca2025"
entrada=""
intentos=0

while entrada!=contra and intentos < 3:
    entrada=input("ingrese contraseña: ")
    if entrada != contra:
        print("contraseña incorrecta:")
        intentos +=1
if entrada == contra:
    print("contraseña correcta")
else:
    print("no hay mas intentos.")