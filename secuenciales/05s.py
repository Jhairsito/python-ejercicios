import os
os.system("cls")

capacidad_gb = float(input("Ingrese la capacidad del disco duro en gigabytes: "))

def convertir_disco_duro(capacidad_gb):
    # Convertir a megabytes
    capacidad_mb = capacidad_gb * 1024

    # Convertir a kilobytes
    capacidad_kb = capacidad_mb * 1024

    # Convertir a bytes
    capacidad_bytes = capacidad_kb * 1024

    return capacidad_mb, capacidad_kb, capacidad_bytes

capacidad_mb, capacidad_kb, capacidad_bytes = convertir_disco_duro(capacidad_gb)

print("Capacidad en megabytes:", capacidad_mb)
print("Capacidad en kilobytes:", capacidad_kb)
print("Capacidad en bytes:", capacidad_bytes)