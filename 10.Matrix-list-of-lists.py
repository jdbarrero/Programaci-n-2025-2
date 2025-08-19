matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

# Convertir cada fila a tupla para “congelarla”
i = 0
while i < len(matriz):
    matriz[i] = tuple(matriz[i])
    i += 1

matriz_tupla = tuple(matriz)  # tupla de tuplas

# Diccionario con metadatos
meta = {
    'filas': len(matriz_tupla),
    'columnas': len(matriz_tupla[0]),
    'estructura': 'tupla de tuplas'
}

print(matriz)        # ahora contiene tuplas
print(matriz_tupla)  # tuple de tuplas
print(meta)          # dict