import matplotlib.pyplot as plt
import csv

def main():
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

    fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7) = plt.subplots(7, 1)
    ax1.plot(anni, totale, 'o-b')
    ax1.set_ylabel('Totale')
    ax1.set_xlabel('Anno')

    ax2.plot(anni, gas, 'o-b')
    ax2.set_ylabel('Gas')
    ax2.set_xlabel('Anno')

    ax3.plot(anni, liquido, 'o-b')
    ax3.set_ylabel('Liquido')
    ax3.set_xlabel('Anno')

    ax4.plot(anni, solido, 'o-b')
    ax4.set_ylabel('Solido')
    ax4.set_xlabel('Anno')

    ax5.plot(anni, cemento, 'o-b')
    ax5.set_ylabel('Cemento')
    ax5.set_xlabel('Anno')

    ax6.plot(anni, combustione, 'o-b')
    ax6.set_ylabel('Combustione')
    ax6.set_xlabel('Anno')

    ax7.plot(anni, procapite, 'o-b')
    ax7.set_ylabel('Procapite')
    ax7.set_xlabel('Anno')

    plt.show()

if __name__ == "__main__":
    main()