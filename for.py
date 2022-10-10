lista = [2, 1, 3, 4, 5, 6, 7, 8]

#modo preferito (pythonico)
min = lista[0]
max = lista[0]
for elemento in lista:
    if(elemento < min):
        min = elemento
    if(elemento > max):
        max = elemento
    else:
        pass #non fa nulla

print(f"Il minimo è {min} e il massimo è {max}")

#modo C-style
#for i in range(1, len(lista)):
#    print(lista[i], end='-')