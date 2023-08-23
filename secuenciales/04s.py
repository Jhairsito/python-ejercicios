import os
os.system("cls")

pies = int(input("pies :"))
pulgadas = int(input("pulgadas :"))

estatura = (((pies * 12)+ pulgadas) * 2.54) / 100

print("su estatura en metros es :",format(estatura,".2f"),"m")