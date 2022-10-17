cifra = {"a": "b", "b": "c", "c": "d", "d": "e", "e": "f", "f": "g", "g": "h", "h": "i", "i": "l", "l": "m", "m": "n", "n": "o", "o": "p", "p": "q", "q": "r", "r": "s", "s": "t", "t": "u", "u": "v", "v": "w", "w": "z", "z": "a", " ": " "}
decifrata = input("Inserisci una stringa: ")
cifrata = ""


for carattere in decifrata:
    cifrata = cifrata + cifra[carattere]

print(cifrata)

cifrata = input("Inserisci una stringa cifrata: ")
decifrata = ""

decifra = {}
for k, v in cifra.items():
    decifra[v] = k

for carattere in cifrata:
    decifrata = decifrata + decifra[carattere]

print(decifrata)