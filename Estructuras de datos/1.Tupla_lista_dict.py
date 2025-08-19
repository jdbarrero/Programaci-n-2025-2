#tuplas (pares clave-valor)
pares = (('a',1),('b',2),('c',3))

#convertir a lista para editar
lista_pares =list(pares)

lista_pares.append(('d',4))

#convertir a diccionario para acceso por clave
d=dict(lista_pares)

#volver a tupla (representación inmutable)

resultado = tuple(d.items())

print (lista_pares)
print(d)
print(resultado)
