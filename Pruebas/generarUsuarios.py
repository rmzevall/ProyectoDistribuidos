import csv

# Inicializar contador N en 1
n = 1

# Abrir archivo CSV en modo escritura
with open('datos.csv', mode='w', newline='') as Usuarios:
    escritor = csv.writer(Usuarios)
    # Escribir encabezados de las columnas
    escritor.writerow(["Nombre", "Apellido", "Email", "Contrasena"])
    # Escribir filas en el archivo CSV
    while n <= 10000:
        escritor.writerow([f"Nombre{n}", f"Apellido{n}", f"Nombre{n}Apellido{n}@hotmail.com", f"contrasena{n}"])
        n += 1