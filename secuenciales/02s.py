import os
os.system("cls")

metros = int(input("Ingrese cantidad en metros : "))

centimetro = metros * 100
pulgadas = metros * 39.37
pies = metros * 3.281
yardas = metros * 1.094

print(f"La cantidad ingresadaen tros es equivalente a :\n"f"{centimetro:.2f}centimetros\n"f"{pulgadas:.2f}pulgadas\n"f"{pies:.2f}pies\n"f"{yardas:.2f}yardas")