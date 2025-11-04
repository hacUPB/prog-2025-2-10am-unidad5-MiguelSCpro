nombre_archivo = "./archivos/text.txt"
ubicacion= "c:\\Users\\migue\\OneDrive\\Escritorio\\ARCHIVOS\\"
with open(nombre_archivo,"r",encoding="utf-8") as archivo:
    lista = archivo.readlines()

for c in lista:
    print(c)