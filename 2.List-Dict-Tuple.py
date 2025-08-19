nombres =['Ana','Luis','sofia']

#Dict cration with keys

indice_a_nombre = {}
i=0
for nombre in nombres:
    indice_a_nombre[i]=nombre
    i+=1

#tuple ony with values 
tupla_nombres   = tuple(indice_a_nombre.values())

print(nombres)   
print(indice_a_nombre)
print(tupla_nombres)