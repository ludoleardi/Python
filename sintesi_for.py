lista1=["a", "b", "c", "d"]
lista2 = [1 , 2 , 3 , 4]

#for su lista1 su c-style
for i in range (0, len(lista1), 1):
    print(lista1[i])
    
print("\n")

#for su lista1 python-style
for i in lista1:
    print(i)
    
print("\n")

#for su lista1 con enumerate
for cont, value in enumerate(lista1):
    print (cont, value)

print("\n")

#for su lista1 e lista2 pythoon-style (zip)
for l, n in zip(lista1, lista2):
    print({l}, {n})

print("\n")

#for su lista1 e lista2 c-style(range ..)
for i in range (0, len(lista1), 1):
    print(lista1[i], lista2[i])
    
print("\n")

diz={1: "a", 2 : "b", 3 : "c", 4 :"d"}

#for su diz usando items 
for key, value in diz.items():
    print(key ,value)

print("\n")

#for su diz senza items
for key in diz:
    print(key, diz[key])

print("\n")