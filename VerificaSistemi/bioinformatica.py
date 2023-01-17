PATH = "VerificaSistemi/covid-19_gen1.txt"
SEQUENZA = "ATGTTTGTTTTT" #sequenza iniziale

def contaOccorrenze(stringa):
    contA, contC, contG, contT = 0, 0, 0, 0
    for carattere in stringa: #scorro tutti i caratteri nella stringa e incremento il contatore corrispondente
        if(carattere == 'A'):
            contA += 1
        elif(carattere == 'C'):
            contC += 1
        elif(carattere == 'G'):
            contG += 1
        elif(carattere == 'T'):
            contT += 1

    print(f"A: {contA}, C: {contC}, G: {contG}, T: {contT}")
        

def main():
    file = open(PATH, "r") #apro il file in lettura
    stringa = file.read() #salvo il contenuto del file in una stringa
    file.close()
    #print(stringa)
    contaOccorrenze(stringa)
    #uso la funzione .find(), restituisce la prima posizione in cui appare la sottostringa passata come parametro 
    #all'interno della stringa su cui è invocato il metodo
    print(f"Posizione sequenza iniziale: {stringa.find(SEQUENZA)}") 
    #print(stringa[21870:])

if __name__ == "__main__":
    main()