inv = {'mouse': 15, 'teclado': 8, 'monitor': 4}

# A lista de tuplas
items_lista = list(inv.items())

# (Reemplazo)
"""def clave(par):
    return par[0]
items_lista.sort(key=clave)"""

# Copia para no perder los datos
aux = items_lista.copy()

# Ordenar por clave usando for (algoritmo de selección)
ordenada = []
while aux:
    menor = aux[0]
    for par in aux:
        if par[0] < menor[0]:  # comparar por la clave
            menor = par
    ordenada.append(menor)
    aux.remove(menor)

# A tupla inmutable
items_tupla = tuple(ordenada)

print(inv)
print(items_lista)   # list de tuplas ordenada
print(ordenada)
print(items_tupla)   # tuple de tuplas ordenada