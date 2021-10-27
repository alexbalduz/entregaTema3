# Pseudocódigo
# 1. Variables: velocidad, tiempo, distancia
# 2. Inicio
# 3. Escribir("Ingrese el tiempo en segundos:")
# 4. Leer (tiempo)
# 5. Escribir("Ingrese la velocidad:")
# 6. Leer (distancia)
# 7. distancia = velocidad * tiempo
# 8. Escribir("La distancia recorrida por el móvil es: " + str(distancia) + " metros")
# 9. Fin

print("Ingrese el tiempo en segundos:")
tiempo = float(input())

print("Ingrese la velocidad:")
velocidad = float(input())

distancia = velocidad * tiempo

print("La distancia recorrida por el móvil es: " + str(distancia) + " metros")