import os
os.system("cls")

r = int(input("ingrese el radio del cilindro : "))
h = int(input("ingrese la altura del cilindro : "))

pi = 3.1416
ab = pi * (r * r)
al = (pi * 2) * r * h
at = (ab * 2) * al

print ("el area base del cilindro es : {:.2f}".format(ab))
print ("el area lateral del cilindro es :{:.2f}".format(al))
print ("el area total del cilindro es :{:.2f}".format(at))