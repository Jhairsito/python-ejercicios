import os
os.system("cls")

b = int(input("ingrese la base del triangulo : "))
h = int(input("ingrese la altura del triangulo : "))

from math import sqrt

desarrollo = (h * h) + (b * b)
resultado = sqrt(desarrollo) 

print ("la hipotenusa del tianguloo es :{:.2f}".format(resultado)) 