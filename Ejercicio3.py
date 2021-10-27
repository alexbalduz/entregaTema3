# Pseudocódigo
# 1. Inicio
# 2. Escribir("Ingrese el número de respuestas correctas:")
# 3. Leer (RC)
# 4. Escribir("Ingrese el número de respuestas incorrectas:")
# 5. Leer (RI)
# 6. Escribir("Ingrese el número de respuestas en blanco:")
# 7. Leer (RB)
# 8. Procedemos a realizar el cálculo de cada grupo de respuestas PCR = RC*3, PRI = RI*(-1), PRB = RB*0
# 9. PF = PCR + PRI + PRB
# 10. Escribir(PF), se imprime el puntaje final
# 11. Fin



print("Ingrese el número de respuestas correctas:")
RC = int(input())

print("Ingrese el número de respuestas incorrectas:")
RI = int(input())

print("Ingrese el número de respuestas en blanco:")
RB = int(input())

PCR = RC*3
PRI = RI*(-1)
PRB = RB*0

PF = PCR + PRI + PRB

print("El puntaje total es: ", PF)