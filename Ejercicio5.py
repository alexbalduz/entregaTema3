#Constantes
LitrosXGalon = 3.785
PrecioXLitro = 4.5

consumo = float(input("Ingresar consumo: "))

total = consumo * LitrosXGalon * PrecioXLitro

print("Total: ", total)