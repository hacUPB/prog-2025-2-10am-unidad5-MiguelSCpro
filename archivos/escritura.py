ubicacion= "c:\\Users\\migue\\OneDrive\\Escritorio\\ARCHIVOS\\"
nombre_archivo = "fruta.txt"
modo = "w" #Solo escritura - sobreescribe
fp = open(ubicacion + nombre_archivo, modo, encoding="utf-8")
variable_entera= int(input("Ingrese su cuenta de bancolombia: "))
fp.write(f"hola usuario: "+str(variable_entera))
fp.write("\n")
variable_float= float(input("ingrese su saldo: "))
fp.write(f"su saldo es: " + str(variable_float))
fp.write("\n")
fp.close()
