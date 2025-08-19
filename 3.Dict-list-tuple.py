#califications dictionary

calif = {'Ana':4.5, 'Luis':3.8, 'Sofia':4.9}

#list to keys (mutability)
claves_lista= list(calif.keys())
claves_lista.append('Nuevo')#only list change 

#tuple keys (inmutbility)

claves_tupla = tuple(calif.keys())

print(calif)
print(claves_lista)
print(claves_tupla)

