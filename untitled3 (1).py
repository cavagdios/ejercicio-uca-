import random
numero = random.randint(1,100)
#agregar una lista de 20 posiciones usando el for, y esas 20posiciones poner numeros aleatorios entre 1 y 100

lista=[]
for i in range(20):
    numero = random.randint(1,100)
    lista.append(numero)
print(lista)