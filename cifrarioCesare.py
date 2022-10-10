cifra = {"a": "b", "b": "c", "c": "d", "d": "e", "e": "f", "f": "g", "g": "h", "h": "i", "i": "l", "l": "m", "m": "n", "n": "o", "o": "p", "p": "q", "q": "r", "r": "s", "s": "t", "t": "u", "u": "v", "v": "w", "w": "z", "z": "a", " ": " "}
decifra = {"z": "w", "w": "v", "v": "u", "u": "t", "t": "s", "s": "r", "r": "q", "q": "p", "p": "o", "o": "n", "n": "m", "m": "l", "l": "i", "i": "h", "h": "g", "g": "f", "f": "e", "e": "d", "d": "c", "c": "b", "b": "a", "a": "z", " ": " "}

decifrata = input("Inserisci una stringa: ")
cifrata = ""


for carattere in decifrata:
    cifrata = cifrata + cifra[carattere]

print(cifrata)

cifrata = input("Inserisci una stringa cifrata: ")
decifrata = ""

for carattere in cifrata:
    decifrata = decifrata + decifra[carattere]

print(decifrata)

for k, v in cifra.items():
    pass