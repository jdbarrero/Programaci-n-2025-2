valores = [3,1,2,3,2,4,1]

#use set to get differents ones
sin_repetidos_set = set(valores)
sin_repetidos_dict = dict.fromkeys(valores,True)

#list to tuple
sin_repetidos_lista = list(sin_repetidos_dict.keys())
sin_repetidos_tupla = tuple(sin_repetidos_dict.keys())


print(valores)
print(sin_repetidos_set)
print(sin_repetidos_lista)
print(sin_repetidos_tupla)

