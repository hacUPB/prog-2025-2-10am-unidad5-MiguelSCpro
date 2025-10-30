lista=["Gazz pirobo", "Medallo", "Creep","Mas que amigos","444"]
ubicacion= "c:\\Users\\migue\\OneDrive\\Escritorio\\ARCHIVOS\\"
modo="x"
nombre_archivo = "canciones.txt"
fp = open(ubicacion + nombre_archivo,modo,encoding="utf-8")
for i in lista:
    fp.write(i+"\n")
fp.close()