# Lista base
datos = [100, 200, 300]

# A tupla (inmutable)
t = tuple(datos)

# "Modificar" tupla: no se puede, así que genero una NUEVA tupla
nueva_lista = list(t)
nueva_lista[1] = 250
#t[1]=250
t_modificada = tuple(nueva_lista)

# Guardar en dict las dos versiones
historial = {'original': t, 'modificada': t_modificada}

print(t)              # tuple original
print(t_modificada)   # tuple nueva
print(historial)      # dict