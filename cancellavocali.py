#carattere = "b"
#print(carattere in vocali) per vedere se appartiene alla lista vocali


vocali = ["a", "e", "i", "o", "u"]
stringa = input("inserisci la tua stringa: ")

caratteri = [c for c in stringa]


def isVocale(c):
    for i in vocali:
        if c == i:
            return False
    return True


senzavocali = [c for c in caratteri if isVocale(c)]
print(senzavocali)