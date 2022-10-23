n = int(input("Inserisci un numero: "))

##l = []
##for i in range(1, n+1):
##   l.append(i)

l = [i for i in range(1, n+1)]  ##list comprehension

print(l)