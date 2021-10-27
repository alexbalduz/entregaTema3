import random

#Incializamos contador de intentos
counter = 0

#Generamos número aleatorio entre el 1 y el 15
aleatorio = random.randint(1, 15)

#Creamos número que introduce el usuario
num_usuario = 0
num_usuario = int(num_usuario)

while num_usuario != aleatorio:
    num_usuario = int(input("Ingresa un número entre el 1 y el 15: "))
    if aleatorio > num_usuario:
        print("Escribe un número mayor")
    else:
        print("Escribe un número menor")
    counter = counter + 1

print("Has acertado el número " + str(aleatorio) + " en " + str(counter) + " intentos")