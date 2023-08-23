import os
os.system("cls")

varones = int(input("ingrese la cantidad de varones : "))
mujeres = int(input("ingrese la cantidad de mujeres : "))

total = varones + mujeres 
Pm = (mujeres / total)*100
Pv = (varones / total)*100

print ("porcentaje de varones en el aula :{:.2f}%".format(Pv))
print ("porcentaje de mujeres en el aula :{:.2f}%".format(Pm))