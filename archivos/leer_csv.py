import csv

with open('C:\\Users\\migue\\OneDrive\\Escritorio\\ARCHIVOS\\Variables.csv', 'r') as csvfile:   #usamos el manejador de contexto
    lector = csv.reader(csvfile, delimiter=";") #se utiliza el método reader
    encabezado=next(lector)
    presion=[]
    print(encabezado[3])
    for fila in lector:
        fila[3]= fila[3].replace(",",".")     #con el for se itera sobre el objeto para leer
        dato= float(fila[3])
        presion.append(dato)
print(presion)
        
