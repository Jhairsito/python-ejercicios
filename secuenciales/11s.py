import os
os.system("cls")

numero1 = int(input("ingrese primer numero de 3 cifras :"))
numero2 = int(input("ingrese segundo numero de 3 cifras :"))

N1c1 = numero1 // 100
N1c2 = (numero1 % 100) // 10
N1c3 = numero1 % 10

N2c1 = numero2 // 100
N2c2 = (numero2 % 100) // 10
N2c3 = numero2 % 10

print ("primer numero: ",(N2c3 * 100) + (N1c2 *10) + (N2c1))
print ("segundo numero: ",(N1c3 * 100) + (N2c2 *10) + (N1c1))