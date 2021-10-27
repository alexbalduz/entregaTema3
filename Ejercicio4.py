# Pseudocódigo
# 1. Inicio
# 2. Escribir("Ingrese el número de partidos ganados:")
# 3. Leer (PG)
# 4. Escribir("Ingrese el número de partidos empatados:")
# 5. Leer (PE)
# 6. Escribir"Ingrese el número de partidos perdidos:")
# 7. Leer (PP)
# 8. Procedemos a realizar el cálculo de cada grupo de partidos PPG = PG*3, PPE = PE*1, PPP = PP*0
# 9. PuntajeFinal = PPG + PPE + PPP
# 10. Escribir(PF), se imprime el puntaje final
# 11. Fin

print("Ingrese el número de partidos ganados:")
PG = int(input())

print("Ingrese el número de partidos empatados:")
PE = int(input())

print("Ingrese el número de partidos perdidos:")
PP = int(input())

PPG = PG*3
PPE = PE*1
PPP = PP*0

PuntajeFinal = PPG + PPE + PPP

print("Puntaje final: ", PuntajeFinal)