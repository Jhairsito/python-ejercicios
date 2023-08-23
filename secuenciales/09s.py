import os
os.system("cls")

Ne = int(input("ingrese un numero entero de 4 cifras : "))

numero_str = str(Ne)

# Inicializar la suma de cifras en cero
suma_cifras = 0

# Sumar cada cifra del número
for cifra in numero_str:
    suma_cifras += int(cifra)

# Mostrar el resultado
print("La suma de las cifras es:", suma_cifras) 