def verifica(n, div):
    if(n%div == 0):
        print(f"{'Il numero è divisibile per'}  {div}")
    else:
        print(f"{'Il numero non è divisibile per'}  {div}")

n = int(input("Inserisci un numero: "))

verifica(n, 2)
verifica(n, 3)
verifica(n, 5)