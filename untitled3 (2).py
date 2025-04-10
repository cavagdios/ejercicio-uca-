import random
numero = random.randint(1,100)
#agregar una lista de 20 posiciones usando el for, y esas 20posiciones poner numeros aleatorios entre 1 y 100

lista=[]
for i in range(20):
    numero = random.randint(1,100)
    if numero not in lista:
        lista.append(numero)
longitud=len(lista)
print(lista)

persona= {"nombre":"rafael","edad":49, "ciudad":"parana"}
print(persona["nombre"])