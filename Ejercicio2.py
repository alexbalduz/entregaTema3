# Pseudocódigo
# 1. Inicio
# 2. Escribir("Ingresa la primera nota:")
# 3. Leer (primeraNota)
# 4. Escribir("Ingresa la segunda nota:")
# 5. Leer (segundaNota)
# 6. Escribir("Ingresa la tercera nota:")
# 7. Leer (terceraNota)
# 8. media = (primeraNota + segundaNota + terceraNota) / 3
# 9. Escribir("La media de las notas parciales es: " + str(media))
# 10. Fin


print("Ingresa la primera nota:")
primeraNota = float(input())

print("Ingresa la segunda nota:")
segundaNota = float(input())

print("Ingresa la tercera nota:")
terceraNota = float(input())

media = (primeraNota + segundaNota + terceraNota) / 3

print("La media de las notas parciales es: " + str(media))