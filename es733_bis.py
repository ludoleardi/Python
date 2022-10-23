import random

def somma(n1, n2):
    return n1 + n2

def sottrazione(n1, n2):
    return n1 - n2

def moltiplicazione(n1, n2):
    return n1 * n2

def divisione(n1, n2):
    return n1 / n2

op = random.randint(0, 3)
n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero: "))

if(op == 0):
    risultato = somma(n1, n2)
elif(op == 1):
    risultato = sottrazione(n1, n2)
elif(op == 2):
    risultato = moltiplicazione(n1, n2)
elif(op == 3):
    risultato = divisione(n1, n2)
else:
    print("Funzione non trovata.")
    exit

print(risultato)

