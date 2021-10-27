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