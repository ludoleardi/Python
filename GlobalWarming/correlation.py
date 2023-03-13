import matplotlib.pyplot as plt
import csv

def co2Emissions(ax):
    anni = []
    totale = []
    gas = []
    liquido = []
    solido = []
    cemento = []
    combustione = []
    procapite = []

    data_file = open("./CO2_emissions.csv")
    data_reader = csv.reader(data_file, delimiter=',')
    next(data_reader)

    for row in data_reader:
        anni.append(str(row[0]))
        totale.append(int(row[1]))
        gas.append(int(row[2]))
        liquido.append(int(row[3]))
        solido.append(int(row[4]))
        cemento.append(int(row[5]))
        combustione.append(int(row[6]))

        if row[7] != '':
            procapite.append(float(row[7]))
        else:
            procapite.append(0.0)
            
    startKey = anni.index('1880')
    anniSlice = anni[startKey::5]
    totaleSlice = totale[startKey::5]
    ax.plot(anniSlice, totaleSlice, 'o-r')
    ax.set_xlabel('Anno')
    ax.set_ylabel('Tonnellate di CO2 emesse')


def temperatureAnomaly(ax):
    anni = []
    valori = []

    data_file = open("./Temperature_Anomaly.csv")
    data_reader = csv.reader(data_file, delimiter=',')
    next(data_reader)

    for row in data_reader:
        anni.append(str(row[0]))
        valori.append(float(row[1]))

    ax.plot(anni[0:-5:5], valori[0:-5:5], 'o-g')
    ax.set_xlabel('Anno')
    ax.set_ylabel('Anomalia di temperatura globale')

def main():
    fig, (ax1, ax2) = plt.subplots(2, 1)
    fig.suptitle = ("Correlazione tra emissioni di CO2 e anomalie di temperatura")

    co2Emissions(ax1)
    temperatureAnomaly(ax2)

    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True
    plt.show()

if __name__ == "__main__":
    main()