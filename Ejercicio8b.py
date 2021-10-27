import random

#Incializamos contador de intentos
counter_intentos = 0

#Generamos número aleatorio entre el 1 y el 300
aleatorio = random.randint(1, 300)

#Creamos número que introduce el usuario
num_usuario = 0
num_usuario = int(num_usuario)

while num_usuario != aleatorio and counter_intentos < 9:
    num_usuario = int(input("Ingresa un número entre el 1 y el 300: "))
    if aleatorio > num_usuario:
        print("Escribe un número mayor")
    elif aleatorio < num_usuario:
        print("Escribe un número menor")
    else:
        break
    counter_intentos = counter_intentos + 1

if num_usuario == aleatorio:
    print("Has acertado el número " + str(aleatorio) + " en " + str(counter_intentos) + " intentos")
else:
    print("¡Se te acabaron los intentos!")