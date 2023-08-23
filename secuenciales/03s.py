import os
os.system("cls")

tramo1 = int(input("Ingrese la longitud en kilometros del tramo 1 : "))
tramo2 = int(input("Ingrese la longitud en pies del tramo 2 : "))
tramo3 = int(input("Ingrese la longitud en millas del tramo 3 : "))

T1 = tramo1 * 1000
T2 = tramo2 * 3.2808
T3 = tramo3 * 1609

Lt = T1 + T2 + T3
Lty = Lt * 1.09361

print ("longitud recorrida en metros :{:.2f}".format(Lt))
print ("longitud recorida en yardas :{:.2f}".format(Lty))