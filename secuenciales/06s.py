import os
os.system("cls")

# Definir las constantes pi y las variables r y h

pi = 3.1416
r= float(input("Ingrese el valor del radio del cilindro: "))
h= float(input("Ingrese el valor de la altura del cilindro: "))

# Calcular el área total y el volumen del cilindro
area_total = 2 * pi * r * (r + h)
volumen = pi *(r * r) * h

# Imprimir los resultados
print("El área total del cilindro es : {:.2f}".format(area_total))
print("El volumen del cilindro es : {:.2f}".format(volumen))