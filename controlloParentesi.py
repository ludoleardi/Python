stringa = "{[3+(a+b)]+8}"
parentesiAperte = ["(", "[", "{"]
parentesiChiuse = [")", "]", "}"]
controllo = {")": "(", "]": "[", "}": "{"}

pila = []

for c in stringa:
    if c in parentesiAperte:
        pila.append(c)

    elif c in parentesiChiuse:
        if controllo[c] != pila.pop():
            break

if len(pila) > 0:
    print("Errore!")
else:
    print("Corretto")
