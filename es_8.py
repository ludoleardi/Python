#Scrivi un programma in Python che, assegnata una parola di almeno 8 lettere a una variabile stringa,
#stampi tutta la parola con un carattere ? al posto della terza lettera

parola=input("Dimmi una parola: ")
print(parola[:3], "?", parola[4:])