dizionario = {"w": "avanti", "a": "sinistra", "s": "indietro", "d": "destra", "i": "avanti"}
lista = []

for chiave, valore in dizionario.items():
    print(chiave, valore)

for indice in dizionario:
    if(dizionario[indice] == "avanti"):
        lista.append(indice)

print(lista)