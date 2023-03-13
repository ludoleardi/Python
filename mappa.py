import pygame

def caricamappa():
    file = open("/Users/mac/Documents/Personale/Scuola/Visual_Studio/Python/mappa.csv", "r")
    lista_righe = file.readlines()
    mappa = []
    for riga in lista_righe:
        riga_nofeed = riga[:-1]
        lista_campi = riga_nofeed.split(",")
        mappa.append(lista_campi)
    print(mappa)
    return mappa

def main():
    mappa = caricamappa()

    celle = []
    cont = 0
    for riga in mappa:
        lr = []
        for element in riga:
            if element == '0':
                lr.append(cont)
                cont += 1
            elif element == '1':
                lr.append(-1)
        celle.append(lr)

    print(celle)

if __name__ == "__main__":
    main()