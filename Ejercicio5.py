# Pseudocódigo
# 1. Declaramos constantes: LitrosXGalon, PrecioXLitro
# 2. Inicio
# 3. Leer(consumo)
# 4. total = consumo * LitrosXGalon * PrecioXLitro
# 5. Escribir(total)
# 6. Fin

#Constantes
LitrosXGalon = 3.785
PrecioXLitro = 4.5

consumo = float(input("Ingresar consumo: "))

total = consumo * LitrosXGalon * PrecioXLitro

print("Total: ", total)