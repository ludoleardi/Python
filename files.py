def leggifile(nome_file):
    """La funzione legge un file"""
    file = open(nome_file, "r")
    lista_righe = file.readlines()
    file.close()

    diz_matematici = {"id": [], "nomi": []}

    for riga in lista_righe[1:]:
        riga_senza_linefeed = riga[:-1]
        lista_campi = riga_senza_linefeed.split(", ")
        id = int(lista_campi[0])
        nome = lista_campi[1]
        diz_matematici["id"].append(id)
        diz_matematici["nomi"].append(nome)

    return diz_matematici

diz = leggifile("Python/files.csv")
print(diz)

