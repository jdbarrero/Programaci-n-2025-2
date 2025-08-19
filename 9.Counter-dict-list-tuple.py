lecturas = ['ok', 'fail', 'ok', 'ok', 'fail', 'pending']

# Contar con dict
conteo = {}
for estado in lecturas:
    if estado in conteo:
        conteo[estado] += 1
    else:
        conteo[estado] = 1

# A lista de tuplas para ver resultados
resultados = list(conteo.items())

# Tupla de estados únicos (solo las claves)
estados_unicos = tuple(conteo.keys())

print(lecturas)         # list
print(resultados)       # list de tuplas (estado, frecuencia)
print(estados_unicos)   # tuple de estados