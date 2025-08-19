pares = [('x', 10), ('y', 20), ('z', 30)]

# A diccionario
d = dict(pares)

# Claves como lista (editable) y tupla (solo lectura)
claves_lista = list(d.keys())
valores_tupla = tuple(d.values())

print(pares)         # list de tuplas
print(d)             # dict
print(claves_lista)  # list
print(valores_tupla) # tuple