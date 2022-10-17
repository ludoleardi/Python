from re import X
from pandas import read_csv
from sklearn.tree import DecisionTreeClassifier

giocatori = read_csv('/Users/mac/Documents/Personale/Scuola/Visual_Studio/Python/ai/giocatori.csv') #legge il file csv
X = giocatori.drop(columns = ['videogame']) #salva tutte le colonne tranne videogames
y = giocatori['videogame'] #salva solo la colonna videogames

modello = DecisionTreeClassifier()
modello.fit(X.values, y.values) #il modello viene addestrato in base ai valori del file csv
previsione = modello.predict([[0, 32]]) #lista contentente lista di dati
print(previsione)