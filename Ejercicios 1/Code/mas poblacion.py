import csv
poblacion = [ ]
eliminar = ["--", "NA"]

with open("/Users/jorgebecker/Desktop/A01027251-Database/Ejercicios 1/TextFiles/populationbycountry19802010millions.csv") as archivo:
    archivo_leido = csv.reader(archivo)

    for row in archivo_leido:
        if row[-1] not in eliminar:
            poblacion.append([float(row[-1]), row[0]])

poblacion.sort(reverse=True)
print(poblacion[:5])
