



Nombres = []
Edades=[]
Ciudades=[]

import csv

with open("c:\\Users\\migue\\OneDrive\\Escritorio\\ARCHIVOS\\listas.csv", 'w', newline='') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['Nombre', 'Edad', 'Ciudad'])  # Escribe la fila de encabezados
    escritor.writerow(['John', 25, 'Nueva York'])
    escritor.writerow(['Jane', 30, 'Los Ángeles'])

    lector= csv.reader(csvfile)
    encabezado = next(lector)
    for fila in lector:
        nombre = fila[0]
        edad= fila[1]
        ciudad= fila[2]
        Nombres.append(nombre)
        Edades.append(edad)
        Ciudades.append(ciudad)
print(Nombres)
print(Edades)
print(Ciudades)