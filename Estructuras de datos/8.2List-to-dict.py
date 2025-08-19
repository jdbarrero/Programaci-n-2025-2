claves = ['id', 'nombre', 'edad']
valores = [1, 'Ana', 21]

# Construir dict manualmente
info = {}
i = 0
while i < len(claves) and i < len(valores):
    info[claves[i]] = valores[i]
    i += 1

# Tupla de items para “congelar” la vista
items_inmutables = tuple(info.items())

print(claves)            # list
print(info)              # dict
print(items_inmutables)  # tuple de tuplas