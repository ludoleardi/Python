##Richiedo subnet mask (notazione CIDR) e IP di rete (notazione decimale) in input
##Calcolo SM binaria e dectimale
##Calcolo IP di Broadcast
##Calcolo range IP utili
##Stampo i dati

##IP di rete: 192.168.100.0
##Subnet Mask: /26
##255.255.255.192
##IP di broadcast: 192.168.100.63
##Range IP: 192.168.100.1 >> 192.168.100.62

##convertitore binario - decimale
def bintodec(binary):
    decimal = 0 
    binary.reverse()
    for i in range(len(binary)):
        decimal = decimal + (2**i)*binary[i]
    return decimal

##convertitore decimale - binario
def dectobin(decimal):
    binary = []

    for elemento in decimal:
        elem = []
        tmp = elemento
        for i in range(0, 8):
            elem.append(tmp % 2)
            tmp = tmp // 2
        elem.reverse()
        binary.extend(elem)

    return binary

##convertitore lista - stringa, IP decimale puntato 
def list2string(list):
    string = ""

    for elemento in list:
        string = string + str(elemento) + '.'
    
    return string[:-1]

##Richiedo subnet mask in input (notazione CIDR)
cidr = input("Inserisci Subnet Mask (notazione CIDR): ")

if cidr[0] == '/':
    cidr = int(cidr[1:])

else:
    cidr = int(cidr)

##Calcolo SM binaria
smBin = []

for i in range(0, cidr):
    smBin.append(1)

for i in range(0, 32-cidr):
    smBin.append(0)

##Calcolo SM decimale
smDec = []

smDec.append(bintodec(smBin[0:8]))
smDec.append(bintodec(smBin[8:16]))
smDec.append(bintodec(smBin[16:24]))
smDec.append(bintodec(smBin[24:]))

##Richiedo IP di rete in input (notazione decimale)
reteDec = [0, 0, 0, 0]
reteDec[0], reteDec[1], reteDec[2], reteDec[3] = input("Inserisci IP di rete (decimale puntato): ").split('.')
reteDec[0], reteDec[1], reteDec[2], reteDec[3] = int(reteDec[0]), int(reteDec[1]), int(reteDec[2]), int(reteDec[3])

##Calcolo IP di rete binario
reteBin = dectobin(reteDec)

##Calcolo IP di broadcast binario
broadcastBin = []

for i in range(0, cidr):
    broadcastBin.append(reteBin[i])

for i in range(0, 32-cidr):
    broadcastBin.append(1)

##Calcolo IP di broadcast decimale
broadcastDec = []

broadcastDec.append(bintodec(broadcastBin[0:8]))
broadcastDec.append(bintodec(broadcastBin[8:16]))
broadcastDec.append(bintodec(broadcastBin[16:24]))
broadcastDec.append(bintodec(broadcastBin[24:]))

##Calcolo primo e ultimo IP utile
primoBin = reteBin
primoBin[31] = 1

ultimoBin = broadcastBin
ultimoBin[31] = 0

##Converto primo e ultimo IP utile in decimale
primoDec = []

primoDec.append(bintodec(primoBin[0:8]))
primoDec.append(bintodec(primoBin[8:16]))
primoDec.append(bintodec(primoBin[16:24]))
primoDec.append(bintodec(primoBin[24:]))

ultimoDec = []

ultimoDec.append(bintodec(ultimoBin[0:8]))
ultimoDec.append(bintodec(ultimoBin[8:16]))
ultimoDec.append(bintodec(ultimoBin[16:24]))
ultimoDec.append(bintodec(ultimoBin[24:]))

##Stampo i dati
print(f"Subnet Mask decimale: {list2string(smDec)}")
print(f"IP di broadcast: {list2string(broadcastDec)}")
print(f"IP utili: {list2string(primoDec)} >> {list2string(ultimoDec)}")