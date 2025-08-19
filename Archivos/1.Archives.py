# 1. Escribir en un archivo
with open("notas.txt", "w") as archivo:   # "w" = write (escribir)
    archivo.write("Ana,4.5\n")
    archivo.write("Luis,3.8\n")
    archivo.write("Sofía,4.9\n")

print("Archivo 'notas.txt' creado con éxito.")

# 2. Leer el archivo línea por línea
with open("notas.txt", "r") as archivo:   # "r" = read (leer)
    lineas = archivo.readlines()

print("\nContenido leído del archivo:")
for linea in lineas:
    nombre, nota = linea.strip().split(",")  # separar por coma
    print(f"Estudiante: {nombre} - Nota: {nota}")
