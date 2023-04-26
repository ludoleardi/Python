import matplotlib.pyplot as plt
import csv

PATH = './data.csv'

def main():
    anni = []
    index = []
    coltivato = []
    pascolo = []

    data_file = open(PATH) #apro il file
    data_reader = csv.reader(data_file, delimiter=',')
    next(data_reader) #elimino la riga di intestazione

    for riga in data_reader:
        anni.append(str(riga[0]))
        index.append(float(riga[1]))
        coltivato.append(float(riga[2]))
        pascolo.append(float(riga[3]))

    #print(pascolo)
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
    fig.suptitle('Biodiversità')

    #grafico biodiversità
    ax1.plot(anni, index, 'o-r')
    ax1.set_ylabel('Indice di biodiversità')
    ax1.set_xticks(anni)
    ax1.tick_params(axis='both', which='major', labelsize=8)
    ax1.set_xticklabels(anni, rotation=25, ha='right')

    #grafico terreno coltivato
    ax2.plot(anni, coltivato, 'o-g')
    ax2.set_ylabel('Terreno coltivato')
    ax2.set_xticks(anni)
    ax2.tick_params(axis='both', which='major', labelsize=8)
    ax2.set_xticklabels(anni, rotation=25, ha='right')

    #grafico terreno destinato al pascolo
    ax3.plot(anni, pascolo, 'o-b')
    ax3.set_ylabel('Terreno destinato al pascolo')
    ax3.set_xticks(anni)
    ax3.tick_params(axis='both', which='major', labelsize=8)
    ax3.set_xticklabels(anni, rotation=25, ha='right')

    plt.show()

if __name__ == '__main__':
    main()

############################################################################################################################
"""
1. Figure1_Leardi.png

2. E' visibile una correlazione negativa tra il terreno dedicato alle coltivazioni e l'indice di biodiversità. E' anche possibile
    notare una correlazione diretta tra il terreno destinato al pascolo e l'indice di biodiversità, a partire dal 2004.

3. Secondo Eurostat, quasi il 40 % del suolo dell’UE è utilizzato per la produzione alimentare. Mentre i metodi agricoli 
    tradizionali permettevano la coesistenza tra coltivazioni e una svariata serie di animali e piante, i cambiamenti avvenuti 
    dal 1950 nelle pratiche agricole – a favore di metodi più intensivi e di specializzazione – hanno contribuito a una perdita 
    massiccia di biodiversità. Secondo la relazione dell’AEA «Lo stato della natura nell’UE», il maggiore impiego di concimi, 
    irrigazione e pesticidi, oltre alle intense modifiche dei terreni, gravano pesantemente su fauna e flora locali, 
    in particolar modo sugli uccelli.
    (Fonte: https://www.eea.europa.eu/it/segnali/segnali-2021/articoli/che-cosa-sta-danneggiando-la)
"""